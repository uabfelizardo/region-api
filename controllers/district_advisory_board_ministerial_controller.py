from flask import Blueprint, jsonify, request  # type: ignore
from models.district_advisory_board_ministerial import DistrictAdvisoryBoardMinisterial  # Importa o modelo DistrictAdvisoryBoardMinisterial
from models import db  # Importa db do __init__.py em models

district_advisory_board_ministerial_bp = Blueprint('district_advisory_board_ministerial', __name__)

@district_advisory_board_ministerial_bp.route('/district_advisory_board_ministerials', methods=['GET'])
def get_district_advisory_board_ministerials():
    advisory_board_ministerials = DistrictAdvisoryBoardMinisterial.query.all()
    return jsonify([{
        'id': advisory_board_ministerial.id,
        'personName': advisory_board_ministerial.personName,
        'district_id': advisory_board_ministerial.district_id,
        'createAt': advisory_board_ministerial.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': advisory_board_ministerial.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for advisory_board_ministerial in advisory_board_ministerials])

@district_advisory_board_ministerial_bp.route('/district_advisory_board_ministerial/<int:id>', methods=['GET'])
def get_district_advisory_board_ministerial(id):
    advisory_board_ministerial = DistrictAdvisoryBoardMinisterial.query.get(id)
    if advisory_board_ministerial:
        return jsonify({
            'id': advisory_board_ministerial.id,
            'personName': advisory_board_ministerial.personName,
            'district_id': advisory_board_ministerial.district_id,
            'createAt': advisory_board_ministerial.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': advisory_board_ministerial.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'DistrictAdvisoryBoardMinisterial not found'}), 404

@district_advisory_board_ministerial_bp.route('/district_advisory_board_ministerial', methods=['POST'])
def add_district_advisory_board_ministerial():
    data = request.get_json()
    if 'personName' not in data or 'district_id' not in data:
        return jsonify({'message': 'personName and district_id are required'}), 400

    new_advisory_board_ministerial = DistrictAdvisoryBoardMinisterial(
        personName=data['personName'],
        district_id=data['district_id']
    )
    db.session.add(new_advisory_board_ministerial)
    db.session.commit()
    return jsonify({
        'message': 'New DistrictAdvisoryBoardMinisterial added!',
        'id': new_advisory_board_ministerial.id,
        'createAt': new_advisory_board_ministerial.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_advisory_board_ministerial.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@district_advisory_board_ministerial_bp.route('/district_advisory_board_ministerial/<int:id>', methods=['PUT'])
def update_district_advisory_board_ministerial(id):
    data = request.get_json()
    advisory_board_ministerial = DistrictAdvisoryBoardMinisterial.query.get(id)
    if not advisory_board_ministerial:
        return jsonify({'message': 'DistrictAdvisoryBoardMinisterial not found'}), 404

    if 'personName' in data:
        advisory_board_ministerial.personName = data['personName']
    if 'district_id' in data:
        advisory_board_ministerial.district_id = data['district_id']

    db.session.commit()
    return jsonify({
        'message': 'DistrictAdvisoryBoardMinisterial updated successfully',
        'createAt': advisory_board_ministerial.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': advisory_board_ministerial.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@district_advisory_board_ministerial_bp.route('/district_advisory_board_ministerial/<int:id>', methods=['DELETE'])
def delete_district_advisory_board_ministerial(id):
    advisory_board_ministerial = DistrictAdvisoryBoardMinisterial.query.get(id)
    if advisory_board_ministerial:
        db.session.delete(advisory_board_ministerial)
        db.session.commit()
        return jsonify({'message': 'DistrictAdvisoryBoardMinisterial deleted successfully'})
    else:
        return jsonify({'message': 'DistrictAdvisoryBoardMinisterial not found'}), 404
