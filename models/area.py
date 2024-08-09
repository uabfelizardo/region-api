from datetime import datetime
from . import db  # Importa db do __init__.py

class Area(db.Model):
    __tablename__ = 'area'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    areaName = db.Column(db.String(100), nullable=False, unique=True)
    createAt = db.Column(db.DateTime, default=db.func.now())
    updateAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Area {self.areaName}>'
