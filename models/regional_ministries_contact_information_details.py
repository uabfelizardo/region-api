from . import db  # Importa db do __init__.py

class RegionalMinistriesContactInformationDetails(db.Model):
    __tablename__ = 'regional_ministries_contact_information_details'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100))
    email = db.Column(db.String(100))
    location = db.Column(db.String(100))
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    
    # Relationships
    region = db.relationship('Region', backref=db.backref('contact_information_details', lazy=True))
    
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<RegionalMinistriesContactInformationDetails {self.name}>'
