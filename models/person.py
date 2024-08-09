from datetime import datetime
from . import db  # Importa db do __init__.py
from sqlalchemy.sql import func

class Person(db.Model):
    __tablename__ = 'person'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname = db.Column(db.String(100), nullable=False)
    givenname = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)  # Pode ser 'Male', 'Female', etc.
    dateofbirth = db.Column(db.Date, nullable=False)
    pastoralstartdate = db.Column(db.Date)
    dsstartdate = db.Column(db.Date)
    citizenship = db.Column(db.String(100))
    spouse = db.Column(db.String(100))
    children = db.Column(db.String(100))  # Se for uma lista de filhos, considere usar um relacionamento ou JSON
    education = db.Column(db.String(255))
    dateelected = db.Column(db.Date)
    picture = db.Column(db.String(255))  # Caminho para o arquivo de imagem ou URL
    
    createAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updateAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Adicione esta linha no final da classe Person
    districts = db.relationship('District', back_populates='person')
    # Adicione esta linha no final da classe Person
    elders_deacons = db.relationship('EldersDeacons', back_populates='person')

    def __repr__(self):
        return f'<Person {self.givenname} {self.surname}>'
