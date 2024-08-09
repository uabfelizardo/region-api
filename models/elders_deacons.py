from datetime import datetime
from . import db  # Importa db do __init__.py

class EldersDeacons(db.Model):
    __tablename__ = 'elders_deacons'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OwningDistrict = db.Column(db.String(100), nullable=False)
    Surname = db.Column(db.String(100), nullable=False)
    GivenName = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    ChurchName = db.Column(db.String(100), nullable=False)
    DatePastorateBegan = db.Column(db.Date, nullable=False)
    IssuingDistrict = db.Column(db.String(100), nullable=False)
    Credential = db.Column(db.String(100), nullable=False)
    IssueDate = db.Column(db.Date, nullable=False)
    Status = db.Column(db.String(50), nullable=False)
    Notes = db.Column(db.Text, nullable=True)
    picture = db.Column(db.LargeBinary, nullable=True)
    personID = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    fieldID = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    districtID = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    person = db.relationship('Person', back_populates='elders_deacons')
    field = db.relationship('Field', back_populates='elders_deacons')
    district = db.relationship('District', back_populates='elders_deacons')

    def __repr__(self):
        return f'<EldersDeacons {self.Surname}, {self.GivenName}>'
