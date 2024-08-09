from . import db  # Importa db do __init__.py

class Local(db.Model):
    __tablename__ = 'local'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NumDistrict = db.Column(db.Integer, nullable=False)
    NumChurch = db.Column(db.Integer, nullable=False)
    Field = db.Column(db.String(100), nullable=False)
    DistrictName = db.Column(db.String(100), nullable=False)
    Church = db.Column(db.String(100), nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    Active = db.Column(db.Boolean, nullable=False)
    fieldID = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    districtID = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    field = db.relationship('Field', back_populates='locals')
    district = db.relationship('District', back_populates='locals')

    def __repr__(self):
        return f'<Local {self.DistrictName}, {self.Church}>'
