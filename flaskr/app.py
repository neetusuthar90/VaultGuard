from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySql initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Secret key generation
secret_key = os.urandom(32)
app.config['secret_key'] = secret_key

login_manager = LoginManager()
login_manager.init_app(app)

#define login model

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), index = True, unique = True)
    email = db.Column(db.String(150), index = True, unique = True)
    password_hash = db.Column(db.String(150))

def set_password(self,password):
    self.password_hash = generate_password_hash(password)

def check_password(self,password):
    return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# add route for home page
from flask import Flask,render_template,flash

@app.route('/home')
def home():
    return render_template('index.html')

#add route for registration
from flask import request, url_for, redirect
from forms import RegistrationForm, LoginForm

@app.route('/register', methods = ['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html',form=form)

from flask_login import login_user, current_user

@app.route('/login', methods = ['GET','POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('home'))
        flash('Invalid email address or Password.')
    return render_template('login.html', form = form)

