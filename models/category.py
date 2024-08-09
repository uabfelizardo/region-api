from datetime import datetime
from . import db  # Importa db do __init__.py

class Category(db.Model):
    __tablename__ = 'category'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    createAt = db.Column(db.DateTime, default=datetime.utcnow)
    updateAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Category {self.name}>'
