from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Task

def init_routes(app):
    
    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email').upper()
            password = request.form.get('password')
            hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
            role = 'Admin' if User.query.first() is None else 'User'
            new_user = User(username=username, email=email, password=hashed_pw, role=role)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email').upper()
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('dashboard'))
            flash('Invalid Credentials')
        return render_template('login.html')

    @app.route('/dashboard')
    @login_required
    def dashboard():
        page = request.args.get('page', 1, type=int)
        status_filter = request.args.get('status', 'All')
        query = Task.query if current_user.role == 'Admin' else Task.query.filter_by(user_id=current_user.id)
        if status_filter != 'All':
            query = query.filter_by(status=status_filter)
        tasks_pagination = query.paginate(page=page, per_page=5)
        return render_template('dashboard.html', tasks=tasks_pagination, current_status=status_filter)

    @app.route('/task/new', methods=['GET', 'POST'])
    @login_required
    def new_task():
        if current_user.role != 'Admin': return redirect(url_for('dashboard'))
        users = User.query.filter_by(role='User').all()
        if request.method == 'POST':
            new_t = Task(title=request.form.get('title'), 
                         description=request.form.get('description'), 
                         user_id=request.form.get('assigned_to'))
            db.session.add(new_t)
            db.session.commit()
            return redirect(url_for('dashboard'))
        return render_template('create_task.html', users=users)

    @app.route('/task/complete/<int:task_id>')
    @login_required
    def complete_task(task_id):
        task = db.session.get(Task, task_id)
        if task and (task.user_id == current_user.id or current_user.role == 'Admin'):
            task.status = 'Completed'
            db.session.commit()
        return redirect(url_for('dashboard'))

    @app.route('/task/delete/<int:task_id>')
    @login_required
    def delete_task(task_id):
        task = db.session.get(Task, task_id)
        if task and current_user.role == 'Admin':
            db.session.delete(task)
            db.session.commit()
        return redirect(url_for('dashboard'))

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('login'))