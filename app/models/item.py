from app import db
# from app.models.user import User

class Item(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    website_name = db.Column(db.String(100),nullable = False)
    username = db.Column(db.String(100),nullable = False)
    password = db.Column(db.String(150),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
