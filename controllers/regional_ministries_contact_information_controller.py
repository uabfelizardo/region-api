from flask import Blueprint, jsonify, request  # type: ignore
from models.regional_ministries_contact_information import RegionalMinistriesContactInformation  # Importa o modelo RegionalMinistriesContactInformation
from models.region import Region  # Importa o modelo Region
from models import db  # Importa db do __init__.py em models

regional_ministries_contact_information_bp = Blueprint('regional_ministries_contact_information', __name__)

@regional_ministries_contact_information_bp.route('/regional_ministries_contacts', methods=['GET'])
def get_regional_ministries_contacts():
    contacts = RegionalMinistriesContactInformation.query.all()
    return jsonify([{
        'id': contact.id,
        'name': contact.name,
        'role': contact.role,
        'contact': contact.contact,
        'email': contact.email,
        'location': contact.location,
        'region_id': contact.region_id,
        'createAt': contact.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': contact.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for contact in contacts])

@regional_ministries_contact_information_bp.route('/regional_ministries_contact/<int:id>', methods=['GET'])
def get_regional_ministries_contact(id):
    contact = RegionalMinistriesContactInformation.query.get(id)
    if contact:
        return jsonify({
            'id': contact.id,
            'name': contact.name,
            'role': contact.role,
            'contact': contact.contact,
            'email': contact.email,
            'location': contact.location,
            'region_id': contact.region_id,
            'createAt': contact.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': contact.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Regional Ministries Contact Information not found'}), 404

@regional_ministries_contact_information_bp.route('/regional_ministries_contact', methods=['POST'])
def add_regional_ministries_contact():
    data = request.get_json()
    if 'name' not in data or 'role' not in data or 'region_id' not in data:
        return jsonify({'message': 'name, role, and region_id are required'}), 400
    
    region = Region.query.get(data['region_id'])
    if not region:
        return jsonify({'message': 'Region not found'}), 404

    new_contact = RegionalMinistriesContactInformation(
        name=data['name'],
        role=data['role'],
        contact=data.get('contact'),
        email=data.get('email'),
        location=data.get('location'),
        region_id=data['region_id']
    )
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({
        'message': 'New regional ministries contact information added!',
        'id': new_contact.id,
        'createAt': new_contact.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_contact.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@regional_ministries_contact_information_bp.route('/regional_ministries_contact/<int:id>', methods=['PUT'])
def update_regional_ministries_contact(id):
    data = request.get_json()
    contact = RegionalMinistriesContactInformation.query.get(id)
    if not contact:
        return jsonify({'message': 'Regional Ministries Contact Information not found'}), 404

    if 'name' in data:
        contact.name = data['name']
    if 'role' in data:
        contact.role = data['role']
    if 'contact' in data:
        contact.contact = data['contact']
    if 'email' in data:
        contact.email = data['email']
    if 'location' in data:
        contact.location = data['location']
    if 'region_id' in data:
        if Region.query.get(data['region_id']):
            contact.region_id = data['region_id']
        else:
            return jsonify({'message': 'Region not found'}), 404

    db.session.commit()
    return jsonify({
        'message': 'Regional Ministries Contact Information updated successfully',
        'createAt': contact.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': contact.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@regional_ministries_contact_information_bp.route('/regional_ministries_contact/<int:id>', methods=['DELETE'])
def delete_regional_ministries_contact(id):
    contact = RegionalMinistriesContactInformation.query.get(id)
    if contact:
        db.session.delete(contact)
        db.session.commit()
        return jsonify({'message': 'Regional Ministries Contact Information deleted successfully'})
    else:
        return jsonify({'message': 'Regional Ministries Contact Information not found'}), 404
