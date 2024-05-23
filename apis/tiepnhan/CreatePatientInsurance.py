import time
from datetime import datetime

import pytest
import requests
from data.Urls import URLS
from apis.tiepnhan.CreatePatient import create_patient
from apis.config import get_auth_header
from data.Patients import Patient
from supports import support


#@pytest.fixture(scope="session")
def create_patient_insurance():
    auth_header = get_auth_header()
    json_response_patient = create_patient()
    patientId = json_response_patient['patientId']
    body = {
        "PatientId": patientId,
        "InsCardNo": "GD401" + support.get_random_last_10digits(),
        "InsName": "BHXH",
        "StartDate": "2024-01-01T00:00:00+07:00",
        "EndDate": "2024-12-31T00:00:00+07:00",
        "MedProviderId": 3075,
        "Address": "Suối Tre",
        "Country": "VN",
        "City": "75",
        "District": "732",
        "Ward": "26095",
        "InsZone": 0,
        "Status": 1,
        "Attribute": 0,
        "Provider": None,
        "IsDisabled": False,
        "IsTemp": False,
        "FullInsOn": None
    }
    response = requests.post(f'{URLS.API_CREATE_PATIENT_INSURANCE}{support.convert_server_time_string(json_response_patient['dob'])}',
                             json=body, headers=auth_header)
    print(f'{URLS.API_CREATE_PATIENT_INSURANCE}{support.convert_server_time_string(json_response_patient['dob'])}')
    json_response_insurance = response.json()
    print(json_response_insurance)
    assert response.status_code == 201
    patientId = json_response_insurance['patientId']
    insCardNo = json_response_insurance['insCardNo']
    ins_patient = Patient(patientId=patientId, insCardNo=insCardNo)
    return json_response_patient, json_response_insurance
def test_create_patient_insurance():
    patient_insurance = create_patient_insurance()
