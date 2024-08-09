from flask import Blueprint, jsonify, request  # type: ignore
from models.elders_deacons import EldersDeacons  # Importa o modelo EldersDeacons
from models import db  # Importa db do __init__.py em models
from datetime import datetime

elders_deacons_bp = Blueprint('elders_deacons', __name__)

@elders_deacons_bp.route('/elders_deacons', methods=['GET'])
def get_elders_deacons():
    elders_deacons_list = EldersDeacons.query.all()
    return jsonify([{
        'id': elders_deacon.id,
        'OwningDistrict': elders_deacon.OwningDistrict,
        'Surname': elders_deacon.Surname,
        'GivenName': elders_deacon.GivenName,
        'gender': elders_deacon.gender,
        'ChurchName': elders_deacon.ChurchName,
        'DatePastorateBegan': elders_deacon.DatePastorateBegan.strftime('%Y-%m-%d'),
        'IssuingDistrict': elders_deacon.IssuingDistrict,
        'Credential': elders_deacon.Credential,
        'IssueDate': elders_deacon.IssueDate.strftime('%Y-%m-%d'),
        'Status': elders_deacon.Status,
        'Notes': elders_deacon.Notes,
        'picture': elders_deacon.picture,
        'personID': elders_deacon.personID,
        'fieldID': elders_deacon.fieldID,
        'districtID': elders_deacon.districtID,
        'createAt': elders_deacon.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': elders_deacon.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for elders_deacon in elders_deacons_list])

@elders_deacons_bp.route('/elders_deacons/<int:id>', methods=['GET'])
def get_elders_deacon(id):
    elders_deacon = EldersDeacons.query.get(id)
    if elders_deacon:
        return jsonify({
            'id': elders_deacon.id,
            'OwningDistrict': elders_deacon.OwningDistrict,
            'Surname': elders_deacon.Surname,
            'GivenName': elders_deacon.GivenName,
            'gender': elders_deacon.gender,
            'ChurchName': elders_deacon.ChurchName,
            'DatePastorateBegan': elders_deacon.DatePastorateBegan.strftime('%Y-%m-%d'),
            'IssuingDistrict': elders_deacon.IssuingDistrict,
            'Credential': elders_deacon.Credential,
            'IssueDate': elders_deacon.IssueDate.strftime('%Y-%m-%d'),
            'Status': elders_deacon.Status,
            'Notes': elders_deacon.Notes,
            'picture': elders_deacon.picture,
            'personID': elders_deacon.personID,
            'fieldID': elders_deacon.fieldID,
            'districtID': elders_deacon.districtID,
            'createAt': elders_deacon.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': elders_deacon.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'EldersDeacon not found'}), 404

@elders_deacons_bp.route('/elders_deacons', methods=['POST'])
def add_elders_deacon():
    data = request.get_json()
    required_fields = ['OwningDistrict', 'Surname', 'GivenName', 'gender', 'ChurchName', 'DatePastorateBegan', 'IssuingDistrict', 'Credential', 'IssueDate', 'Status', 'personID', 'fieldID', 'districtID']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'{field} is required'}), 400

    new_elders_deacon = EldersDeacons(
        OwningDistrict=data['OwningDistrict'],
        Surname=data['Surname'],
        GivenName=data['GivenName'],
        gender=data['gender'],
        ChurchName=data['ChurchName'],
        DatePastorateBegan=datetime.strptime(data['DatePastorateBegan'], '%Y-%m-%d'),
        IssuingDistrict=data['IssuingDistrict'],
        Credential=data['Credential'],
        IssueDate=datetime.strptime(data['IssueDate'], '%Y-%m-%d'),
        Status=data['Status'],
        Notes=data.get('Notes'),
        picture=data.get('picture'),
        personID=data['personID'],
        fieldID=data['fieldID'],
        districtID=data['districtID']
    )
    db.session.add(new_elders_deacon)
    db.session.commit()
    return jsonify({
        'message': 'New EldersDeacon added!',
        'id': new_elders_deacon.id,
        'createAt': new_elders_deacon.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_elders_deacon.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@elders_deacons_bp.route('/elders_deacons/<int:id>', methods=['PUT'])
def update_elders_deacon(id):
    data = request.get_json()
    elders_deacon = EldersDeacons.query.get(id)
    if not elders_deacon:
        return jsonify({'message': 'EldersDeacon not found'}), 404

    if 'OwningDistrict' in data:
        elders_deacon.OwningDistrict = data['OwningDistrict']
    if 'Surname' in data:
        elders_deacon.Surname = data['Surname']
    if 'GivenName' in data:
        elders_deacon.GivenName = data['GivenName']
    if 'gender' in data:
        elders_deacon.gender = data['gender']
    if 'ChurchName' in data:
        elders_deacon.ChurchName = data['ChurchName']
    if 'DatePastorateBegan' in data:
        elders_deacon.DatePastorateBegan = datetime.strptime(data['DatePastorateBegan'], '%Y-%m-%d')
    if 'IssuingDistrict' in data:
        elders_deacon.IssuingDistrict = data['IssuingDistrict']
    if 'Credential' in data:
        elders_deacon.Credential = data['Credential']
    if 'IssueDate' in data:
        elders_deacon.IssueDate = datetime.strptime(data['IssueDate'], '%Y-%m-%d')
    if 'Status' in data:
        elders_deacon.Status = data['Status']
    if 'Notes' in data:
        elders_deacon.Notes = data['Notes']
    if 'picture' in data:
        elders_deacon.picture = data['picture']
    if 'personID' in data:
        elders_deacon.personID = data['personID']
    if 'fieldID' in data:
        elders_deacon.fieldID = data['fieldID']
    if 'districtID' in data:
        elders_deacon.districtID = data['districtID']

    db.session.commit()
    return jsonify({
        'message': 'EldersDeacon updated successfully',
        'createAt': elders_deacon.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': elders_deacon.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@elders_deacons_bp.route('/elders_deacons/<int:id>', methods=['DELETE'])
def delete_elders_deacon(id):
    elders_deacon = EldersDeacons.query.get(id)
    if elders_deacon:
        db.session.delete(elders_deacon)
        db.session.commit()
        return jsonify({'message': 'EldersDeacon deleted successfully'})
    else:
        return jsonify({'message': 'EldersDeacon not found'}), 404
