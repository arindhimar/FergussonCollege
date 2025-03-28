from flask import Flask, render_template, request, redirect, url_for, flash, session
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

@app.route('/create_task', methods=['POST'])
def create_task():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    task = Task(
        title=request.form.get('title'),
        description=request.form.get('description'),
        status=request.form.get('status', 'todo'),
        due_date=datetime.strptime(request.form.get('due_date'), '%Y-%m-%d'),
        board_id=request.form.get('board_id'),
        user_id=session['user_id']
    )
    
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('board_dashboard'))

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