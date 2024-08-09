from flask import Blueprint, jsonify, request  # type: ignore
from models.region_and_field_contact_information import RegionAndFieldContactInformation  # Importa o modelo RegionAndFieldContactInformation
from models.region import Region  # Importa o modelo Region
from models import db  # Importa db do __init__.py em models

region_and_field_contact_information_bp = Blueprint('region_and_field_contact_information', __name__)

#region_and_field_contact_information_bp.route('/region_and_field_contacts', methods=['GET'])
def get_region_and_field_contacts():
    contacts = RegionAndFieldContactInformation.query.all()
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

@region_and_field_contact_information_bp.route('/region_and_field_contact/<int:id>', methods=['GET'])
def get_region_and_field_contact(id):
    contact = RegionAndFieldContactInformation.query.get(id)
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
        return jsonify({'message': 'Region and Field Contact Information not found'}), 404

@region_and_field_contact_information_bp.route('/region_and_field_contact', methods=['POST'])
def add_region_and_field_contact():
    data = request.get_json()
    if 'name' not in data or 'role' not in data or 'region_id' not in data:
        return jsonify({'message': 'name, role, and region_id are required'}), 400
    
    region = Region.query.get(data['region_id'])
    if not region:
        return jsonify({'message': 'Region not found'}), 404

    new_contact = RegionAndFieldContactInformation(
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
        'message': 'New region and field contact information added!',
        'id': new_contact.id,
        'createAt': new_contact.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_contact.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@region_and_field_contact_information_bp.route('/region_and_field_contact/<int:id>', methods=['PUT'])
def update_region_and_field_contact(id):
    data = request.get_json()
    contact = RegionAndFieldContactInformation.query.get(id)
    if not contact:
        return jsonify({'message': 'Region and Field Contact Information not found'}), 404

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
        'message': 'Region and Field Contact Information updated successfully',
        'createAt': contact.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': contact.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@region_and_field_contact_information_bp.route('/region_and_field_contact/<int:id>', methods=['DELETE'])
def delete_region_and_field_contact(id):
    contact = RegionAndFieldContactInformation.query.get(id)
    if contact:
        db.session.delete(contact)
        db.session.commit()
        return jsonify({'message': 'Region and Field Contact Information deleted successfully'})
    else:
        return jsonify({'message': 'Region and Field Contact Information not found'}), 404
