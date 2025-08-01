from flask import Flask, render_template, request, redirect, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user

# Setting the Flask App 
app = Flask(__name__)
app.secret_key = 'super-secret-key-donotshare'

# MySQL configuration for database using SQLALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:flaskpass123@localhost/role_auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize of database 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)

# Login Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # ⚠️ Legacy warning, but okay for now

# Homepage
@app.route('/')
def home():
    return redirect('/select-role')

#Role Selection Page
@app.route('/select-role')
def select_role():
    return render_template('index.html')

# Registration Page (Students Only)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        raw_password = request.form['password']

        if not username or not raw_password:
            flash('All fields are required.')
            return redirect('/register')

        existing = User.query.filter_by(username=username).first()
        if existing:
            flash('Username already exists.')
            return redirect('/register')

        hashed_pw = bcrypt.generate_password_hash(raw_password).decode('utf-8')
        new_user = User(username=username, password=hashed_pw, role='student')
        db.session.add(new_user)
        db.session.commit()
        flash('Registered successfully. Please login.')
        return redirect('/login?role=student')

    return render_template('register.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    role = request.args.get('role')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful.')

            if user.role == 'admin':
                return redirect('/admin')
            else:
                return redirect('/student')

        flash('Invalid login. Check your credentials.')
        return redirect('/login?role=' + role)

    return render_template('login.html', role=role)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect('/login')

# Change Password
@app.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        current_pw = request.form['current_password']
        new_pw = request.form['new_password']

        if not bcrypt.check_password_hash(current_user.password, current_pw):
            flash('Current password is incorrect.')
            return redirect('/change-password')

        current_user.password = bcrypt.generate_password_hash(new_pw).decode('utf-8')
        db.session.commit()
        flash('Password updated successfully.')
        return redirect('/')

    return render_template('change_password.html')

# Admin Dashboard
@app.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        abort(403)
    users = User.query.all()
    return render_template('dashboard.html', users=users)

#Student Dashboard
@app.route('/student')
@login_required
def student():
    if current_user.role != 'student':
        abort(403)
    return render_template('welcome.html', user=current_user)

# Error Page for Unauthorized Access 
@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

#Run App + Seed Admin 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            hashed_pw = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin = User(username='admin', password=hashed_pw, role='admin')
            db.session.add(admin)
            db.session.commit()
            print("✅ Admin created: admin / admin123")
        else:
            print("⚠️ Admin already exists.")
    app.run(debug=True)
