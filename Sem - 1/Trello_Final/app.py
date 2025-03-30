from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from enum import Enum
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IaB8kqagM3TeF6pUP9jw9bH9FZPbj3ml'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/trello'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
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
    # Add relationship for board invitations
    received_invitations = db.relationship('BoardInvitation', backref='invitee', lazy=True, foreign_keys='BoardInvitation.invitee_id')
    sent_invitations = db.relationship('BoardInvitation', backref='inviter', lazy=True, foreign_keys='BoardInvitation.inviter_id')

# Add a BoardMember model for board sharing
class BoardMemberRole(Enum):
    VIEWER = 'viewer'
    EDITOR = 'editor'
    ADMIN = 'admin'

class BoardInvitationStatus(Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

class BoardInvitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    inviter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    invitee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.Enum(BoardMemberRole), default=BoardMemberRole.VIEWER)
    status = db.Column(db.Enum(BoardInvitationStatus), default=BoardInvitationStatus.PENDING)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Define unique constraint to prevent duplicate invitations
    __table_args__ = (db.UniqueConstraint('board_id', 'invitee_id', name='unique_board_invitation'),)
    
    board = db.relationship('Board', backref='invitations')

class BoardMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.Enum(BoardMemberRole), default=BoardMemberRole.VIEWER)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Define unique constraint to prevent duplicate memberships
    __table_args__ = (db.UniqueConstraint('board_id', 'user_id', name='unique_board_member'),)

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

# Update the board_dashboard route to include more detailed metrics
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
  
  # Get pending invitations
  pending_invitations = BoardInvitation.query.filter_by(
      invitee_id=user.id, 
      status=BoardInvitationStatus.PENDING
  ).all()
  
  # Calculate task analytics - include both created tasks AND assigned tasks
  created_tasks = Task.query.filter_by(user_id=user.id).all()
  assigned_tasks = Task.query.filter_by(assigned_to=user.id).all()
  
  # Combine tasks without duplicates
  all_user_tasks = created_tasks + [task for task in assigned_tasks if task not in created_tasks]
  total_tasks = len(all_user_tasks)
  
  status_counts = {
      'todo': len([t for t in all_user_tasks if t.status == 'todo']),
      'progress': len([t for t in all_user_tasks if t.status == 'progress']),
      'review': len([t for t in all_user_tasks if t.status == 'review']),
      'done': len([t for t in all_user_tasks if t.status == 'done'])
  }
  
  completion_percent = int((status_counts['done'] / total_tasks * 100)) if total_tasks else 0
  
  # Get upcoming deadlines - include both created and assigned tasks
  upcoming = Task.query.filter(
      ((Task.user_id == user.id) | (Task.assigned_to == user.id)),
      Task.due_date >= datetime.utcnow()
  ).order_by(Task.due_date.asc()).limit(4).all()
  
  # Add team productivity data with enhanced metrics
  team_productivity = []
  if owned_boards:
      for board in owned_boards:
          for member in board.get_members():
              member_tasks = Task.query.filter_by(board_id=board.id, assigned_to=member.id).all()
              if member_tasks:
                  completed = len([t for t in member_tasks if t.status == 'done'])
                  productivity = int((completed / len(member_tasks) * 100)) if member_tasks else 0
                  
                  # Calculate trend (mock data - in a real app, you'd compare with historical data)
                  trend = 'up' if productivity > 50 else ('down' if productivity < 25 else None)
                  
                  team_productivity.append({
                      'name': member.username,
                      'initials': member.username[:2].upper(),
                      'productivity': productivity,
                      'completed': completed,
                      'total': len(member_tasks),
                      'trend': trend
                  })
  
  return render_template(
      'board_dashboard.html',
      user=user,
      boards=all_boards,
      status_counts=status_counts,
      total_tasks=total_tasks,
      completion_percent=completion_percent,
      upcoming=upcoming,
      team_productivity=team_productivity,
      pending_invitations=pending_invitations
  )

