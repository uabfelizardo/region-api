from flask import Blueprint, jsonify, request  # type: ignore
from models.district import District  # Importa o modelo District
from models import db  # Importa db do __init__.py em models
from datetime import datetime

district_bp = Blueprint('district', __name__)

@district_bp.route('/districts', methods=['GET'])
def get_districts():
    districts = District.query.all()
    return jsonify([{
        'id': district.id,
        'DistrictNumber': district.DistrictNumber,
        'DistrictName': district.DistrictName,
        'Phase': district.Phase,
        'Year_est': district.Year_est,
        'DSname': district.DSname,
        'DateElected': district.DateElected.strftime('%Y-%m-%d'),
        'Email': district.Email,
        'Contact': district.Contact,
        'Language': district.Language,
        'Membership': district.Membership,
        'Churches': district.Churches,
        'Organised': district.Organised,
        'NonOrg': district.NonOrg,
        'Elders': district.Elders,
        'Deacons': district.Deacons,
        'LicensedMin': district.LicensedMin,
        'CountryPopulation': district.CountryPopulation,
        'LocalCurrency': district.LocalCurrency,
        'LocalLanguage': district.LocalLanguage,
        'fieldID': district.fieldID,
        'countryID': district.countryID,
        'personID': district.personID,
        'createAt': district.createAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updateAt': district.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    } for district in districts])

@district_bp.route('/district/<int:id>', methods=['GET'])
def get_district(id):
    district = District.query.get(id)
    if district:
        return jsonify({
            'id': district.id,
            'DistrictNumber': district.DistrictNumber,
            'DistrictName': district.DistrictName,
            'Phase': district.Phase,
            'Year_est': district.Year_est,
            'DSname': district.DSname,
            'DateElected': district.DateElected.strftime('%Y-%m-%d'),
            'Email': district.Email,
            'Contact': district.Contact,
            'Language': district.Language,
            'Membership': district.Membership,
            'Churches': district.Churches,
            'Organised': district.Organised,
            'NonOrg': district.NonOrg,
            'Elders': district.Elders,
            'Deacons': district.Deacons,
            'LicensedMin': district.LicensedMin,
            'CountryPopulation': district.CountryPopulation,
            'LocalCurrency': district.LocalCurrency,
            'LocalLanguage': district.LocalLanguage,
            'fieldID': district.fieldID,
            'countryID': district.countryID,
            'personID': district.personID,
            'createAt': district.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updateAt': district.updateAt.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return jsonify({'message': 'District not found'}), 404

@district_bp.route('/district', methods=['POST'])
def add_district():
    data = request.get_json()
    required_fields = ['DistrictNumber', 'DistrictName', 'Phase', 'Year_est', 'DSname', 'DateElected', 'Email', 'Contact', 'Language', 'Membership', 'Churches', 'Organised', 'NonOrg', 'Elders', 'Deacons', 'LicensedMin', 'CountryPopulation', 'LocalCurrency', 'LocalLanguage', 'fieldID', 'countryID', 'personID']

    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'{field} is required'}), 400

    new_district = District(
        DistrictNumber=data['DistrictNumber'],
        DistrictName=data['DistrictName'],
        Phase=data['Phase'],
        Year_est=data['Year_est'],
        DSname=data['DSname'],
        DateElected=datetime.strptime(data['DateElected'], '%Y-%m-%d'),
        Email=data['Email'],
        Contact=data['Contact'],
        Language=data['Language'],
        Membership=data['Membership'],
        Churches=data['Churches'],
        Organised=data['Organised'],
        NonOrg=data['NonOrg'],
        Elders=data['Elders'],
        Deacons=data['Deacons'],
        LicensedMin=data['LicensedMin'],
        CountryPopulation=data['CountryPopulation'],
        LocalCurrency=data['LocalCurrency'],
        LocalLanguage=data['LocalLanguage'],
        fieldID=data['fieldID'],
        countryID=data['countryID'],
        personID=data['personID']
    )
    db.session.add(new_district)
    db.session.commit()
    return jsonify({'message': 'New district added!', 'id': new_district.id}), 201

@district_bp.route('/district/<int:id>', methods=['PUT'])
def update_district(id):
    data = request.get_json()
    district = District.query.get(id)
    if not district:
        return jsonify({'message': 'District not found'}), 404

    for key, value in data.items():
        if hasattr(district, key):
            setattr(district, key, value)
    
    if 'DateElected' in data:
        district.DateElected = datetime.strptime(data['DateElected'], '%Y-%m-%d')

    db.session.commit()
    return jsonify({'message': 'District updated successfully'})

@district_bp.route('/district/<int:id>', methods=['DELETE'])
def delete_district(id):
    district = District.query.get(id)
    if district:
        db.session.delete(district)
        db.session.commit()
        return jsonify({'message': 'District deleted successfully'})
    else:
        return jsonify({'message': 'District not found'}), 404
