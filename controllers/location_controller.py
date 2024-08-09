from flask import Blueprint, jsonify, request  # type: ignore
from models.location import Location  # Importa o modelo Location
from models import db  # Importa db do __init__.py em models

location_bp = Blueprint('location', __name__)

@location_bp.route('/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([{'id': location.id, 'name': location.name, 'createAt': location.createAt, 'updateAt': location.updateAt} for location in locations])

@location_bp.route('/location/<int:id>', methods=['GET'])
def get_location(id):
    location = Location.query.get(id)
    if location:
        return jsonify({'id': location.id, 'name': location.name, 'createAt': location.createAt, 'updateAt': location.updateAt})
    else:
        return jsonify({'message': 'Location not found'}), 404

@location_bp.route('/location', methods=['POST'])
def add_location():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'name is required'}), 400

    if Location.query.filter_by(name=data['name']).first():
        return jsonify({'message': 'Location with this name already exists'}), 400

    new_location = Location(name=data['name'])
    db.session.add(new_location)
    db.session.commit()
    return jsonify({'message': 'New location added!', 'id': new_location.id}), 201

@location_bp.route('/location/<int:id>', methods=['PUT'])
def update_location(id):
    data = request.get_json()
    location = Location.query.get(id)
    if not location:
        return jsonify({'message': 'Location not found'}), 404

    if 'name' in data:
        if Location.query.filter_by(name=data['name']).first():
            return jsonify({'message': 'Location with this name already exists'}), 400
        location.name = data['name']
    
    db.session.commit()
    return jsonify({'message': 'Location updated successfully'})

@location_bp.route('/location/<int:id>', methods=['DELETE'])
def delete_location(id):
    location = Location.query.get(id)
    if location:
        db.session.delete(location)
        db.session.commit()
        return jsonify({'message': 'Location deleted successfully'})
    else:
        return jsonify({'message': 'Location not found'}), 404
