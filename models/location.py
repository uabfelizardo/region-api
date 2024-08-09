from datetime import datetime
from . import db  # Importa db do __init__.py

class Location(db.Model):
    __tablename__ = 'location'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Define o relacionamento com Schools
    schools = db.relationship('Schools', back_populates='location')

    def __repr__(self):
        return f'<Location {self.name}>'
