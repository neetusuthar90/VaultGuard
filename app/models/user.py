from flask_login import UserMixin
from datetime import datetime
from app.models.item import Item
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin, db.Model):
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(50), index=True, unique=True)
      email = db.Column(db.String(150), unique = True, index = True)
      password_hash = db.Column(db.String(150))
      joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

      def __init__(self,username,email,password):
            self.username = username
            self.email = email
            self.set_password(password)
      
      def set_password(self, password):
            self.password_hash = generate_password_hash(password)

      def check_password(self,password):
            return check_password_hash(self.password_hash,password)
      
      items = db.relationship('Item', backref='user', lazy=True)
