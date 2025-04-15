from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from enum import Enum
import os
from werkzeug.utils import secure_filename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import timedelta
import atexit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IaB8kqagM3TeF6pUP9jw9bH9FZPbj3ml'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/trello'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size


# SMTP Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Example for Gmail
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'alvfcoc@gmail.com'
app.config['MAIL_PASSWORD'] = 'owjz jode vsjb kgdn'
app.config['MAIL_DEFAULT_SENDER'] = 'alvfcoc@gmail.com'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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
    skills = db.relationship('UserSkill', backref='user', lazy=True, cascade='all, delete-orphan')

# Add UserSkill model after User model
class UserSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill = db.Column(db.String(50), nullable=False)
    proficiency = db.Column(db.Integer, default=1)  # 1-5 scale
    
    __table_args__ = (db.UniqueConstraint('user_id', 'skill', name='unique_user_skill'),)

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
    technologies = db.Column(db.String(255))
    cost = db.Column(db.Float)
    deadline = db.Column(db.DateTime)
    
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
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Keep for backward compatibility
    priority = db.Column(db.String(20), default='medium')  # high, medium, low
    technology = db.Column(db.String(50))

    @property
    def status_color(self):
        colors = {
            'todo': 'red',
            'progress': 'yellow',
            'review': 'blue',
            'done': 'green'
        }
        return colors.get(self.status, 'gray')
        
    @property
    def priority_color(self):
        colors = {
            'high': 'red',
            'medium': 'yellow',
            'low': 'green'
        }
        return colors.get(self.priority, 'gray')
        
    @property
    def assignees(self):
        return [assignee.user for assignee in self.assignees_rel]

# Add TaskAssignee model after Task model
class TaskAssignee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('task_id', 'user_id', name='unique_task_assignee'),)
    
    task = db.relationship('Task', backref='assignees_rel')
    user = db.relationship('User')


# Email Utility Functions
def send_email(to, subject, body_html, body_text=None):
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = app.config['MAIL_DEFAULT_SENDER']
        msg['To'] = to

        part1 = MIMEText(body_text, 'plain') if body_text else None
        part2 = MIMEText(body_html, 'html')

        if part1:
            msg.attach(part1)
        msg.attach(part2)

        with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
            server.starttls()
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            server.sendmail(app.config['MAIL_DEFAULT_SENDER'], [to], msg.as_string())
    except Exception as e:
        app.logger.error(f"Failed to send email: {str(e)}")

def send_invitation_email(invitee_email, board_name, inviter_name):
    subject = f"You've been invited to join the board '{board_name}'"
    html = f"""
    <html>
        <body>
            <p>Hello,</p>
            <p>{inviter_name} has invited you to join the board '{board_name}' on TaskFlow.</p>
            <p>Please check your dashboard to accept or reject the invitation.</p>
            <br>
            <p>Best regards,<br>TaskFlow Team</p>
        </body>
    </html>
    """
    send_email(invitee_email, subject, html)

def send_task_assignment_email(user_email, task_title, board_name, assigner_name):
    subject = f"New task assigned: {task_title}"
    html = f"""
    <html>
        <body>
            <p>Hello,</p>
            <p>{assigner_name} has assigned you to the task '{task_title}' in board '{board_name}'.</p>
            <p>Please check the task details and update your progress accordingly.</p>
            <br>
            <p>Best regards,<br>TaskFlow Team</p>
        </body>
    </html>
    """
    send_email(user_email, subject, html)

def send_deadline_reminder_email(user_email, task_title, board_name, due_date):
    subject = f"Deadline approaching for task: {task_title}"
    html = f"""
    <html>
        <body>
            <p>Hello,</p>
            <p>This is a reminder that the task '{task_title}' in board '{board_name}'</p>
            <p>is due on {due_date.strftime('%Y-%m-%d %H:%M')}.</p>
            <br>
            <p>Best regards,<br>TaskFlow Team</p>
        </body>
    </html>
    """
    send_email(user_email, subject, html)
    

