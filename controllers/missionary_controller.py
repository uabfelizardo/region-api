from flask import Blueprint, jsonify, request  # type: ignore
from models.missionary import Missionary  # Importa o modelo Missionary
from models import db  # Importa db do __init__.py em models

missionary_bp = Blueprint('missionary', __name__)

@missionary_bp.route('/missionaries', methods=['GET'])
def get_missionaries():
    missionaries = Missionary.query.all()
    return jsonify([{
        'id': missionary.id,
        'firstName': missionary.firstName,
        'lastName': missionary.lastName,
        'BirthDate': missionary.BirthDate.strftime('%Y-%m-%d'),
        'CountryOfService': missionary.CountryOfService,
        'NumOfChildren': missionary.NumOfChildren,
        'picture': missionary.picture.decode('utf-8') if missionary.picture else None,
        'Deployment': missionary.Deployment,
        'Region': missionary.Region,
        'Employee': missionary.Employee,
        'Notes': missionary.Notes,
        'fieldID': missionary.fieldID,
        'createAt': missionary.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': missionary.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for missionary in missionaries])

@missionary_bp.route('/missionary/<int:id>', methods=['GET'])
def get_missionary(id):
    missionary = Missionary.query.get(id)
    if missionary:
        return jsonify({
            'id': missionary.id,
            'firstName': missionary.firstName,
            'lastName': missionary.lastName,
            'BirthDate': missionary.BirthDate.strftime('%Y-%m-%d'),
            'CountryOfService': missionary.CountryOfService,
            'NumOfChildren': missionary.NumOfChildren,
            'picture': missionary.picture.decode('utf-8') if missionary.picture else None,
            'Deployment': missionary.Deployment,
            'Region': missionary.Region,
            'Employee': missionary.Employee,
            'Notes': missionary.Notes,
            'fieldID': missionary.fieldID,
            'createAt': missionary.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': missionary.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Missionary not found'}), 404

@missionary_bp.route('/missionary', methods=['POST'])
def add_missionary():
    data = request.get_json()
    required_fields = ['firstName', 'lastName', 'BirthDate', 'CountryOfService', 'Deployment', 'Region', 'Employee', 'fieldID']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'{field} is required'}), 400

    new_missionary = Missionary(
        firstName=data['firstName'],
        lastName=data['lastName'],
        BirthDate=data['BirthDate'],
        CountryOfService=data['CountryOfService'],
        NumOfChildren=data.get('NumOfChildren'),
        picture=data.get('picture').encode('utf-8') if data.get('picture') else None,
        Deployment=data['Deployment'],
        Region=data['Region'],
        Employee=data['Employee'],
        Notes=data.get('Notes'),
        fieldID=data['fieldID']
    )
    db.session.add(new_missionary)
    db.session.commit()
    return jsonify({
        'message': 'New missionary added!',
        'id': new_missionary.id,
        'createAt': new_missionary.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_missionary.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@missionary_bp.route('/missionary/<int:id>', methods=['PUT'])
def update_missionary(id):
    data = request.get_json()
    missionary = Missionary.query.get(id)
    if not missionary:
        return jsonify({'message': 'Missionary not found'}), 404

    if 'firstName' in data:
        missionary.firstName = data['firstName']
    if 'lastName' in data:
        missionary.lastName = data['lastName']
    if 'BirthDate' in data:
        missionary.BirthDate = data['BirthDate']
    if 'CountryOfService' in data:
        missionary.CountryOfService = data['CountryOfService']
    if 'NumOfChildren' in data:
        missionary.NumOfChildren = data['NumOfChildren']
    if 'picture' in data:
        missionary.picture = data['picture'].encode('utf-8') if data['picture'] else None
    if 'Deployment' in data:
        missionary.Deployment = data['Deployment']
    if 'Region' in data:
        missionary.Region = data['Region']
    if 'Employee' in data:
        missionary.Employee = data['Employee']
    if 'Notes' in data:
        missionary.Notes = data['Notes']
    if 'fieldID' in data:
        missionary.fieldID = data['fieldID']

    db.session.commit()
    return jsonify({
        'message': 'Missionary updated successfully',
        'createAt': missionary.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': missionary.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@missionary_bp.route('/missionary/<int:id>', methods=['DELETE'])
def delete_missionary(id):
    missionary = Missionary.query.get(id)
    if missionary:
        db.session.delete(missionary)
        db.session.commit()
        return jsonify({'message': 'Missionary deleted successfully'})
    else:
        return jsonify({'message': 'Missionary not found'}), 404
