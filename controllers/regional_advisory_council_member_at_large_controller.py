from flask import Blueprint, jsonify, request  # type: ignore
from models.regional_advisory_council_member_at_large import RegionalAdvisoryCouncilMemberAtLarge  # Importa o modelo RegionalAdvisoryCouncilMemberAtLarge
from models.region import Region  # Importa o modelo Region
from models import db  # Importa db do __init__.py em models

regional_advisory_council_member_at_large_bp = Blueprint('regional_advisory_council_member_at_large', __name__)

@regional_advisory_council_member_at_large_bp.route('/regional_advisory_council_members_at_large', methods=['GET'])
def get_regional_advisory_council_members_at_large():
    members = RegionalAdvisoryCouncilMemberAtLarge.query.all()
    return jsonify([{
        'id': member.id,
        'name': member.name,
        'role': member.role,
        'contact': member.contact,
        'email': member.email,
        'location': member.location,
        'region_id': member.region_id,
        'createAt': member.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': member.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for member in members])

@regional_advisory_council_member_at_large_bp.route('/regional_advisory_council_member_at_large/<int:id>', methods=['GET'])
def get_regional_advisory_council_member_at_large(id):
    member = RegionalAdvisoryCouncilMemberAtLarge.query.get(id)
    if member:
        return jsonify({
            'id': member.id,
            'name': member.name,
            'role': member.role,
            'contact': member.contact,
            'email': member.email,
            'location': member.location,
            'region_id': member.region_id,
            'createAt': member.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': member.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Regional Advisory Council Member at Large not found'}), 404

@regional_advisory_council_member_at_large_bp.route('/regional_advisory_council_member_at_large', methods=['POST'])
def add_regional_advisory_council_member_at_large():
    data = request.get_json()
    if 'name' not in data or 'role' not in data or 'region_id' not in data:
        return jsonify({'message': 'name, role, and region_id are required'}), 400
    
    region = Region.query.get(data['region_id'])
    if not region:
        return jsonify({'message': 'Region not found'}), 404

    new_member = RegionalAdvisoryCouncilMemberAtLarge(
        name=data['name'],
        role=data['role'],
        contact=data.get('contact'),
        email=data.get('email'),
        location=data.get('location'),
        region_id=data['region_id']
    )
    db.session.add(new_member)
    db.session.commit()
    return jsonify({
        'message': 'New regional advisory council member at large added!',
        'id': new_member.id,
        'createAt': new_member.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_member.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@regional_advisory_council_member_at_large_bp.route('/regional_advisory_council_member_at_large/<int:id>', methods=['PUT'])
def update_regional_advisory_council_member_at_large(id):
    data = request.get_json()
    member = RegionalAdvisoryCouncilMemberAtLarge.query.get(id)
    if not member:
        return jsonify({'message': 'Regional Advisory Council Member at Large not found'}), 404

    if 'name' in data:
        member.name = data['name']
    if 'role' in data:
        member.role = data['role']
    if 'contact' in data:
        member.contact = data['contact']
    if 'email' in data:
        member.email = data['email']
    if 'location' in data:
        member.location = data['location']
    if 'region_id' in data:
        if Region.query.get(data['region_id']):
            member.region_id = data['region_id']
        else:
            return jsonify({'message': 'Region not found'}), 404

    db.session.commit()
    return jsonify({
        'message': 'Regional Advisory Council Member at Large updated successfully',
        'createAt': member.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': member.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@regional_advisory_council_member_at_large_bp.route('/regional_advisory_council_member_at_large/<int:id>', methods=['DELETE'])
def delete_regional_advisory_council_member_at_large(id):
    member = RegionalAdvisoryCouncilMemberAtLarge.query.get(id)
    if member:
        db.session.delete(member)
        db.session.commit()
        return jsonify({'message': 'Regional Advisory Council Member at Large deleted successfully'})
    else:
        return jsonify({'message': 'Regional Advisory Council Member at Large not found'}), 404
