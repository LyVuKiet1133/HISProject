import concurrent
import json

import pytest
import concurrent.futures
from data.Urls import URLS
from apis.config import get_auth_header
from apis.CurrentServerDateTime import get_server_datetime
import requests
from apis.tiepnhan.CreatePatient import create_patient
from apis.tiepnhan.CreatePatientInsurance import create_patient_insurance
from supports import support
from data.Visits import Visit


# @pytest.fixture(scope='session')
def create_visit():
    auth_header = get_auth_header()
    json_response_patient, json_response_insurance = create_patient_insurance()
    sub_string_replaced = "20240511125645"
    body_visit_on = get_server_datetime()
    body_visit_on_content_hash = support.convert_server_time_ddmmyyyhhmm(body_visit_on)
    body_dob = support.convert_server_time_ddmmyyyhhmm(json_response_patient['dob'])
    sub_string_replace = support.convert_server_time_string(body_visit_on)
    url = URLS.API_CREATE_VISIT.replace(sub_string_replaced, sub_string_replace)
    print("URL: " + url)
    body = {
        "ReceiveType": 1,
        "RcvState": 1,
        "RxTypeIn": 1,
        "VisitOn": str(body_visit_on),
        "PatientId": json_response_insurance['patientId'],
        "PtName": json_response_patient['srcFullName'],
        "PtAge": 34,
        "PtGender": 2,
        "PtDob": "1990-01-01T00:00:00+07:00",
        "PtAddress": json_response_patient['address'],
        "PtDistrict": json_response_patient['district'],
        "PtWard": json_response_patient['ward'],
        "PtEthnic": json_response_patient['ethnic'],
        "PtNationality": json_response_patient['nationality'],
        "PtOccupation": json_response_patient['occupation'],
        "InsCardNo": json_response_insurance['insCardNo'],
        "InsBenefitType": 2,
        "InsBenefitRatio": 80,
        "Attribute": 0,
        "FileStoreNo": "",
        "CreateById": 4451,
        "Status": 1,
        "InsCheckedMessage": "Thẻ BHYT hợp lệ",
        "InsCheckedStatus": 1,
        "Entry": {
            "MedServiceId": 21250,
            "WardUnitId": 36,
            "OnDate": str(body_visit_on),
            "CreateById": 4451,
            "Status": 1,
            "InsBenefitType": 2,
            "InsBenefitRatio": 80,
            "PriceId": 1083264,
            "CreateByWardUnitId": 560,
            "Service": None,
            "LabExams": None,
            "CreatedBy": None,
            "ContentHash": f'||36|{body_visit_on_content_hash}||||||4451||||New|21250|80|||2|1083264|||'
        },
        "FullPatientCode": None,
        "InsBenefitTypeName": None,
        "WardUnitNames": None,
        "CreateByStaffName": None,
        "ContentHash": f'||1|Normal|CorrectRoute|{body_visit_on_content_hash}|{json_response_insurance['patientId']}|{json_response_patient['srcFullName']}|34|Female|{body_dob}|Suối Tre|732|26095|01|VN|10||{json_response_insurance['insCardNo']}|2|80|None|||||||||4451|Open|||||||||||36|{body_visit_on_content_hash}||||||4451||||New|21250|80|||2|1083264|||',
        "LastUpdateByStaffName": None,
        "ModifiedOn": None
    }
    response = requests.post(url, json=body, headers=auth_header)
    json_data_visit = response.json()
    print(json_data_visit)
    assert response.status_code == 200
    '''entryId = json_data_visit['entry']['entryId']
    visitId = json_data_visit['entry']['visitId']
    medServiceId = json_data_visit['entry']['medServiceId']
    wardUnitId = json_data_visit['entry']['wardUnitId']
    onDate = json_data_visit['entry']['onDate']
    insBenefitType = json_data_visit['entry']['insBenefitType']
    insBenefitRatio = json_data_visit['entry']['insBenefitRatio']
    priceId = json_data_visit['entry']['priceId']
    qmsNo = json_data_visit['entry']['qmsNo']
    ticketId = json_data_visit['entry']['ticketId']
    createByWardUnitId = json_data_visit['entry']['createByWardUnitId']

    visit = Visit(entryId=entryId, visitId=visitId, medServiceId=medServiceId,
                  wardUnitId=wardUnitId, onDate=onDate, insBenefitType=insBenefitType,
                  insBenefitRatio=insBenefitRatio, priceId=priceId, qmsNo=qmsNo,
                  ticketId=ticketId, createByWardUnitId=createByWardUnitId)'''
    return json_data_visit


'''def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit() for _ in range(2)]
        for future in concurrent.futures.as_completed(futures):
            response = future.result()'''


'''if __name__ == "__main__":
    main()
'''