from flask import Blueprint, jsonify, request  # type: ignore
from models.field import Field  # Importa o modelo Field
from models.country import Country  # Importa o modelo Country
from models import db  # Importa db do __init__.py em models

field_bp = Blueprint('field', __name__)

@field_bp.route('/fields', methods=['GET'])
def get_fields():
    fields = Field.query.all()
    return jsonify([{
        'id': field.id,
        'fieldName': field.fieldName,
        'picture': field.picture,
        'description': field.description,
        'createAt': field.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': field.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for field in fields])

@field_bp.route('/field/<int:id>', methods=['GET'])
def get_field(id):
    field = Field.query.get(id)
    if field:
        return jsonify({
            'id': field.id,
            'fieldName': field.fieldName,
            'picture': field.picture,
            'description': field.description,
            'createAt': field.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': field.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Field not found'}), 404

@field_bp.route('/field', methods=['POST'])
def add_field():
    data = request.get_json()
    if 'fieldName' not in data:
        return jsonify({'message': 'fieldName is required'}), 400

    new_field = Field(
        fieldName=data['fieldName'],
        picture=data.get('picture'),
        description=data.get('description')
    )
    db.session.add(new_field)
    db.session.commit()
    return jsonify({
        'message': 'New field added!',
        'id': new_field.id,
        'createAt': new_field.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_field.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@field_bp.route('/field/<int:id>', methods=['PUT'])
def update_field(id):
    data = request.get_json()
    field = Field.query.get(id)
    if not field:
        return jsonify({'message': 'Field not found'}), 404

    if 'fieldName' in data:
        field.fieldName = data['fieldName']
    if 'picture' in data:
        field.picture = data['picture']
    if 'description' in data:
        field.description = data['description']

    db.session.commit()
    return jsonify({
        'message': 'Field updated successfully',
        'createAt': field.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': field.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@field_bp.route('/field/<int:id>', methods=['DELETE'])
def delete_field(id):
    field = Field.query.get(id)
    if field:
        db.session.delete(field)
        db.session.commit()
        return jsonify({'message': 'Field deleted successfully'})
    else:
        return jsonify({'message': 'Field not found'}), 404

@field_bp.route('/field/<int:id>/countries', methods=['GET'])
def get_countries_by_field(id):
    field = Field.query.get(id)
    if not field:
        return jsonify({'message': 'Field not found'}), 404

    countries = Country.query.filter_by(field_id=id).all()
    return jsonify([{
        'id': country.id,
        'Country': country.Country,
        'Map': country.Map,
        'field_id': country.field_id,
        'createAt': country.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': country.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for country in countries])
