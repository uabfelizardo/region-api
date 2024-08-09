from flask import Blueprint, jsonify, request  # type: ignore
from models.person import Person  # Importa o modelo Person
from models import db  # Importa db do __init__.py em models
from datetime import datetime

person_bp = Blueprint('person', __name__)

@person_bp.route('/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    return jsonify([{
        'id': person.id,
        'surname': person.surname,
        'givenname': person.givenname,
        'gender': person.gender,
        'dateofbirth': person.dateofbirth.strftime('%Y-%m-%d'),
        'pastoralstartdate': person.pastoralstartdate.strftime('%Y-%m-%d') if person.pastoralstartdate else None,
        'dsstartdate': person.dsstartdate.strftime('%Y-%m-%d') if person.dsstartdate else None,
        'citizenship': person.citizenship,
        'spouse': person.spouse,
        'children': person.children,
        'education': person.education,
        'dateelected': person.dateelected.strftime('%Y-%m-%d') if person.dateelected else None,
        'picture': person.picture,
        'createAt': person.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': person.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for person in persons])

@person_bp.route('/person/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get(id)
    if person:
        return jsonify({
            'id': person.id,
            'surname': person.surname,
            'givenname': person.givenname,
            'gender': person.gender,
            'dateofbirth': person.dateofbirth.strftime('%Y-%m-%d'),
            'pastoralstartdate': person.pastoralstartdate.strftime('%Y-%m-%d') if person.pastoralstartdate else None,
            'dsstartdate': person.dsstartdate.strftime('%Y-%m-%d') if person.dsstartdate else None,
            'citizenship': person.citizenship,
            'spouse': person.spouse,
            'children': person.children,
            'education': person.education,
            'dateelected': person.dateelected.strftime('%Y-%m-%d') if person.dateelected else None,
            'picture': person.picture,
            'createAt': person.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': person.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Person not found'}), 404

@person_bp.route('/person', methods=['POST'])
def add_person():
    data = request.get_json()
    required_fields = ['surname', 'givenname', 'gender', 'dateofbirth']

    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'{field} is required'}), 400

    new_person = Person(
        surname=data['surname'],
        givenname=data['givenname'],
        gender=data['gender'],
        dateofbirth=datetime.strptime(data['dateofbirth'], '%Y-%m-%d').date(),
        pastoralstartdate=datetime.strptime(data['pastoralstartdate'], '%Y-%m-%d').date() if 'pastoralstartdate' in data else None,
        dsstartdate=datetime.strptime(data['dsstartdate'], '%Y-%m-%d').date() if 'dsstartdate' in data else None,
        citizenship=data.get('citizenship'),
        spouse=data.get('spouse'),
        children=data.get('children'),
        education=data.get('education'),
        dateelected=datetime.strptime(data['dateelected'], '%Y-%m-%d').date() if 'dateelected' in data else None,
        picture=data.get('picture')
    )
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'New person added!', 'id': new_person.id}), 201

@person_bp.route('/person/<int:id>', methods=['PUT'])
def update_person(id):
    data = request.get_json()
    person = Person.query.get(id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404

    if 'surname' in data:
        person.surname = data['surname']
    if 'givenname' in data:
        person.givenname = data['givenname']
    if 'gender' in data:
        person.gender = data['gender']
    if 'dateofbirth' in data:
        person.dateofbirth = datetime.strptime(data['dateofbirth'], '%Y-%m-%d').date()
    if 'pastoralstartdate' in data:
        person.pastoralstartdate = datetime.strptime(data['pastoralstartdate'], '%Y-%m-%d').date() if data['pastoralstartdate'] else None
    if 'dsstartdate' in data:
        person.dsstartdate = datetime.strptime(data['dsstartdate'], '%Y-%m-%d').date() if data['dsstartdate'] else None
    if 'citizenship' in data:
        person.citizenship = data['citizenship']
    if 'spouse' in data:
        person.spouse = data['spouse']
    if 'children' in data:
        person.children = data['children']
    if 'education' in data:
        person.education = data['education']
    if 'dateelected' in data:
        person.dateelected = datetime.strptime(data['dateelected'], '%Y-%m-%d').date() if data['dateelected'] else None
    if 'picture' in data:
        person.picture = data['picture']

    person.updateAt = datetime.utcnow()  # Atualiza o campo `updateAt`
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'})

@person_bp.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get(id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'})
    else:
        return jsonify({'message': 'Person not found'}), 404
