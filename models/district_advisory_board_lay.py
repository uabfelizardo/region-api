from datetime import datetime
from . import db  # Importa db do __init__.py

class DistrictAdvisoryBoardLay(db.Model):
    __tablename__ = 'district_advisory_board_lay'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    personName = db.Column(db.String(100), nullable=False)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    district = db.relationship('District', back_populates='advisory_board_lays')

    def __repr__(self):
        return f'<DistrictAdvisoryBoardLay {self.personName}>'
