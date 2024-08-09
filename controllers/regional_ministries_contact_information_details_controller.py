from flask import Blueprint, jsonify, request  # type: ignore
from models.regional_ministries_contact_information_details import RegionalMinistriesContactInformationDetails  # Importa o modelo RegionalMinistriesContactInformationDetails
from models.region import Region  # Importa o modelo Region
from models import db  # Importa db do __init__.py em models

regional_ministries_contact_information_details_bp = Blueprint('regional_ministries_contact_information_details', __name__)

@regional_ministries_contact_information_details_bp.route('/regional_ministries_contact_details', methods=['GET'])
def get_regional_ministries_contact_details():
    details = RegionalMinistriesContactInformationDetails.query.all()
    return jsonify([{
        'id': detail.id,
        'name': detail.name,
        'role': detail.role,
        'contact': detail.contact,
        'email': detail.email,
        'location': detail.location,
        'region_id': detail.region_id,
        'createAt': detail.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': detail.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for detail in details])

@regional_ministries_contact_information_details_bp.route('/regional_ministries_contact_detail/<int:id>', methods=['GET'])
def get_regional_ministries_contact_detail(id):
    detail = RegionalMinistriesContactInformationDetails.query.get(id)
    if detail:
        return jsonify({
            'id': detail.id,
            'name': detail.name,
            'role': detail.role,
            'contact': detail.contact,
            'email': detail.email,
            'location': detail.location,
            'region_id': detail.region_id,
            'createAt': detail.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': detail.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Regional Ministries Contact Information Details not found'}), 404

@regional_ministries_contact_information_details_bp.route('/regional_ministries_contact_detail', methods=['POST'])
def add_regional_ministries_contact_detail():
    data = request.get_json()
    if 'name' not in data or 'role' not in data or 'region_id' not in data:
        return jsonify({'message': 'name, role, and region_id are required'}), 400
    
    region = Region.query.get(data['region_id'])
    if not region:
        return jsonify({'message': 'Region not found'}), 404

    new_detail = RegionalMinistriesContactInformationDetails(
        name=data['name'],
        role=data['role'],
        contact=data.get('contact'),
        email=data.get('email'),
        location=data.get('location'),
        region_id=data['region_id']
    )
    db.session.add(new_detail)
    db.session.commit()
    return jsonify({
        'message': 'New regional ministries contact information details added!',
        'id': new_detail.id,
        'createAt': new_detail.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_detail.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@regional_ministries_contact_information_details_bp.route('/regional_ministries_contact_detail/<int:id>', methods=['PUT'])
def update_regional_ministries_contact_detail(id):
    data = request.get_json()
    detail = RegionalMinistriesContactInformationDetails.query.get(id)
    if not detail:
        return jsonify({'message': 'Regional Ministries Contact Information Details not found'}), 404

    if 'name' in data:
        detail.name = data['name']
    if 'role' in data:
        detail.role = data['role']
    if 'contact' in data:
        detail.contact = data['contact']
    if 'email' in data:
        detail.email = data['email']
    if 'location' in data:
        detail.location = data['location']
    if 'region_id' in data:
        if Region.query.get(data['region_id']):
            detail.region_id = data['region_id']
        else:
            return jsonify({'message': 'Region not found'}), 404

    db.session.commit()
    return jsonify({
        'message': 'Regional Ministries Contact Information Details updated successfully',
        'createAt': detail.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': detail.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@regional_ministries_contact_information_details_bp.route('/regional_ministries_contact_detail/<int:id>', methods=['DELETE'])
def delete_regional_ministries_contact_detail(id):
    detail = RegionalMinistriesContactInformationDetails.query.get(id)
    if detail:
        db.session.delete(detail)
        db.session.commit()
        return jsonify({'message': 'Regional Ministries Contact Information Details deleted successfully'})
    else:
        return jsonify({'message': 'Regional Ministries Contact Information Details not found'}), 404
