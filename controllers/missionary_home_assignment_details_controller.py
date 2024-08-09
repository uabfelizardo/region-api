from flask import Blueprint, jsonify, request  # type: ignore
from models.missionary_home_assignment_details import MissionaryHomeAssignmentDetails  # Importa o modelo MissionaryHomeAssignmentDetails
from models import db  # Importa db do __init__.py em models

missionary_home_assignment_details_bp = Blueprint('missionary_home_assignment_details', __name__)

@missionary_home_assignment_details_bp.route('/home_assignments', methods=['GET'])
def get_home_assignments():
    assignments = MissionaryHomeAssignmentDetails.query.all()
    return jsonify([{
        'id': assignment.id,
        'home_assignment_date': assignment.home_assignment_date.strftime('%Y-%m-%d'),
        'StartDate': assignment.StartDate.strftime('%Y-%m-%d'),
        'EndDate': assignment.EndDate.strftime('%Y-%m-%d'),
        'Place': assignment.Place,
        'Notes': assignment.Notes,
        'missionary_id': assignment.missionary_id,
        'createAt': assignment.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': assignment.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for assignment in assignments])

@missionary_home_assignment_details_bp.route('/home_assignment/<int:id>', methods=['GET'])
def get_home_assignment_by_id(id):
    assignment = MissionaryHomeAssignmentDetails.query.get(id)
    if assignment:
        return jsonify({
            'id': assignment.id,
            'home_assignment_date': assignment.home_assignment_date.strftime('%Y-%m-%d'),
            'StartDate': assignment.StartDate.strftime('%Y-%m-%d'),
            'EndDate': assignment.EndDate.strftime('%Y-%m-%d'),
            'Place': assignment.Place,
            'Notes': assignment.Notes,
            'missionary_id': assignment.missionary_id,
            'createAt': assignment.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': assignment.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Home Assignment not found'}), 404

@missionary_home_assignment_details_bp.route('/home_assignment', methods=['POST'])
def add_home_assignment():
    data = request.get_json()
    required_fields = ['home_assignment_date', 'StartDate', 'EndDate', 'Place', 'missionary_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'{field} is required'}), 400

    new_assignment = MissionaryHomeAssignmentDetails(
        home_assignment_date=data['home_assignment_date'],
        StartDate=data['StartDate'],
        EndDate=data['EndDate'],
        Place=data['Place'],
        Notes=data.get('Notes'),
        missionary_id=data['missionary_id']
    )
    db.session.add(new_assignment)
    db.session.commit()
    return jsonify({
        'message': 'New home assignment added!',
        'id': new_assignment.id,
        'createAt': new_assignment.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_assignment.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@missionary_home_assignment_details_bp.route('/home_assignment/<int:id>', methods=['PUT'])
def update_home_assignment(id):
    data = request.get_json()
    assignment = MissionaryHomeAssignmentDetails.query.get(id)
    if not assignment:
        return jsonify({'message': 'Home Assignment not found'}), 404

    if 'home_assignment_date' in data:
        assignment.home_assignment_date = data['home_assignment_date']
    if 'StartDate' in data:
        assignment.StartDate = data['StartDate']
    if 'EndDate' in data:
        assignment.EndDate = data['EndDate']
    if 'Place' in data:
        assignment.Place = data['Place']
    if 'Notes' in data:
        assignment.Notes = data['Notes']
    if 'missionary_id' in data:
        assignment.missionary_id = data['missionary_id']

    db.session.commit()
    return jsonify({
        'message': 'Home Assignment updated successfully',
        'createAt': assignment.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': assignment.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@missionary_home_assignment_details_bp.route('/home_assignment/<int:id>', methods=['DELETE'])
def delete_home_assignment(id):
    assignment = MissionaryHomeAssignmentDetails.query.get(id)
    if assignment:
        db.session.delete(assignment)
        db.session.commit()
        return jsonify({'message': 'Home Assignment deleted successfully'})
    else:
        return jsonify({'message': 'Home Assignment not found'}), 404
