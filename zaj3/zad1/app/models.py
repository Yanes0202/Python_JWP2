from app import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    subject = db.Column(db.String, unique=False, nullable=False)
    time = db.Column(db.String)