@app.route('/create_board', methods=['POST'])
def create_board():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    board = Board(
        name=request.form.get('name'),
        color=request.form.get('color', 'blue'),
        user_id=session['user_id'],
        is_private=request.form.get('private') == 'on'
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
    board.is_private = request.form.get('is_private') == 'on'
    
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
    
    return render_template(
        'board-view.html',
        board=board,
        tasks_by_status=tasks_by_status,
        session=session
    )

# API endpoints for board data
@app.route('/api/boards/<int:board_id>', methods=['GET'])
def get_board(board_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user has access to this board
    is_member = BoardMember.query.filter_by(board_id=board_id, user_id=session['user_id']).first()
    if board.user_id != session['user_id'] and not is_member:
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
            flash('Error: Tasks can only be assigned to board members. Please add the user to the board first.', 'error')
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
    
    flash('Task created successfully!', 'success')
    return redirect(url_for('board_view', board_id=board_id))

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
            flash('Error: Tasks can only be assigned to board members. Please add the user to the board first.', 'error')
            return redirect(url_for('board_view', board_id=task.board_id))
    else:
        task.assigned_to = None
    
    db.session.commit()
    
    flash('Task updated successfully!', 'success')
    return redirect(url_for('board_view', board_id=task.board_id))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    task = Task.query.get_or_404(task_id)
    board = Board.query.get(task.board_id)
    
    # Check if user has access to this task
    is_member = BoardMember.query.filter_by(board_id=task.board_id, user_id=session['user_id']).first()
    if task.user_id != session['user_id'] and board.user_id != session['user_id'] and not is_member:
        abort(403)
    
    board_id = task.board_id
    db.session.delete(task)
    db.session.commit()
    
    flash('Task deleted successfully!', 'success')
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
    board = Board.query.get(task.board_id)
    
    # Check if user has access to this task
    is_member = BoardMember.query.filter_by(board_id=task.board_id, user_id=session['user_id']).first()
    if task.user_id != session['user_id'] and board.user_id != session['user_id'] and not is_member:
        return jsonify({'error': 'Forbidden'}), 403
    
    task.status = new_status
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    task = Task.query.get_or_404(task_id)
    board = Board.query.get(task.board_id)
    
    # Check if user has access to this task
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

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Board Members Management
@app.route('/manage_members/<int:board_id>')
def manage_members(board_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user is the owner or admin
    is_admin = BoardMember.query.filter_by(
        board_id=board_id, 
        user_id=session['user_id'], 
        role=BoardMemberRole.ADMIN
    ).first()
    
    if board.user_id != session['user_id'] and not is_admin:
        flash('You do not have permission to manage members for this board', 'error')
        return redirect(url_for('board_view', board_id=board_id))
    
    # Get all users except the current user and existing members
    existing_member_ids = [member.user_id for member in board.members]
    existing_member_ids.append(board.user_id)  # Add the owner
    
    # Also exclude users with pending invitations
    pending_invitation_user_ids = [
        inv.invitee_id for inv in BoardInvitation.query.filter_by(
            board_id=board_id, 
            status=BoardInvitationStatus.PENDING
        ).all()
    ]
    
    excluded_user_ids = list(set(existing_member_ids + pending_invitation_user_ids))
    
    available_users = User.query.filter(User.id.notin_(excluded_user_ids)).all()
    
    # Get pending invitations for this board
    pending_invitations = BoardInvitation.query.filter_by(
        board_id=board_id, 
        status=BoardInvitationStatus.PENDING
    ).all()
    
    return render_template(
        'manage_members.html',
        board=board,
        available_users=available_users,
        pending_invitations=pending_invitations
    )

@app.route('/invite_board_member/<int:board_id>', methods=['POST'])
def invite_board_member(board_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user is the owner or admin
    is_admin = BoardMember.query.filter_by(
        board_id=board_id, 
        user_id=session['user_id'], 
        role=BoardMemberRole.ADMIN
    ).first()
    
    if board.user_id != session['user_id'] and not is_admin:
        flash('You do not have permission to invite members to this board', 'error')
        return redirect(url_for('board_view', board_id=board_id))
    
    user_id = request.form.get('user_id')
    role = request.form.get('role', 'viewer')
    
    if not user_id:
        flash('Please select a user to invite', 'error')
        return redirect(url_for('manage_members', board_id=board_id))
    
    # Check if user exists
    user = User.query.get(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('manage_members', board_id=board_id))
    
    # Check if user is already a member
    existing_member = BoardMember.query.filter_by(board_id=board_id, user_id=user_id).first()
    if existing_member:
        flash('User is already a member of this board', 'error')
        return redirect(url_for('manage_members', board_id=board_id))
    
    # Check if there's already a pending invitation
    existing_invitation = BoardInvitation.query.filter_by(
        board_id=board_id, 
        invitee_id=user_id,
        status=BoardInvitationStatus.PENDING
    ).first()
    
    if existing_invitation:
        flash('An invitation has already been sent to this user', 'error')
        return redirect(url_for('manage_members', board_id=board_id))
    
    # Create a new invitation
    role_value = role.lower() if role else 'viewer'
    invitation = BoardInvitation(
        board_id=board_id,
        inviter_id=session['user_id'],
        invitee_id=user_id,
        role=BoardMemberRole(role_value),
        status=BoardInvitationStatus.PENDING
    )
    
    db.session.add(invitation)
    db.session.commit()
    
    flash(f'Invitation sent to {user.username}', 'success')
    return redirect(url_for('manage_members', board_id=board_id))

@app.route('/cancel_invitation/<int:invitation_id>', methods=['POST'])
def cancel_invitation(invitation_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    invitation = BoardInvitation.query.get_or_404(invitation_id)
    board = Board.query.get(invitation.board_id)
    
    # Check if user is the owner, admin, or the one who sent the invitation
    is_admin = BoardMember.query.filter_by(
        board_id=invitation.board_id, 
        user_id=session['user_id'], 
        role=BoardMemberRole.ADMIN
    ).first()
    
    if board.user_id != session['user_id'] and invitation.inviter_id != session['user_id'] and not is_admin:
        flash('You do not have permission to cancel this invitation', 'error')
        return redirect(url_for('board_view', board_id=invitation.board_id))
    
    db.session.delete(invitation)
    db.session.commit()
    
    flash('Invitation cancelled successfully', 'success')
    return redirect(url_for('manage_members', board_id=invitation.board_id))

@app.route('/respond_to_invitation/<int:invitation_id>/<string:action>', methods=['POST'])
def respond_to_invitation(invitation_id, action):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    invitation = BoardInvitation.query.get_or_404(invitation_id)
    
    # Check if the current user is the invitee
    if invitation.invitee_id != session['user_id']:
        flash('You do not have permission to respond to this invitation', 'error')
        return redirect(url_for('board_dashboard'))
    
    if action == 'accept':
        # Create a new board member
        member = BoardMember(
            board_id=invitation.board_id,
            user_id=invitation.invitee_id,
            role=invitation.role
        )
        
        db.session.add(member)
        invitation.status = BoardInvitationStatus.ACCEPTED
        db.session.commit()
        
        flash('You have joined the board successfully!', 'success')
    elif action == 'reject':
        invitation.status = BoardInvitationStatus.REJECTED
        db.session.commit()
        
        flash('Invitation rejected', 'success')
    else:
        flash('Invalid action', 'error')
    
    return redirect(url_for('board_dashboard'))

@app.route('/update_board_member_role/<int:board_id>/<int:user_id>', methods=['POST'])
def update_board_member_role(board_id, user_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user is the owner or admin
    is_admin = BoardMember.query.filter_by(
        board_id=board_id, 
        user_id=session['user_id'], 
        role=BoardMemberRole.ADMIN
    ).first()
    
    if board.user_id != session['user_id'] and not is_admin:
        flash('You do not have permission to update member roles', 'error')
        return redirect(url_for('board_view', board_id=board_id))
    
    role = request.form.get('role')
    
    # Update the member's role
    member = BoardMember.query.filter_by(board_id=board_id, user_id=user_id).first()
    if member:
        # Convert role to lowercase to match enum values
        role_value = role.lower() if role else 'viewer'
        member.role = BoardMemberRole(role_value)
        db.session.commit()
        flash('Member role updated successfully', 'success')
    else:
        flash('Member not found', 'error')
    
    return redirect(url_for('manage_members', board_id=board_id))

@app.route('/remove_board_member/<int:board_id>/<int:user_id>', methods=['POST'])
def remove_board_member(board_id, user_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user is the owner or admin
    is_admin = BoardMember.query.filter_by(
        board_id=board_id, 
        user_id=session['user_id'], 
        role=BoardMemberRole.ADMIN
    ).first()
    
    if board.user_id != session['user_id'] and not is_admin:
        flash('You do not have permission to remove members', 'error')
        return redirect(url_for('board_view', board_id=board_id))
    
    # Remove the member
    member = BoardMember.query.filter_by(board_id=board_id, user_id=user_id).first()
    if member:
        # Check if member has any assigned tasks
        assigned_tasks = Task.query.filter_by(board_id=board_id, assigned_to=user_id).all()
        for task in assigned_tasks:
            task.assigned_to = None
        
        db.session.delete(member)
        db.session.commit()
        flash('Member removed successfully', 'success')
    else:
        flash('Member not found', 'error')
    
    return redirect(url_for('manage_members', board_id=board_id))

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

# Update the profile route to include assigned tasks
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    user = User.query.get_or_404(session['user_id'])
    
    # Get boards owned by the user
    owned_boards = Board.query.filter_by(user_id=user.id).all()
    
    # Get boards shared with the user
    shared_boards = Board.query.join(BoardMember).filter(BoardMember.user_id == user.id).all()
    
    # Get tasks created by the user
    created_tasks = Task.query.filter_by(user_id=user.id).all()
    
    # Get tasks assigned to the user
    assigned_tasks = Task.query.filter_by(assigned_to=user.id).all()
    
    return render_template(
        'profile.html',
        user=user,
        boards=owned_boards,
        shared_boards=shared_boards,
        created_tasks=created_tasks,
        assigned_tasks=assigned_tasks
    )

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

