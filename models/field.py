from datetime import datetime
from . import db  # Importa db do __init__.py

class Field(db.Model):
    __tablename__ = 'field'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fieldName = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(255))
    description = db.Column(db.Text)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    # Relacionamento com Country
    countries = db.relationship('Country', backref='field', lazy=True)
    districts = db.relationship('District', back_populates='field')
    
    # Adicione esta linha no final da classe Field
    elders_deacons = db.relationship('EldersDeacons', back_populates='field')

    # Adicione esta linha no final da classe Field
    locals = db.relationship('Local', back_populates='field')
        
    # Adicione esta linha no final da classe Field
    missionaries = db.relationship('Missionary', back_populates='field')

    # Define o relacionamento com Schools
    schools = db.relationship('Schools', back_populates='field')

    def __repr__(self):
        return f'<Field {self.fieldName}>'
