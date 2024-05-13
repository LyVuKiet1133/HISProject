import pytest
from data.Urls import URLS
from apis.config import token, auth_header
from apis.tiepnhan.CurrentServerDateTime import get_server_datetime
import requests
from apis.tiepnhan.CreatePatient import create_patient
from apis.tiepnhan.CreatePatientInsurance import create_patient_insurance
from supports import support


def test_create_visit(token, auth_header, get_server_datetime, create_patient,create_patient_insurance):
    sub_string_replaced = "20240511125645"
    body_visit_on = get_server_datetime
    body_visit_on_content_hash = support.convert_server_time_(body_visit_on)
    body_dob = support.convert_server_time_(create_patient.dob)
    sub_string_replace = support.convert_server_time_string(body_visit_on)
    url = URLS.API_CREATE_VISIT.replace(sub_string_replaced, sub_string_replace)
    print("URL: " + url)
    body = {
        "ReceiveType": 1,
        "RcvState": 1,
        "RxTypeIn": 1,
        "VisitOn": str(body_visit_on),
        "PatientId": create_patient_insurance.patientId,
        "PtName": create_patient.srcFullName,
        "PtAge": 34,
        "PtGender": 2,
        "PtDob": "1990-01-01T00:00:00+07:00",
        "PtAddress": create_patient.address,
        "PtDistrict": create_patient.district,
        "PtWard": create_patient.ward,
        "PtEthnic": create_patient.ethnic,
        "PtNationality": create_patient.nationality,
        "PtOccupation": create_patient.occupation,
        "InsCardNo": create_patient_insurance.insCardNo,
        "InsBenefitType": 2,
        "InsBenefitRatio": 80,
        "Attribute": 0,
        "FileStoreNo": "",
        "CreateById": 3854,
        "Status": 1,
        "InsCheckedMessage": "Thẻ BHYT hợp lệ",
        "InsCheckedStatus": 1,
        "Entry": {
            "MedServiceId": 21250,
            "WardUnitId": 36,
            "OnDate": str(body_visit_on),
            "CreateById": 3854,
            "Status": 1,
            "InsBenefitType": 2,
            "InsBenefitRatio": 80,
            "PriceId": 1083264,
            "CreateByWardUnitId": 560,
            "Service": None,
            "LabExams": None,
            "CreatedBy": None,
            "ContentHash": f'||36|{body_visit_on_content_hash}||||||3854||||New|21250|80|||2|1083264|||'
        },
        "FullPatientCode": None,
        "InsBenefitTypeName": None,
        "WardUnitNames": None,
        "CreateByStaffName": None,
        "ContentHash": f'||1|Normal|CorrectRoute|{body_visit_on_content_hash}|{create_patient_insurance.patientId}|{create_patient.srcFullName}|34|Female|{body_dob}|Suối Tre|732|26095|01|VN|10||{create_patient_insurance.insCardNo}|2|80|None|||||||||3854|Open|||||||||||36|{body_visit_on_content_hash}||||||3854||||New|21250|80|||2|1083264|||',
        "LastUpdateByStaffName": None,
        "ModifiedOn": None
    }
    response = requests.post(url, json=body, headers=auth_header)
    json_data = response.json()
    print(json_data)
    assert response.status_code == 200
