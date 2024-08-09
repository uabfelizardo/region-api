from . import db  # Importa db do __init__.py
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Schools(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school_name = db.Column(db.String(100), nullable=False)
    vice_chancellor = db.Column(db.String(100))
    degrees_offered = db.Column(db.String(255))
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # Define relacionamentos
    field = relationship('Field', back_populates='schools')
    location = relationship('Location', back_populates='schools')

    def __repr__(self):
        return f'<Schools {self.school_name}>'
