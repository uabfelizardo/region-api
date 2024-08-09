from flask import Blueprint, jsonify, request  # type: ignore
from models.country import Country  # Importa o modelo Country
from models import db  # Importa db do __init__.py em models

country_bp = Blueprint('country', __name__)

@country_bp.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    return jsonify([{
        'id': country.id,
        'Country': country.Country,
        'Map': country.Map,
        'field_id': country.field_id,
        'createAt': country.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': country.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for country in countries])

@country_bp.route('/country/<int:id>', methods=['GET'])
def get_country(id):
    country = Country.query.get(id)
    if country:
        return jsonify({
            'id': country.id,
            'Country': country.Country,
            'Map': country.Map,
            'field_id': country.field_id,
            'createAt': country.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': country.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Country not found'}), 404

@country_bp.route('/country', methods=['POST'])
def add_country():
    data = request.get_json()
    required_fields = ['Country', 'field_id']

    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'{field} is required'}), 400

    new_country = Country(
        Country=data['Country'],
        Map=data.get('Map'),
        field_id=data['field_id']
    )
    db.session.add(new_country)
    db.session.commit()
    return jsonify({
        'message': 'New country added!',
        'id': new_country.id,
        'createAt': new_country.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_country.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@country_bp.route('/country/<int:id>', methods=['PUT'])
def update_country(id):
    data = request.get_json()
    country = Country.query.get(id)
    if not country:
        return jsonify({'message': 'Country not found'}), 404

    if 'Country' in data:
        country.Country = data['Country']
    if 'Map' in data:
        country.Map = data['Map']
    if 'field_id' in data:
        country.field_id = data['field_id']

    db.session.commit()
    return jsonify({
        'message': 'Country updated successfully',
        'createAt': country.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': country.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@country_bp.route('/country/<int:id>', methods=['DELETE'])
def delete_country(id):
    country = Country.query.get(id)
    if country:
        db.session.delete(country)
        db.session.commit()
        return jsonify({'message': 'Country deleted successfully'})
    else:
        return jsonify({'message': 'Country not found'}), 404
