from datetime import datetime
from . import db  # Importa db do __init__.py

class District(db.Model):
    __tablename__ = 'district'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DistrictNumber = db.Column(db.String(50), nullable=False)
    DistrictName = db.Column(db.String(100), nullable=False)
    Phase = db.Column(db.String(50), nullable=False)
    Year_est = db.Column(db.String(4), nullable=False)
    DSname = db.Column(db.String(100), nullable=False)
    DateElected = db.Column(db.DateTime, nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Contact = db.Column(db.String(20), nullable=False)
    Language = db.Column(db.String(50), nullable=False)
    Membership = db.Column(db.Integer, nullable=False)
    Churches = db.Column(db.Integer, nullable=False)
    Organised = db.Column(db.Integer, nullable=False)
    NonOrg = db.Column(db.Integer, nullable=False)
    Elders = db.Column(db.Integer, nullable=False)
    Deacons = db.Column(db.Integer, nullable=False)
    LicensedMin = db.Column(db.Integer, nullable=False)
    CountryPopulation = db.Column(db.Integer, nullable=False)
    LocalCurrency = db.Column(db.String(50), nullable=False)
    LocalLanguage = db.Column(db.String(50), nullable=False)
    fieldID = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    countryID = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    personID = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    field = db.relationship('Field', back_populates='districts')
    country = db.relationship('Country', back_populates='districts')
    person = db.relationship('Person', back_populates='districts')
    # Adicione esta linha no final da classe District
    advisory_board_lays = db.relationship('DistrictAdvisoryBoardLay', back_populates='district')
    # Adicione esta linha no final da classe District
    advisory_board_ministerials = db.relationship('DistrictAdvisoryBoardMinisterial', back_populates='district')

    # Adicione esta linha no final da classe District
    elders_deacons = db.relationship('EldersDeacons', back_populates='district')

    # Adicione esta linha no final da classe District
    locals = db.relationship('Local', back_populates='district')


    def __repr__(self):
        return f'<District {self.DistrictName}>'
