from flask import Blueprint, jsonify, request  # type: ignore
from models.area import Area  # Importa o modelo Area
from models import db  # Importa db do __init__.py em models

area_bp = Blueprint('area', __name__)

@area_bp.route('/areas', methods=['GET'])
def get_areas():
    areas = Area.query.all()
    return jsonify([{
        'id': area.id,
        'areaName': area.areaName,
        'createAt': area.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': area.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for area in areas])

@area_bp.route('/area/<int:id>', methods=['GET'])
def get_area(id):
    area = Area.query.get(id)
    if area:
        return jsonify({
            'id': area.id,
            'areaName': area.areaName,
            'createAt': area.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': area.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Area not found'}), 404

@area_bp.route('/area', methods=['POST'])
def add_area():
    data = request.get_json()
    if 'areaName' not in data:
        return jsonify({'message': 'areaName is required'}), 400

    if Area.query.filter_by(areaName=data['areaName']).first():
        return jsonify({'message': 'Area with this name already exists'}), 400

    new_area = Area(areaName=data['areaName'])
    db.session.add(new_area)
    db.session.commit()
    return jsonify({
        'message': 'New area added!',
        'id': new_area.id,
        'createAt': new_area.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_area.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@area_bp.route('/area/<int:id>', methods=['PUT'])
def update_area(id):
    data = request.get_json()
    area = Area.query.get(id)
    if not area:
        return jsonify({'message': 'Area not found'}), 404

    if 'areaName' in data:
        if Area.query.filter_by(areaName=data['areaName']).first():
            return jsonify({'message': 'Area with this name already exists'}), 400
        area.areaName = data['areaName']
        db.session.commit()
        return jsonify({
            'message': 'Area updated successfully',
            'createAt': area.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': area.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return jsonify({'message': 'No data to update'}), 400

@area_bp.route('/area/<int:id>', methods=['DELETE'])
def delete_area(id):
    area = Area.query.get(id)
    if area:
        db.session.delete(area)
        db.session.commit()
        return jsonify({'message': 'Area deleted successfully'})
    else:
        return jsonify({'message': 'Area not found'}), 404
