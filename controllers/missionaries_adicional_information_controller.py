from flask import Blueprint, jsonify, request  # type: ignore
from models.missionaries_adicional_information import MissionariesAdicionalInformation  # Importa o modelo MissionariesAdicionalInformation
from models import db  # Importa db do __init__.py em models

missionaries_adicional_information_bp = Blueprint('missionaries_adicional_information', __name__)

@missionaries_adicional_information_bp.route('/adicional_info', methods=['GET'])
def get_adicional_info():
    info_list = MissionariesAdicionalInformation.query.all()
    return jsonify([{
        'id': info.id,
        'year': info.year,
        'Deployment': info.Deployment,
        'AdmissionDate': info.AdmissionDate.strftime('%Y-%m-%d'),
        'YearsOfService': info.YearsOfService,
        'LicenseDays': info.LicenseDays,
        'DaysOnBalance': info.DaysOnBalance,
        'Notes': info.Notes,
        'VacationType': info.VacationType,
        'DaysOff': info.DaysOff,
        'missionary_id': info.missionary_id,
        'createAt': info.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': info.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for info in info_list])

@missionaries_adicional_information_bp.route('/adicional_info/<int:id>', methods=['GET'])
def get_adicional_info_by_id(id):
    info = MissionariesAdicionalInformation.query.get(id)
    if info:
        return jsonify({
            'id': info.id,
            'year': info.year,
            'Deployment': info.Deployment,
            'AdmissionDate': info.AdmissionDate.strftime('%Y-%m-%d'),
            'YearsOfService': info.YearsOfService,
            'LicenseDays': info.LicenseDays,
            'DaysOnBalance': info.DaysOnBalance,
            'Notes': info.Notes,
            'VacationType': info.VacationType,
            'DaysOff': info.DaysOff,
            'missionary_id': info.missionary_id,
            'createAt': info.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': info.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'Adicional Information not found'}), 404

@missionaries_adicional_information_bp.route('/adicional_info', methods=['POST'])
def add_adicional_info():
    data = request.get_json()
    required_fields = ['year', 'Deployment', 'AdmissionDate', 'YearsOfService', 'LicenseDays', 'DaysOnBalance', 'missionary_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'{field} is required'}), 400

    new_info = MissionariesAdicionalInformation(
        year=data['year'],
        Deployment=data['Deployment'],
        AdmissionDate=data['AdmissionDate'],
        YearsOfService=data['YearsOfService'],
        LicenseDays=data['LicenseDays'],
        DaysOnBalance=data['DaysOnBalance'],
        Notes=data.get('Notes'),
        VacationType=data.get('VacationType'),
        DaysOff=data.get('DaysOff'),
        missionary_id=data['missionary_id']
    )
    db.session.add(new_info)
    db.session.commit()
    return jsonify({
        'message': 'New additional information added!',
        'id': new_info.id,
        'createAt': new_info.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': new_info.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@missionaries_adicional_information_bp.route('/adicional_info/<int:id>', methods=['PUT'])
def update_adicional_info(id):
    data = request.get_json()
    info = MissionariesAdicionalInformation.query.get(id)
    if not info:
        return jsonify({'message': 'Adicional Information not found'}), 404

    if 'year' in data:
        info.year = data['year']
    if 'Deployment' in data:
        info.Deployment = data['Deployment']
    if 'AdmissionDate' in data:
        info.AdmissionDate = data['AdmissionDate']
    if 'YearsOfService' in data:
        info.YearsOfService = data['YearsOfService']
    if 'LicenseDays' in data:
        info.LicenseDays = data['LicenseDays']
    if 'DaysOnBalance' in data:
        info.DaysOnBalance = data['DaysOnBalance']
    if 'Notes' in data:
        info.Notes = data['Notes']
    if 'VacationType' in data:
        info.VacationType = data['VacationType']
    if 'DaysOff' in data:
        info.DaysOff = data['DaysOff']
    if 'missionary_id' in data:
        info.missionary_id = data['missionary_id']

    db.session.commit()
    return jsonify({
        'message': 'Adicional Information updated successfully',
        'createAt': info.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': info.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    })

@missionaries_adicional_information_bp.route('/adicional_info/<int:id>', methods=['DELETE'])
def delete_adicional_info(id):
    info = MissionariesAdicionalInformation.query.get(id)
    if info:
        db.session.delete(info)
        db.session.commit()
        return jsonify({'message': 'Adicional Information deleted successfully'})
    else:
        return jsonify({'message': 'Adicional Information not found'}), 404
