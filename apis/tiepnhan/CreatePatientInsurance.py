import time
from datetime import datetime

import pytest
import requests
from data.Urls import URLS
from apis.tiepnhan.CreatePatient import create_patient
from apis.config import token, auth_header
from data.Patients import Patient
from supports import support


@pytest.fixture(scope="session")
def create_patient_insurance(token, auth_header, create_patient):
    patient = create_patient
    body = {
        "PatientId": patient.patientId,
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
    response = requests.post(f'{URLS.API_CREATE_PATIENT_INSURANCE}{support.convert_server_time_string(patient.dob)}',
                             json=body, headers=auth_header)
    print(f'{URLS.API_CREATE_PATIENT_INSURANCE}{support.convert_server_time_string(patient.dob)}')
    json_data = response.json()
    print(json_data)
    assert response.status_code == 201
    patientId = json_data['patientId']
    insCardNo = json_data['insCardNo']
    ins_patient = Patient(patientId=patientId, insCardNo=insCardNo)
    return ins_patient
