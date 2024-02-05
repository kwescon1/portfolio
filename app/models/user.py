
from app.extensions import db
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(255), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    projects = db.relationship('Project', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.email}')"

