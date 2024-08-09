from flask import Blueprint, jsonify, request  # type: ignore
from models.district_advisory_board_lay import DistrictAdvisoryBoardLay  # Importa o modelo DistrictAdvisoryBoardLay
from models import db  # Importa db do __init__.py em models

district_advisory_board_lay_bp = Blueprint('district_advisory_board_lay', __name__)

@district_advisory_board_lay_bp.route('/district_advisory_board_lays', methods=['GET'])
def get_district_advisory_board_lays():
    advisory_board_lays = DistrictAdvisoryBoardLay.query.all()
    return jsonify([{
        'id': advisory_board_lay.id,
        'personName': advisory_board_lay.personName,
        'district_id': advisory_board_lay.district_id,
        'createAt': advisory_board_lay.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': advisory_board_lay.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for advisory_board_lay in advisory_board_lays])

@district_advisory_board_lay_bp.route('/district_advisory_board_lay/<int:id>', methods=['GET'])
def get_district_advisory_board_lay(id):
    advisory_board_lay = DistrictAdvisoryBoardLay.query.get(id)
    if advisory_board_lay:
        return jsonify({
            'id': advisory_board_lay.id,
            'personName': advisory_board_lay.personName,
            'district_id': advisory_board_lay.district_id,
            'createAt': advisory_board_lay.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': advisory_board_lay.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'DistrictAdvisoryBoardLay not found'}), 404

@district_advisory_board_lay_bp.route('/district_advisory_board_lay', methods=['POST'])
def add_district_advisory_board_lay():
    data = request.get_json()
    if 'personName' not in data or 'district_id' not in data:
        return jsonify({'message': 'personName and district_id are required'}), 400

    new_advisory_board_lay = DistrictAdvisoryBoardLay(
        personName=data['personName'],
        district_id=data['district_id']
    )
    db.session.add(new_advisory_board_lay)
    db.session.commit()
    return jsonify({
        'message': 'New DistrictAdvisoryBoardLay added!',
        'id': new_advisory_board_lay.id,
        'createAt': new_advisory_board_lay.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_advisory_board_lay.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@district_advisory_board_lay_bp.route('/district_advisory_board_lay/<int:id>', methods=['PUT'])
def update_district_advisory_board_lay(id):
    data = request.get_json()
    advisory_board_lay = DistrictAdvisoryBoardLay.query.get(id)
    if not advisory_board_lay:
        return jsonify({'message': 'DistrictAdvisoryBoardLay not found'}), 404

    if 'personName' in data:
        advisory_board_lay.personName = data['personName']
    if 'district_id' in data:
        advisory_board_lay.district_id = data['district_id']

    db.session.commit()
    return jsonify({
        'message': 'DistrictAdvisoryBoardLay updated successfully',
        'createAt': advisory_board_lay.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': advisory_board_lay.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@district_advisory_board_lay_bp.route('/district_advisory_board_lay/<int:id>', methods=['DELETE'])
def delete_district_advisory_board_lay(id):
    advisory_board_lay = DistrictAdvisoryBoardLay.query.get(id)
    if advisory_board_lay:
        db.session.delete(advisory_board_lay)
        db.session.commit()
        return jsonify({'message': 'DistrictAdvisoryBoardLay deleted successfully'})
    else:
        return jsonify({'message': 'DistrictAdvisoryBoardLay not found'}), 404
