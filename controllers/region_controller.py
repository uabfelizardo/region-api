from flask import Blueprint, jsonify, request  # type: ignore
from models.region import Region  # Importa o modelo Region
from models import db  # Importa db do __init__.py em models

region_bp = Blueprint('region', __name__)

@region_bp.route('/regions', methods=['GET'])
def get_regions():
    regions = Region.query.all()
    return jsonify([{
        'id': region.id,
        'name': region.name,
        'createAt': region.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': region.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for region in regions])

@region_bp.route('/region/<int:id>', methods=['GET'])
def get_region(id):
    region = Region.query.get(id)
    if region:
        return jsonify({
            'id': region.id,
            'name': region.name,
            'createAt': region.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': region.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Region not found'}), 404

@region_bp.route('/region', methods=['POST'])
def add_region():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'name is required'}), 400

    if Region.query.filter_by(name=data['name']).first():
        return jsonify({'message': 'Region with this name already exists'}), 400

    new_region = Region(name=data['name'])
    db.session.add(new_region)
    db.session.commit()
    return jsonify({
        'message': 'New region added!',
        'id': new_region.id,
        'createAt': new_region.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_region.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@region_bp.route('/region/<int:id>', methods=['PUT'])
def update_region(id):
    data = request.get_json()
    region = Region.query.get(id)
    if not region:
        return jsonify({'message': 'Region not found'}), 404

    if 'name' in data:
        if Region.query.filter_by(name=data['name']).first():
            return jsonify({'message': 'Region with this name already exists'}), 400
        region.name = data['name']
    
    db.session.commit()
    return jsonify({
        'message': 'Region updated successfully',
        'createAt': region.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': region.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@region_bp.route('/region/<int:id>', methods=['DELETE'])
def delete_region(id):
    region = Region.query.get(id)
    if region:
        db.session.delete(region)
        db.session.commit()
        return jsonify({'message': 'Region deleted successfully'})
    else:
        return jsonify({'message': 'Region not found'}), 404
