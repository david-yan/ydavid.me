from datetime import datetime

from app import app, db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    image_path = db.Column(db.String(64))
    text_path = db.Column(db.String(64))