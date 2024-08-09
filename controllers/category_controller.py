from flask import Blueprint, jsonify, request  # type: ignore
from models.category import Category  # Importa o modelo Category
from models import db  # Importa db do __init__.py em models
from datetime import datetime

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{
        'id': category.id,
        'name': category.name,
        'createAt': category.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': category.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for category in categories])

@category_bp.route('/category/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get(id)
    if category:
        return jsonify({
            'id': category.id,
            'name': category.name,
            'createAt': category.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': category.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Category not found'}), 404

@category_bp.route('/category', methods=['POST'])
def add_category():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'Name is required'}), 400

    if Category.query.filter_by(name=data['name']).first():
        return jsonify({'message': 'Category with this name already exists'}), 400

    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'New category added!', 'id': new_category.id}), 201

@category_bp.route('/category/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    category = Category.query.get(id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404

    if 'name' in data:
        if Category.query.filter_by(name=data['name']).first():
            return jsonify({'message': 'Category with this name already exists'}), 400
        category.name = data['name']

    category.updateAt = datetime.utcnow()  # Atualiza o campo `updateAt`
    db.session.commit()
    return jsonify({'message': 'Category updated successfully'})

@category_bp.route('/category/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'})
    else:
        return jsonify({'message': 'Category not found'}), 404
