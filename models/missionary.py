from . import db  # Importa db do __init__.py

class Missionary(db.Model):
    __tablename__ = 'missionary'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    BirthDate = db.Column(db.Date, nullable=False)
    CountryOfService = db.Column(db.String(100), nullable=False)
    NumOfChildren = db.Column(db.Integer, nullable=True)
    picture = db.Column(db.LargeBinary, nullable=True)
    Deployment = db.Column(db.String(100), nullable=False)
    Region = db.Column(db.String(100), nullable=False)
    Employee = db.Column(db.Boolean, nullable=False)
    Notes = db.Column(db.Text, nullable=True)
    fieldID = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updateAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    field = db.relationship('Field', back_populates='missionaries')

    # Adicione esta linha no final da classe Missionary
    adicional_info = db.relationship('MissionariesAdicionalInformation', back_populates='missionary')

    # Adicione esta linha no final da classe Missionary
    home_assignments = db.relationship('MissionaryHomeAssignmentDetails', back_populates='missionary')

    def __repr__(self):
        return f'<Missionary {self.firstName} {self.lastName}>'
