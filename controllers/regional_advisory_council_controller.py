from flask import Blueprint, jsonify, request  # type: ignore
from models.regional_advisory_council import RegionalAdvisoryCouncil  # Importa o modelo RegionalAdvisoryCouncil
from models.region import Region  # Importa o modelo Region
from models import db  # Importa db do __init__.py em models

regional_advisory_council_bp = Blueprint('regional_advisory_council', __name__)

@regional_advisory_council_bp.route('/regional_advisory_councils', methods=['GET'])
def get_regional_advisory_councils():
    councils = RegionalAdvisoryCouncil.query.all()
    return jsonify([{
        'id': council.id,
        'name': council.name,
        'role': council.role,
        'contact': council.contact,
        'email': council.email,
        'location': council.location,
        'region_id': council.region_id,
        'createAt': council.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': council.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for council in councils])

@regional_advisory_council_bp.route('/regional_advisory_council/<int:id>', methods=['GET'])
def get_regional_advisory_council(id):
    council = RegionalAdvisoryCouncil.query.get(id)
    if council:
        return jsonify({
            'id': council.id,
            'name': council.name,
            'role': council.role,
            'contact': council.contact,
            'email': council.email,
            'location': council.location,
            'region_id': council.region_id,
            'createAt': council.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': council.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Regional Advisory Council not found'}), 404

@regional_advisory_council_bp.route('/regional_advisory_council', methods=['POST'])
def add_regional_advisory_council():
    data = request.get_json()
    if 'name' not in data or 'role' not in data or 'region_id' not in data:
        return jsonify({'message': 'name, role, and region_id are required'}), 400
    
    region = Region.query.get(data['region_id'])
    if not region:
        return jsonify({'message': 'Region not found'}), 404

    new_council = RegionalAdvisoryCouncil(
        name=data['name'],
        role=data['role'],
        contact=data.get('contact'),
        email=data.get('email'),
        location=data.get('location'),
        region_id=data['region_id']
    )
    db.session.add(new_council)
    db.session.commit()
    return jsonify({
        'message': 'New regional advisory council added!',
        'id': new_council.id,
        'createAt': new_council.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_council.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@regional_advisory_council_bp.route('/regional_advisory_council/<int:id>', methods=['PUT'])
def update_regional_advisory_council(id):
    data = request.get_json()
    council = RegionalAdvisoryCouncil.query.get(id)
    if not council:
        return jsonify({'message': 'Regional Advisory Council not found'}), 404

    if 'name' in data:
        council.name = data['name']
    if 'role' in data:
        council.role = data['role']
    if 'contact' in data:
        council.contact = data['contact']
    if 'email' in data:
        council.email = data['email']
    if 'location' in data:
        council.location = data['location']
    if 'region_id' in data:
        if Region.query.get(data['region_id']):
            council.region_id = data['region_id']
        else:
            return jsonify({'message': 'Region not found'}), 404

    db.session.commit()
    return jsonify({
        'message': 'Regional Advisory Council updated successfully',
        'createAt': council.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': council.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@regional_advisory_council_bp.route('/regional_advisory_council/<int:id>', methods=['DELETE'])
def delete_regional_advisory_council(id):
    council = RegionalAdvisoryCouncil.query.get(id)
    if council:
        db.session.delete(council)
        db.session.commit()
        return jsonify({'message': 'Regional Advisory Council deleted successfully'})
    else:
        return jsonify({'message': 'Regional Advisory Council not found'}), 404
