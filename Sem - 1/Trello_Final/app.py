from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

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
    boards = db.relationship('Board', backref='user', lazy=True)
    tasks = db.relationship('Task', backref='user', lazy=True)

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(20), nullable=False, default='blue')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='board', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False, default='todo')
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
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

@app.route('/board_dashboard')
def board_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    user = User.query.get(session['user_id'])
    
    # Calculate task analytics
    tasks = Task.query.filter_by(user_id=user.id).all()
    total_tasks = len(tasks)
    
    status_counts = {
        'todo': len([t for t in tasks if t.status == 'todo']),
        'progress': len([t for t in tasks if t.status == 'progress']),
        'review': len([t for t in tasks if t.status == 'review']),
        'done': len([t for t in tasks if t.status == 'done'])
    }
    
    completion_percent = int((status_counts['done'] / total_tasks * 100)) if total_tasks else 0
    
    # Get upcoming deadlines
    upcoming = Task.query.filter(
        Task.user_id == user.id,
        Task.due_date >= datetime.utcnow()
    ).order_by(Task.due_date.asc()).limit(4).all()
    
    return render_template(
        'board_dashboard.html',
        user=user,
        boards=user.boards,
        status_counts=status_counts,
        total_tasks=total_tasks,
        completion_percent=completion_percent,
        upcoming=upcoming
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
    if board.user_id != session['user_id']:
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
        tasks_by_status=tasks_by_status
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

@app.route('/create_task', methods=['POST'])
def create_task():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    board_id = request.form.get('board_id')
    board = Board.query.get_or_404(board_id)
    
    # Check if user has access to this board
    if board.user_id != session['user_id']:
        abort(403)
    
    due_date = None
    if request.form.get('due_date'):
        due_date = datetime.strptime(request.form.get('due_date'), '%Y-%m-%d')
    
    task = Task(
        title=request.form.get('title'),
        description=request.form.get('description'),
        status=request.form.get('status', 'todo'),
        due_date=due_date,
        board_id=board_id,
        user_id=session['user_id']
    )
    
    db.session.add(task)
    db.session.commit()
    
    # Redirect back to board view
    return redirect(url_for('board_view', board_id=board_id))

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    task = Task.query.get_or_404(task_id)
    
    # Check if user has access to this task
    if task.user_id != session['user_id']:
        abort(403)
    
    task.title = request.form.get('title')
    task.description = request.form.get('description')
    task.status = request.form.get('status')
    
    if request.form.get('due_date'):
        task.due_date = datetime.strptime(request.form.get('due_date'), '%Y-%m-%d')
    
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

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

