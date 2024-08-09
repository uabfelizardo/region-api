from . import db  # Importa db do __init__.py

class RegionAndFieldContactInformation(db.Model):
    __tablename__ = 'region_and_field_contact_information'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100))
    email = db.Column(db.String(100))
    location = db.Column(db.String(100))
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    
    # Relationships
    region = db.relationship('Region', backref=db.backref('field_contact_information', lazy=True))
    
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<RegionAndFieldContactInformation {self.name}>'
