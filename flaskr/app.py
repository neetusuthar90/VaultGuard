from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySql initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Secret key generation
secret_key = os.random(32)
app.config['secret_key'] = secret_key

login_manger = LoginManager()
login_manger.init_app(app)

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
