from . import db  # Importa db do __init__.py

class RegionalAdvisoryCouncilMemberAtLarge(db.Model):
    __tablename__ = 'regional_advisory_council_member_at_large'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100))
    email = db.Column(db.String(100))
    location = db.Column(db.String(100))
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    
    # Relationships
    region = db.relationship('Region', backref=db.backref('regional_advisory_council_members_at_large', lazy=True))
    
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<RegionalAdvisoryCouncilMemberAtLarge {self.name}>'
