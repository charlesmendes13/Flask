from app.config import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    book = db.relationship('Book', backref='author', lazy='dynamic')
    
    def __init__(self, name):
        self.name = name