def check_deadlines():
    with app.app_context():
        now = datetime.utcnow()
        upcoming = Task.query.filter(
            Task.due_date > now,
            Task.due_date <= now + timedelta(hours=24)
        ).all()

        for task in upcoming:
            assignees = [task.creator]  # Add logic to get all assignees
            if task.assignees:
                assignees += [a.user for a in task.assignees_rel]
            
            for user in set(assignees):
                send_deadline_reminder_email(
                    user.email,
                    task.title,
                    task.board.name,
                    task.due_date
                )



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

# Update create_board route to handle new fields
@app.route('/create_board', methods=['POST'])
def create_board():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    # Parse deadline if provided
    deadline = None
    if request.form.get('deadline'):
        try:
            deadline = datetime.strptime(request.form.get('deadline'), '%Y-%m-%d')
        except ValueError:
            flash('Invalid deadline format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('board_dashboard'))
    
    # Parse cost if provided
    cost = None
    if request.form.get('cost'):
        try:
            cost = float(request.form.get('cost'))
        except ValueError:
            flash('Invalid cost value. Please enter a number.', 'error')
            return redirect(url_for('board_dashboard'))

    board = Board(
        name=request.form.get('name'),
        color=request.form.get('color', 'blue'),
        user_id=session['user_id'],
        is_private=request.form.get('private') == 'on',
        technologies=request.form.get('technologies'),
        cost=cost,
        deadline=deadline
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
    
    # Update new fields
    if request.form.get('technologies'):
        board.technologies = request.form.get('technologies')
        
    if request.form.get('deadline'):
        try:
            board.deadline = datetime.strptime(request.form.get('deadline'), '%Y-%m-%d')
        except ValueError:
            flash('Invalid deadline format. Please use YYYY-MM-DD.', 'error')
            
    if request.form.get('cost'):
        try:
            board.cost = float(request.form.get('cost'))
        except ValueError:
            flash('Invalid cost value. Please enter a number.', 'error')
    
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
    
    # Get the current user
    user = User.query.get_or_404(session['user_id'])
    
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
        session=session,
        user=user  # Pass the user to the template
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
        'technologies': board.technologies,
        'cost': board.cost,
        'deadline': board.deadline.isoformat() if board.deadline else None,
        'is_private': board.is_private,
        'tasks': tasks_by_status
    })

# Update create_task route to handle new fields and multiple assignees
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
    
    # Create the task
    task = Task(
        title=request.form.get('title'),
        description=request.form.get('description'),
        status=request.form.get('status', 'todo'),
        due_date=due_date,
        board_id=board_id,
        user_id=session['user_id'],
        priority=request.form.get('priority', 'medium'),
        technology=request.form.get('technology')
    )
    
    # Handle single assignee for backward compatibility
    assigned_to = request.form.get('assigned_to')
    if assigned_to and assigned_to.isdigit():
        task.assigned_to = int(assigned_to)
    
    db.session.add(task)
    db.session.commit()
    
    # Handle multiple assignees
    assignees = request.form.getlist('assignees[]')
    for assignee_id in assignees:
        if assignee_id and assignee_id.isdigit():
            user_id = int(assignee_id)
            
            # Verify the assignee is a member of the board
            is_valid_assignee = False
            if user_id == board.user_id:  # Board owner
                is_valid_assignee = True
            else:
                board_member = BoardMember.query.filter_by(board_id=board_id, user_id=user_id).first()
                if board_member:
                    is_valid_assignee = True
            
            if is_valid_assignee:
                task_assignee = TaskAssignee(task_id=task.id, user_id=user_id)
                db.session.add(task_assignee)
                user = User.query.get(user_id)
                send_task_assignment_email(user.email, task.title, board.name, user.username)
    
    db.session.commit()
    
    flash('Task created successfully!', 'success')
    return redirect(url_for('board_view', board_id=board_id))

