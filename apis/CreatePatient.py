import requests
import pytest
from apis.config import token, auth_header
from data.Urls import URLS
from data.Patients import Patient


def test_create_patient(token, auth_header):
    patient = Patient.random_patient()
    body = {
        "PatientCode": "SimulatedCode",
        "FullPatientCode": "SimulatedCode",
        "FirstName": patient.first_name,
        "LastName": patient.last_name,
        "Dob": "1990-01-01T00:00:00+07:00",
        "Gender": 1,
        "IdCardNo": "",
        "MobileNo": "",
        "Nationality": "VN",
        "Ethnic": "01",
        "Country": "VN",
        "City": "75",
        "District": "732",
        "Ward": "26095",
        "Address": patient.address,
        "Occupation": 10,
        "EmployerName": "",
        "EmployerAddr": "",
        "TaxCode": "",
        "RelativeName": "",
        "RelativeAddr": "",
        "RelativePhone": "",
        "RelativeType": 0,
        "Status": 1,
        "FullName": "LVK 1205",
        "FullAddress": "Suối Tre"
    }
    response = requests.post(URLS.API_CREATE_PATIENT, json=body, headers=auth_header)
    assert response.status_code == 201
    json_data = response.json()
    print(json_data)
    assert json_data['patientCode'] is not None
