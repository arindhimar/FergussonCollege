from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
# Add these imports at the top
from enum import Enum
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IaB8kqagM3TeF6pUP9jw9bH9FZPbj3ml'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/trello'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
# Update the User model to include more profile information
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    avatar = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    boards = db.relationship('Board', backref='owner', lazy=True, foreign_keys='Board.user_id')
    tasks = db.relationship('Task', backref='creator', lazy=True, foreign_keys='Task.user_id')
    assigned_tasks = db.relationship('Task', backref='assignee', lazy=True, foreign_keys='Task.assigned_to')
    # Add relationship for board memberships
    board_memberships = db.relationship('BoardMember', backref='user', lazy=True)

# Add a BoardMember model for board sharing
class BoardMemberRole(Enum):
    VIEWER = 'viewer'
    EDITOR = 'editor'
    ADMIN = 'admin'

class BoardMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.Enum(BoardMemberRole), default=BoardMemberRole.VIEWER)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Define unique constraint to prevent duplicate memberships
    __table_args__ = (db.UniqueConstraint('board_id', 'user_id', name='unique_board_member'),)

# Update the Board model to include members
class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(20), nullable=False, default='blue')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='board', lazy=True, cascade='all, delete-orphan')
    members = db.relationship('BoardMember', backref='board', lazy=True, cascade='all, delete-orphan')
    is_private = db.Column(db.Boolean, default=True)
    
    def get_members(self):
        return [member.user for member in self.members]

# Update the Task model to include assignment
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False, default='todo')
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    @property
    def status_color(self):
        colors = {
            'todo': 'red',
            'progress': 'yellow',
            'review': 'blue',
            'done': 'green'
        }
        return colors.get(self.status, 'gray')

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        flash('Passwords do not match!', 'error')
        return redirect(url_for('home'))

    existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
    if existing_user:
        flash('User already exists with this email/username', 'error')
        return redirect(url_for('home'))

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    flash('Registration successful! Please login.', 'success')
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Invalid email or password', 'error')
        return redirect(url_for('home'))

    session['user_id'] = user.id
    flash('Login successful!', 'success')
    return redirect(url_for('board_dashboard'))

# Update the board_dashboard route to include shared boards
@app.route('/board_dashboard')
def board_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    user = User.query.get(session['user_id'])
    
    if not user:
        session.pop('user_id', None)
        flash('Session expired. Please login again.', 'error')
        return redirect(url_for('home'))
    
    # Get boards owned by the user
    owned_boards = Board.query.filter_by(user_id=user.id).all()
    
    # Get boards shared with the user
    shared_boards = Board.query.join(BoardMember).filter(BoardMember.user_id == user.id).all()
    
    # Combine owned and shared boards
    all_boards = owned_boards + [board for board in shared_boards if board not in owned_boards]
    
    # Calculate task analytics
    tasks = Task.query.filter_by(user_id=user.id).all()
    total_tasks = len(tasks)
    
    status_counts = {
        'todo': len([t for t in tasks if t.status == 'todo']),
        'progress': len([t for t in tasks if t.status == 'progress']),
        'review': len([t for t in tasks if t.status == 'progress']),
        'done': len([t for t in tasks if t.status == 'review']),
        'done': len([t for t in tasks if t.status == 'done'])
    }
    
    completion_percent = int((status_counts['done'] / total_tasks * 100)) if total_tasks else 0
    
    # Get upcoming deadlines
    upcoming = Task.query.filter(
        Task.user_id == user.id,
        Task.due_date >= datetime.utcnow()
    ).order_by(Task.due_date.asc()).limit(4).all()
    
    # Add team productivity data
    team_productivity = []
    if owned_boards:
        for board in owned_boards:
            for member in board.get_members():
                member_tasks = Task.query.filter_by(board_id=board.id, assigned_to=member.id).all()
                if member_tasks:
                    completed = len([t for t in member_tasks if t.status == 'done'])
                    productivity = int((completed / len(member_tasks) * 100)) if member_tasks else 0
                    team_productivity.append({
                        'name': member.username,
                        'initials': member.username[:2].upper(),
                        'productivity': productivity
                    })
    
    return render_template(
        'board_dashboard.html',
        user=user,
        boards=all_boards,
        status_counts=status_counts,
        total_tasks=total_tasks,
        completion_percent=completion_percent,
        upcoming=upcoming,
        team_productivity=team_productivity
    )

