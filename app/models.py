from datetime import datetime

from flask_login import UserMixin

from app import app, db, login

class Admin(UserMixin):
    id = 1

@login.user_loader
def load_user(id):
    return Admin()
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    image_path = db.Column(db.String(64))
    text_path = db.Column(db.String(64))