# Update update_task route to handle new fields and multiple assignees
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
    task.priority = request.form.get('priority', 'medium')
    task.technology = request.form.get('technology')
    
    if request.form.get('due_date'):
        task.due_date = datetime.strptime(request.form.get('due_date'), '%Y-%m-%d')
    else:
        task.due_date = None
    
    # Handle single assignee for backward compatibility
    assigned_to = request.form.get('assigned_to')
    if assigned_to and assigned_to.isdigit():
        task.assigned_to = int(assigned_to)
    else:
        task.assigned_to = None
    
    # Handle multiple assignees - first remove existing assignees
    TaskAssignee.query.filter_by(task_id=task.id).delete()
    
    # Add new assignees
    assignees = request.form.getlist('assignees[]')
    for assignee_id in assignees:
        if assignee_id and assignee_id.isdigit():
            user_id = int(assignee_id)
            
            # Verify the assignee is a member of the board
            is_valid_assignee = False
            if user_id == board.user_id:  # Board owner
                is_valid_assignee = True
            else:
                board_member = BoardMember.query.filter_by(board_id=task.board_id, user_id=user_id).first()
                if board_member:
                    is_valid_assignee = True
            
            if is_valid_assignee:
                task_assignee = TaskAssignee(task_id=task.id, user_id=user_id)
                db.session.add(task_assignee)
                user = User.query.get(user_id)
                send_task_assignment_email(user.email, task.title, board.name, user.username)
    
    db.session.commit()
    
    flash('Task updated successfully!', 'success')
    return redirect(url_for('board_view', board_id=task.board_id))

# Add a route for deleting tasks
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    task = Task.query.get_or_404(task_id)
    board_id = task.board_id
    board = Board.query.get(board_id)
    
    # Check if user has permission to delete this task
    is_admin = BoardMember.query.filter_by(
        board_id=board_id, 
        user_id=session['user_id'], 
        role=BoardMemberRole.ADMIN
    ).first()
    
    if task.user_id != session['user_id'] and board.user_id != session['user_id'] and not is_admin:
        flash('You do not have permission to delete this task', 'error')
        return redirect(url_for('board_view', board_id=board_id))
    
    # Delete task assignees first
    TaskAssignee.query.filter_by(task_id=task_id).delete()
    
    # Delete the task
    db.session.delete(task)
    db.session.commit()
    
    flash('Task deleted successfully', 'success')
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
    is_member = BoardMember.query.filter_by(
        board_id=board.id,  # Corrected from board.board_id to board.id
        user_id=session['user_id']
    ).first()
    
    if task.user_id != session['user_id'] and board.user_id != session['user_id'] and not is_member:
        return jsonify({'error': 'Forbidden'}), 403
    
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'due_date': task.due_date.isoformat() if task.due_date else None,
        'board_id': task.board_id,
        'assigned_to': task.assigned_to,
        'priority': task.priority,
        'technology': task.technology
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

# Update the invite_board_member function to handle existing invitations
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
    
    # Delete any existing invitation records for this user and board
    BoardInvitation.query.filter_by(board_id=board_id, invitee_id=user_id).delete()
    
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
    send_invitation_email(user.email, board.name, user.username)

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

# Update the remove_board_member function to also delete any invitation records
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
        
        # Delete any invitation records for this user and board
        BoardInvitation.query.filter_by(board_id=board_id, invitee_id=user_id).delete()
        
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

# Add route for updating user profile
@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    user = User.query.get_or_404(session['user_id'])
    
    # Update user information
    user.full_name = request.form.get('full_name')
    user.bio = request.form.get('bio')
    
    # Handle avatar upload
    if 'avatar' in request.files and request.files['avatar'].filename:
        avatar_file = request.files['avatar']
        if avatar_file:
            # Generate a secure filename
            filename = secure_filename(f"{user.username}_{int(datetime.utcnow().timestamp())}.jpg")
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Save the file
            avatar_file.save(filepath)
            
            # Update user avatar path
            user.avatar = f"/static/uploads/{filename}"
    
    db.session.commit()
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('profile'))