@app.route('/create_board', methods=['POST'])
def create_board():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    board = Board(
        name=request.form.get('name'),
        color=request.form.get('color', 'blue'),
        user_id=session['user_id']
    )
    
    db.session.add(board)
    db.session.commit()
    return redirect(url_for('board_dashboard'))


@app.route('/update_board/<int:board_id>', methods=['POST'])
def update_board(board_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    board = Board.query.get_or_404(board_id)
    if board.user_id != session['user_id']:
        abort(403)

    board.name = request.form.get('name')
    board.color = request.form.get('color', 'blue')
    
    db.session.commit()
    return redirect(url_for('board_dashboard'))

@app.route('/delete_board/<int:board_id>', methods=['POST'])
def delete_board(board_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    board = Board.query.get_or_404(board_id)
    if board.user_id != session['user_id']:
        abort(403)

    db.session.delete(board)
    db.session.commit()
    return redirect(url_for('board_dashboard'))

# New route for board view
@app.route('/board-view')
def board_view():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    board_id = request.args.get('board_id')
    if not board_id:
        flash('Board not found', 'error')
        return redirect(url_for('board_dashboard'))
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user has access to this board
    is_member = BoardMember.query.filter_by(board_id=board_id, user_id=session['user_id']).first()
    if board.user_id != session['user_id'] and not is_member:
        abort(403)
    
    # Get tasks grouped by status
    tasks_by_status = {
        'todo': Task.query.filter_by(board_id=board_id, status='todo').all(),
        'progress': Task.query.filter_by(board_id=board_id, status='progress').all(),
        'review': Task.query.filter_by(board_id=board_id, status='review').all(),
        'done': Task.query.filter_by(board_id=board_id, status='done').all()
    }
    
    # Get board members for task assignment
    board_members = []
    
    # Add the owner
    owner = User.query.get(board.user_id)
    board_members.append(owner)
    
    # Add all members
    for member in board.members:
        member_user = User.query.get(member.user_id)
        if member_user and member_user not in board_members:
            board_members.append(member_user)
    
    return render_template(
        'board-view.html',
        board=board,
        tasks_by_status=tasks_by_status,
        board_members=board_members
    )

# API endpoints for board data
@app.route('/api/boards/<int:board_id>', methods=['GET'])
def get_board(board_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user has access to this board
    if board.user_id != session['user_id']:
        return jsonify({'error': 'Forbidden'}), 403
    
    # Get tasks grouped by status
    tasks_by_status = {
        'todo': [{'id': t.id, 'title': t.title, 'description': t.description, 'due_date': t.due_date.isoformat() if t.due_date else None} 
                for t in Task.query.filter_by(board_id=board_id, status='todo').all()],
        'progress': [{'id': t.id, 'title': t.title, 'description': t.description, 'due_date': t.due_date.isoformat() if t.due_date else None} 
                    for t in Task.query.filter_by(board_id=board_id, status='progress').all()],
        'review': [{'id': t.id, 'title': t.title, 'description': t.description, 'due_date': t.due_date.isoformat() if t.due_date else None} 
                  for t in Task.query.filter_by(board_id=board_id, status='review').all()],
        'done': [{'id': t.id, 'title': t.title, 'description': t.description, 'due_date': t.due_date.isoformat() if t.due_date else None} 
                for t in Task.query.filter_by(board_id=board_id, status='done').all()]
    }
    
    return jsonify({
        'id': board.id,
        'name': board.name,
        'color': board.color,
        'tasks': tasks_by_status
    })

# Add a new route to get board members for a specific board
@app.route('/api/boards/<int:board_id>/members', methods=['GET'])
def get_board_members(board_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user has access to this board
    is_member = BoardMember.query.filter_by(board_id=board_id, user_id=session['user_id']).first()
    if board.user_id != session['user_id'] and not is_member:
        return jsonify({'error': 'Forbidden'}), 403
    
    # Get the owner
    owner = User.query.get(board.user_id)
    
    # Get all members
    members = []
    members.append({
        'id': owner.id,
        'username': owner.username,
        'email': owner.email,
        'role': 'owner'
    })
    
    for member in board.members:
        user = User.query.get(member.user_id)
        if user:
            members.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': member.role.value
            })
    
    return jsonify(members)

# Update the create_task route to properly handle task assignment
@app.route('/create_task', methods=['POST'])
def create_task():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    board_id = request.form.get('board_id')
    board = Board.query.get_or_404(board_id)
    
    # Check if user has access to this board
    is_member = BoardMember.query.filter_by(board_id=board_id, user_id=session['user_id']).first()
    if board.user_id != session['user_id'] and not is_member:
        abort(403)
    
    due_date = None
    if request.form.get('due_date'):
        due_date = datetime.strptime(request.form.get('due_date'), '%Y-%m-%d')
    
    assigned_to = request.form.get('assigned_to')
    if assigned_to and assigned_to.isdigit():
        assigned_to = int(assigned_to)
        
        # Verify the assignee is a member of the board
        is_valid_assignee = False
        if assigned_to == board.user_id:  # Board owner
            is_valid_assignee = True
        else:
            board_member = BoardMember.query.filter_by(board_id=board_id, user_id=assigned_to).first()
            if board_member:
                is_valid_assignee = True
        
        if not is_valid_assignee:
            flash('Invalid assignee selected', 'error')
            return redirect(url_for('board_view', board_id=board_id))
    else:
        assigned_to = None
    
    task = Task(
        title=request.form.get('title'),
        description=request.form.get('description'),
        status=request.form.get('status', 'todo'),
        due_date=due_date,
        board_id=board_id,
        user_id=session['user_id'],
        assigned_to=assigned_to
    )
    
    db.session.add(task)
    db.session.commit()
    
    # Redirect back to board view
    return redirect(url_for('board_view', board_id=board_id))

# Update the update_task route to properly handle task assignment
@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    task = Task.query.get_or_404(task_id)
    board = Board.query.get(task.board_id)
    
    # Check if user has access to this task
    is_member = BoardMember.query.filter_by(board_id=task.board_id, user_id=session['user_id']).first()
    if task.user_id != session['user_id'] and board.user_id != session['user_id'] and not is_member:
        abort(403)
    
    task.title = request.form.get('title')
    task.description = request.form.get('description')
    task.status = request.form.get('status')
    
    if request.form.get('due_date'):
        task.due_date = datetime.strptime(request.form.get('due_date'), '%Y-%m-%d')
    else:
        task.due_date = None
    
    assigned_to = request.form.get('assigned_to')
    if assigned_to and assigned_to.isdigit():
        assigned_to = int(assigned_to)
        
        # Verify the assignee is a member of the board
        is_valid_assignee = False
        if assigned_to == board.user_id:  # Board owner
            is_valid_assignee = True
        else:
            board_member = BoardMember.query.filter_by(board_id=task.board_id, user_id=assigned_to).first()
            if board_member:
                is_valid_assignee = True
        
        if is_valid_assignee:
            task.assigned_to = assigned_to
        else:
            flash('Invalid assignee selected', 'error')
    else:
        task.assigned_to = None
    
    db.session.commit()
    
    # Redirect back to board view
    return redirect(url_for('board_view', board_id=task.board_id))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    task = Task.query.get_or_404(task_id)
    
    # Check if user has access to this task
    if task.user_id != session['user_id']:
        abort(403)
    
    board_id = task.board_id
    db.session.delete(task)
    db.session.commit()
    
    # Redirect back to board view
    return redirect(url_for('board_view', board_id=board_id))

# API endpoint to update task status (for drag and drop)
@app.route('/api/tasks/<int:task_id>/status', methods=['PUT'])
def update_task_status(task_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    new_status = data.get('status')
    
    if not new_status:
        return jsonify({'error': 'Status is required'}), 400
    
    task = Task.query.get_or_404(task_id)
    
    # Check if user has access to this task
    if task.user_id != session['user_id']:
        return jsonify({'error': 'Forbidden'}), 403
    
    task.status = new_status
    db.session.commit()
    
    return jsonify({'success': True})

# Add a new route to handle task assignment via API
@app.route('/api/tasks/<int:task_id>/assign', methods=['POST'])
def assign_task(task_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    assignee_id = data.get('assignee_id')
    
    task = Task.query.get_or_404(task_id)
    board = Board.query.get(task.board_id)
    
    # Check if user has permission to assign tasks
    is_member = BoardMember.query.filter_by(board_id=task.board_id, user_id=session['user_id']).first()
    if task.user_id != session['user_id'] and board.user_id != session['user_id'] and not is_member:
        return jsonify({'error': 'Forbidden'}), 403
    
    if assignee_id:
        # Verify the assignee is a member of the board
        is_valid_assignee = False
        if int(assignee_id) == board.user_id:  # Board owner
            is_valid_assignee = True
        else:
            board_member = BoardMember.query.filter_by(board_id=task.board_id, user_id=assignee_id).first()
            if board_member:
                is_valid_assignee = True
        
        if is_valid_assignee:
            task.assigned_to = int(assignee_id)
        else:
            return jsonify({'error': 'Invalid assignee'}), 400
    else:
        task.assigned_to = None
    
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Add these routes for user profile and settings

# Update the profile route to properly handle user data
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    user = User.query.get(session['user_id'])
    
    # Get user's boards
    boards = Board.query.filter_by(user_id=user.id).all()
    
    # Get boards shared with the user through board memberships
    shared_boards_query = db.session.query(Board).join(BoardMember).filter(BoardMember.user_id == user.id)
    shared_boards = shared_boards_query.all()
    
    # Get tasks created by the user
    created_tasks = Task.query.filter_by(user_id=user.id).all()
    
    # Get tasks assigned to the user
    assigned_tasks = Task.query.filter_by(assigned_to=user.id).all()
    
    return render_template(
        'profile.html',
        user=user,
        boards=boards,
        shared_boards=shared_boards,
        created_tasks=created_tasks,
        assigned_tasks=assigned_tasks
    )

# Update the update_profile route to handle file uploads properly
@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    user = User.query.get(session['user_id'])
    
    user.full_name = request.form.get('full_name', user.full_name)
    user.bio = request.form.get('bio', user.bio)
    
    # Handle avatar upload if provided
    if 'avatar' in request.files:
        avatar = request.files['avatar']
        if avatar and avatar.filename:
            # Create directory if it doesn't exist
            avatar_dir = os.path.join('static', 'avatars')
            if not os.path.exists(avatar_dir):
                os.makedirs(avatar_dir)
            
            # Save avatar to a directory and update user.avatar
            filename = secure_filename(f"{user.id}_{avatar.filename}")
            avatar_path = os.path.join(avatar_dir, filename)
            avatar.save(avatar_path)
            user.avatar = f'/static/avatars/{filename}'
    
    db.session.commit()
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('profile'))

@app.route('/board_settings/<int:board_id>')
def board_settings(board_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user is the owner or admin
    if board.user_id != session['user_id'] and not any(
        member.user_id == session['user_id'] and member.role == BoardMemberRole.ADMIN
        for member in board.members
    ):
        abort(403)
    
    # Get all users for member selection
    users = User.query.filter(User.id != session['user_id']).all()
    
    # Get current board members
    board_members = BoardMember.query.filter_by(board_id=board_id).all()
    
    return render_template(
        'board_settings.html',
        board=board,
        users=users,
        board_members=board_members
    )

@app.route('/add_board_member/<int:board_id>', methods=['POST'])
def add_board_member(board_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user is the owner or admin
    if board.user_id != session['user_id'] and not any(
        member.user_id == session['user_id'] and member.role == BoardMemberRole.ADMIN
        for member in board.members
    ):
        abort(403)
    
    user_id = request.form.get('user_id')
    role = request.form.get('role', 'VIEWER')
    
    # Check if user exists
    user = User.query.get(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('board_settings', board_id=board_id))
    
    # Check if user is already a member
    existing_member = BoardMember.query.filter_by(board_id=board_id, user_id=user_id).first()
    if existing_member:
        flash('User is already a member of this board', 'error')
        return redirect(url_for('board_settings', board_id=board_id))
    
    # Add user as a member
    member = BoardMember(
        board_id=board_id,
        user_id=user_id,
        role=BoardMemberRole(role)
    )
    
    db.session.add(member)
    db.session.commit()
    
    flash(f'{user.username} has been added to the board', 'success')
    return redirect(url_for('board_settings', board_id=board_id))

@app.route('/remove_board_member/<int:board_id>/<int:user_id>', methods=['POST'])
def remove_board_member(board_id, user_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user is the owner or admin
    if board.user_id != session['user_id'] and not any(
        member.user_id == session['user_id'] and member.role == BoardMemberRole.ADMIN
        for member in board.members
    ):
        abort(403)
    
    # Remove the member
    member = BoardMember.query.filter_by(board_id=board_id, user_id=user_id).first()
    if member:
        db.session.delete(member)
        db.session.commit()
        flash('Member removed successfully', 'success')
    else:
        flash('Member not found', 'error')
    
    return redirect(url_for('board_settings', board_id=board_id))

@app.route('/update_board_member_role/<int:board_id>/<int:user_id>', methods=['POST'])
def update_board_member_role(board_id, user_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user is the owner or admin
    if board.user_id != session['user_id'] and not any(
        member.user_id == session['user_id'] and member.role == BoardMemberRole.ADMIN
        for member in board.members
    ):
        abort(403)
    
    role = request.form.get('role')
    
    # Update the member's role
    member = BoardMember.query.filter_by(board_id=board_id, user_id=user_id).first()
    if member:
        member.role = BoardMemberRole(role)
        db.session.commit()
        flash('Member role updated successfully', 'success')
    else:
        flash('Member not found', 'error')
    
    return redirect(url_for('board_settings', board_id=board_id))

@app.template_filter('status_color')
def status_color_filter(status):
    colors = {
        'todo': 'red',
        'progress': 'yellow',
        'review': 'blue',
        'done': 'green'
    }
    return colors.get(status, 'gray')

@app.template_filter('time_until')
def time_until_filter(due_date):
    now = datetime.utcnow()
    delta = due_date - now
    days = delta.days + delta.seconds // 86400
    
    if days < 0:
        return 'Overdue'
    elif days == 0:
        return 'Today'
    elif days == 1:
        return 'Tomorrow'
    return f'In {days} days'

# Update the API endpoint for getting task details to include assigned_to
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    task = Task.query.get_or_404(task_id)
    
    # Check if user has access to this task
    board = Board.query.get(task.board_id)
    is_member = BoardMember.query.filter_by(board_id=task.board_id, user_id=session['user_id']).first()
    if task.user_id != session['user_id'] and board.user_id != session['user_id'] and not is_member:
        return jsonify({'error': 'Forbidden'}), 403
    
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'due_date': task.due_date.isoformat() if task.due_date else None,
        'board_id': task.board_id,
        'assigned_to': task.assigned_to
    })


if __name__ == '__main__':
    # Create upload directories
    avatar_dir = os.path.join('static', 'avatars')
    if not os.path.exists(avatar_dir):
        os.makedirs(avatar_dir)
        
    with app.app_context():
        db.create_all()
    app.run(debug=True)

