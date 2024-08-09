from datetime import datetime
from . import db  # Importa db do __init__.py

class MissionariesAdicionalInformation(db.Model):
    __tablename__ = 'missionaries_adicional_information'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    Deployment = db.Column(db.String(100), nullable=False)
    AdmissionDate = db.Column(db.Date, nullable=False)
    YearsOfService = db.Column(db.Integer, nullable=False)
    LicenseDays = db.Column(db.Integer, nullable=False)
    DaysOnBalance = db.Column(db.Integer, nullable=False)
    Notes = db.Column(db.Text, nullable=True)
    VacationType = db.Column(db.String(100), nullable=True)
    DaysOff = db.Column(db.Integer, nullable=True)
    missionary_id = db.Column(db.Integer, db.ForeignKey('missionary.id'), nullable=False)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    missionary = db.relationship('Missionary', back_populates='adicional_info')

    def __repr__(self):
        return f'<MissionariesAdicionalInformation {self.id}>'
