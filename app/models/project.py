from app.extensions import db
from datetime import datetime
class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    image_file = db.Column(db.String(255), nullable=False, default='default.jpg')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.slug}', '{self.description}', '{self.image_file}')"