from . import db  # Importa db do __init__.py

class MissionaryHomeAssignmentDetails(db.Model):
    __tablename__ = 'missionary_home_assignment_details'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    home_assignment_date = db.Column(db.Date, nullable=False)
    StartDate = db.Column(db.Date, nullable=False)
    EndDate = db.Column(db.Date, nullable=False)
    Place = db.Column(db.String(200), nullable=False)
    Notes = db.Column(db.Text, nullable=True)
    missionary_id = db.Column(db.Integer, db.ForeignKey('missionary.id'), nullable=False)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    missionary = db.relationship('Missionary', back_populates='home_assignments')

    def __repr__(self):
        return f'<MissionaryHomeAssignmentDetails {self.id}>'
