from datetime import datetime
from . import db  # Importa db do __init__.py

class Country(db.Model):
    __tablename__ = 'country'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Country = db.Column(db.String(100), nullable=False)
    Map = db.Column(db.String(255))  # URL ou caminho para o mapa
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Adicione esta linha no final da classe Country
    districts = db.relationship('District', back_populates='country')

    def __repr__(self):
        return f'<Country {self.Country}>'