# Add route for managing user skills
@app.route('/manage_skills', methods=['GET', 'POST'])
def manage_skills():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    user = User.query.get_or_404(session['user_id'])
    
    if request.method == 'POST':
        # Clear existing skills
        UserSkill.query.filter_by(user_id=user.id).delete()
        
        # Add new skills
        skills = request.form.getlist('skill[]')
        proficiencies = request.form.getlist('proficiency[]')
        
        for i in range(len(skills)):
            if skills[i].strip():
                skill = UserSkill(
                    user_id=user.id,
                    skill=skills[i].strip(),
                    proficiency=int(proficiencies[i]) if i < len(proficiencies) else 1
                )
                db.session.add(skill)
        
        db.session.commit()
        flash('Skills updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    # Common skills for dropdown suggestions
    common_skills = ['Python', 'JavaScript', 'PHP', 'Java', 'C#', 'Ruby', 'Go', 'Swift', 
                    'HTML', 'CSS', 'React', 'Angular', 'Vue', 'Node.js', 'Django', 
                    'Flask', 'Laravel', 'Spring', 'ASP.NET', 'SQL', 'MongoDB', 'AWS', 
                    'Docker', 'Kubernetes', 'DevOps', 'UI/UX Design', 'Project Management']
    
    return render_template(
        'manage_skills.html',
        user=user,
        common_skills=common_skills
    )

# Add route to get users by skill for task assignment
@app.route('/api/users_by_skill/<string:skill>', methods=['GET'])
def get_users_by_skill(skill):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    board_id = request.args.get('board_id')
    if not board_id:
        return jsonify({'error': 'Board ID is required'}), 400
    
    board = Board.query.get_or_404(board_id)
    
    # Check if user has access to this board
    is_member = BoardMember.query.filter_by(board_id=board_id, user_id=session['user_id']).first()
    if board.user_id != session['user_id'] and not is_member:
        return jsonify({'error': 'Forbidden'}), 403
    
    # Get all users who are members of the board and have the required skill
    skilled_users = User.query.join(UserSkill).filter(
        UserSkill.skill == skill,
        User.id.in_([board.user_id] + [member.user_id for member in board.members])
    ).all()
    
    # Get all other users who are members of the board
    other_users = User.query.filter(
        User.id.in_([board.user_id] + [member.user_id for member in board.members]),
        ~User.id.in_([user.id for user in skilled_users])
    ).all()
    
    # Format the response
    result = {
        'skilled_users': [{'id': user.id, 'username': user.username, 'proficiency': next((s.proficiency for s in user.skills if s.skill == skill), 0)} for user in skilled_users],
        'other_users': [{'id': user.id, 'username': user.username} for user in other_users]
    }
    
    return jsonify(result)

# Add a new API endpoint to get task assignees
@app.route('/api/task_assignees/<int:task_id>', methods=['GET'])
def get_task_assignees(task_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    task = Task.query.get_or_404(task_id)
    board = Board.query.get(task.board_id)
    
    # Check if user has access to this task
    is_member = BoardMember.query.filter_by(board_id=board.board_id, user_id=session['user_id']).first()
    if task.user_id != session['user_id'] and board.user_id != session['user_id'] and not is_member:
        return jsonify({'error': 'Forbidden'}), 403
    
    # Get assignees
    assignees = []
    
    # Add primary assignee if it exists
    if task.assigned_to:
        primary_assignee = User.query.get(task.assigned_to)
        if primary_assignee:
            assignees.append({
                'id': primary_assignee.id,
                'username': primary_assignee.username
            })
    
    # Add other assignees from TaskAssignee model
    task_assignees = TaskAssignee.query.filter_by(task_id=task.id).all()
    for ta in task_assignees:
        # Skip if already added as primary assignee
        if ta.user_id == task.assigned_to:
            continue
        
        assignees.append({
            'id': ta.user_id,
            'username': ta.user.username
        })
    
    return jsonify({
        'assignees': assignees
    })
    


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=check_deadlines, trigger='interval', hours=1)
    scheduler.start()

