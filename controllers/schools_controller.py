from flask import Blueprint, jsonify, request
from models.schools import Schools
from models.field import Field
from models.location import Location
from models import db

schools_bp = Blueprint('schools', __name__)

@schools_bp.route('/schools', methods=['GET'])
def get_schools():
    schools = Schools.query.all()
    return jsonify([{
        'id': school.id,
        'School': school.School,
        'ViceChancellor': school.ViceChancellor,
        'DegreesOffered': school.DegreesOffered,
        'field_id': school.field_id,
        'location_id': school.location_id
    } for school in schools])

@schools_bp.route('/school/<int:id>', methods=['GET'])
def get_school(id):
    school = Schools.query.get(id)
    if school:
        return jsonify({
            'id': school.id,
            'School': school.School,
            'ViceChancellor': school.ViceChancellor,
            'DegreesOffered': school.DegreesOffered,
            'field_id': school.field_id,
            'location_id': school.location_id
        })
    else:
        return jsonify({'message': 'School not found'}), 404

@schools_bp.route('/school', methods=['POST'])
def add_school():
    data = request.get_json()
    if 'School' not in data or 'field_id' not in data or 'location_id' not in data:
        return jsonify({'message': 'School, field_id, and location_id are required'}), 400

    field = Field.query.get(data['field_id'])
    location = Location.query.get(data['location_id'])

    if not field or not location:
        return jsonify({'message': 'Invalid field_id or location_id'}), 400

    new_school = Schools(
        School=data['School'],
        ViceChancellor=data.get('ViceChancellor'),
        DegreesOffered=data.get('DegreesOffered'),
        field_id=data['field_id'],
        location_id=data['location_id']
    )
    db.session.add(new_school)
    db.session.commit()
    return jsonify({'message': 'New school added!', 'id': new_school.id}), 201

@schools_bp.route('/school/<int:id>', methods=['PUT'])
def update_school(id):
    data = request.get_json()
    school = Schools.query.get(id)
    if not school:
        return jsonify({'message': 'School not found'}), 404

    if 'School' in data:
        school.School = data['School']
    if 'ViceChancellor' in data:
        school.ViceChancellor = data['ViceChancellor']
    if 'DegreesOffered' in data:
        school.DegreesOffered = data['DegreesOffered']
    if 'field_id' in data:
        if Field.query.get(data['field_id']):
            school.field_id = data['field_id']
        else:
            return jsonify({'message': 'Invalid field_id'}), 400
    if 'location_id' in data:
        if Location.query.get(data['location_id']):
            school.location_id = data['location_id']
        else:
            return jsonify({'message': 'Invalid location_id'}), 400

    db.session.commit()
    return jsonify({'message': 'School updated successfully'})

@schools_bp.route('/school/<int:id>', methods=['DELETE'])
def delete_school(id):
    school = Schools.query.get(id)
    if school:
        db.session.delete(school)
        db.session.commit()
        return jsonify({'message': 'School deleted successfully'})
    else:
        return jsonify({'message': 'School not found'}), 404
