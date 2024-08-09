from flask import Blueprint, jsonify, request  # type: ignore
from models.local import Local  # Importa o modelo Local
from models import db  # Importa db do __init__.py em models

local_bp = Blueprint('local', __name__)

@local_bp.route('/local', methods=['GET'])
def get_locals():
    locals_list = Local.query.all()
    return jsonify([{
        'id': local.id,
        'NumDistrict': local.NumDistrict,
        'NumChurch': local.NumChurch,
        'Field': local.Field,
        'DistrictName': local.DistrictName,
        'Church': local.Church,
        'Type': local.Type,
        'Active': local.Active,
        'fieldID': local.fieldID,
        'districtID': local.districtID,
        'createAt': local.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': local.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for local in locals_list])

@local_bp.route('/local/<int:id>', methods=['GET'])
def get_local(id):
    local = Local.query.get(id)
    if local:
        return jsonify({
            'id': local.id,
            'NumDistrict': local.NumDistrict,
            'NumChurch': local.NumChurch,
            'Field': local.Field,
            'DistrictName': local.DistrictName,
            'Church': local.Church,
            'Type': local.Type,
            'Active': local.Active,
            'fieldID': local.fieldID,
            'districtID': local.districtID,
            'createAt': local.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': local.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Local not found'}), 404

@local_bp.route('/local', methods=['POST'])
def add_local():
    data = request.get_json()
    required_fields = ['NumDistrict', 'NumChurch', 'Field', 'DistrictName', 'Church', 'Type', 'Active', 'fieldID', 'districtID']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'{field} is required'}), 400

    new_local = Local(
        NumDistrict=data['NumDistrict'],
        NumChurch=data['NumChurch'],
        Field=data['Field'],
        DistrictName=data['DistrictName'],
        Church=data['Church'],
        Type=data['Type'],
        Active=data['Active'],
        fieldID=data['fieldID'],
        districtID=data['districtID']
    )
    db.session.add(new_local)
    db.session.commit()
    return jsonify({
        'message': 'New Local added!',
        'id': new_local.id,
        'createAt': new_local.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_local.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@local_bp.route('/local/<int:id>', methods=['PUT'])
def update_local(id):
    data = request.get_json()
    local = Local.query.get(id)
    if not local:
        return jsonify({'message': 'Local not found'}), 404

    if 'NumDistrict' in data:
        local.NumDistrict = data['NumDistrict']
    if 'NumChurch' in data:
        local.NumChurch = data['NumChurch']
    if 'Field' in data:
        local.Field = data['Field']
    if 'DistrictName' in data:
        local.DistrictName = data['DistrictName']
    if 'Church' in data:
        local.Church = data['Church']
    if 'Type' in data:
        local.Type = data['Type']
    if 'Active' in data:
        local.Active = data['Active']
    if 'fieldID' in data:
        local.fieldID = data['fieldID']
    if 'districtID' in data:
        local.districtID = data['districtID']

    db.session.commit()
    return jsonify({
        'message': 'Local updated successfully',
        'createAt': local.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': local.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@local_bp.route('/local/<int:id>', methods=['DELETE'])
def delete_local(id):
    local = Local.query.get(id)
    if local:
        db.session.delete(local)
        db.session.commit()
        return jsonify({'message': 'Local deleted successfully'})
    else:
        return jsonify({'message': 'Local not found'}), 404
