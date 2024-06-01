import json
import time

import pytest
import requests

from apis.config import get_auth_header
from apis.kb_ketoa.Get_Drugs_To_Prescribe import get_drug
from apis.CurrentServerDateTime import get_server_datetime
from apis.tiepnhan.Create_Visit import create_visit
from apis.tiepnhan.CreatePatient import create_patient
from apis.tiepnhan.CreatePatientInsurance import create_patient_insurance
from apis.duoc.ApproveVoucherIn import Approve_Voucher_In
from data.Urls import URLS
from supports import support
import concurrent.futures


def save_medical_examination(json_data_visit, auth_header):
    #   auth_header = get_auth_header()
    server_datetime = get_server_datetime()
    #   json_data_visit = create_visit()
    replaced_string_entryId = "27811"
    replace_string_entryId = str(json_data_visit['entry']['entryId'])
    url = URLS.API_SAVE_MEDICAL.replace(replaced_string_entryId, replace_string_entryId)
    print("URL:" + url)
    body = {
        "EntryId": json_data_visit['entry']['entryId'],
        "VisitId": json_data_visit['entry']['visitId'],
        "MedServiceId": json_data_visit['entry']['medServiceId'],
        "WardUnitId": json_data_visit['entry']['wardUnitId'],
        "OnDate": json_data_visit['entry']['onDate'],
        "DxSymptom": "tc",
        "InitialDxICD": "A00",
        "InitialDxText": "Bệnh tả",
        "DxICD": "A00.0",
        "DxText": "Bệnh tả do Vibrio cholerae 01, typ sinh học cholerae CĐ",
        "DxByStaffId": 4451,
        "TxInstruction": 3,
        "CreateOn": support.convert_datetime_string_medical(server_datetime),
        "CreateById": 4451,
        "Status": 8,
        "InsBenefitType": json_data_visit['entry']['insBenefitType'],
        "InsBenefitRatio": json_data_visit['entry']['insBenefitRatio'],
        "PriceId": json_data_visit['entry']['priceId'],
        "QmsNo": json_data_visit['entry']['qmsNo'],
        "TicketId": json_data_visit['entry']['ticketId'],
        "MedRcdNo": "",
        "CreateByWardUnitId": json_data_visit['entry']['createByWardUnitId'],
        "VisitDXList": [
            {
                "IcdCode": "A02.0",
                "ICDReason": None
            }
        ],
        "TxVisit": {
            "OnDate": support.convert_datetime_string_medical(server_datetime),
            "PxDays": 1,
            "CreateByStaffName": None
        },
        "PxItems": [

        ],
        "Service": {
            "ServiceId": json_data_visit['entry']['medServiceId'],
            "Code": "KTMH1",
            "TypeL1": 13,
            "TypeL2": 13,
            "TypeL3": 30,
            "TypeL4": 130,
            "Category": 2,
            "Rank": 1,
            "Unit": "Lần",
            "Description": "Khám Tai Mũi Họng 1",
            "InsServiceName": "Khám Tai mũi họng",
            "Attribute": 1024,
            "NationalCode": "15.1897",
            "Status": 1,
            "InsPrice": 37500.0,
            "Price": 37500.0,
            "PriceId": 1083264,
            "ServiceGroupName": None
        },
        "LabExams": None,
        "CreatedBy": None,
        "ContentHash": f'{replace_string_entryId}|{json_data_visit['entry']['visitId']}|{json_data_visit['entry']['wardUnitId']}|{support.convert_server_time_ddmmyyyhhmm(json_data_visit['entry']['onDate'])}|A00.0|Bệnh tả do Vibrio cholerae 01, typ sinh học cholerae CĐ|4451|3|{support.convert_server_time_ddmmyyyhhmm(support.convert_datetime_string_medical(server_datetime))}|4451||||PendingProcessing|{json_data_visit['entry']['medServiceId']}|80||tc|2|{json_data_visit['entry']['priceId']}|{json_data_visit['entry']['qmsNo']}||',
        "IsPassOnWarning": False
    }
    response = requests.put(url, json=body, headers=auth_header)
    assert response.status_code == 204


def prepare_data_save_drug():
    json_response_get_drug = get_drug()
    auth_header = get_auth_header()
    server_datetime = get_server_datetime()
    json_data_visit = create_visit()
    replaced_string_entryId = "27811"
    replace_string_entryId = str(json_data_visit['entry']['entryId'])
    createOn = support.convert_datetime_string_medical(server_datetime)
    url = URLS.API_SAVE_MEDICAL.replace(replaced_string_entryId, replace_string_entryId)
    print("URL:" + url)
    body = {
        "EntryId": json_data_visit['entry']['entryId'],
        "VisitId": json_data_visit['entry']['visitId'],
        "MedServiceId": json_data_visit['entry']['medServiceId'],
        "WardUnitId": json_data_visit['entry']['wardUnitId'],
        "OnDate": json_data_visit['entry']['onDate'],
        "DxSymptom": "tc",
        "InitialDxICD": "A00",
        "InitialDxText": "Bệnh tả",
        "DxICD": "A00.0",
        "DxText": "Bệnh tả do Vibrio cholerae 01, typ sinh học cholerae CĐ",
        "DxByStaffId": 4451,
        "TxInstruction": 2,
        "CreateOn": createOn,
        "CreateById": 4451,
        "Status": 8,
        "InsBenefitType": json_data_visit['entry']['insBenefitType'],
        "InsBenefitRatio": json_data_visit['entry']['insBenefitRatio'],
        "PriceId": json_data_visit['entry']['priceId'],
        "QmsNo": json_data_visit['entry']['qmsNo'],
        "TicketId": json_data_visit['entry']['ticketId'],
        "MedRcdNo": "",
        "CreateByWardUnitId": json_data_visit['entry']['createByWardUnitId'],
        "VisitDXList": [
            {
                "IcdCode": "A02.0",
                "ICDReason": None
            }
        ],
        "TxVisit": {
            "OnDate": createOn,
            "PxDays": 1,
            "CreateByStaffName": None
        },
        "PxItems": [

        ],
        "Service": {
            "ServiceId": json_data_visit['entry']['medServiceId'],
            "Code": "KTMH1",
            "TypeL1": 13,
            "TypeL2": 13,
            "TypeL3": 30,
            "TypeL4": 130,
            "Category": 2,
            "Rank": 1,
            "Unit": "Lần",
            "Description": "Khám Tai Mũi Họng 1",
            "InsServiceName": "Khám Tai mũi họng",
            "Attribute": 1024,
            "NationalCode": "15.1897",
            "Status": 8,
            "InsPrice": 37500.0,
            "Price": 37500.0,
            "PriceId": 1083264,
            "ServiceGroupName": None
        },
        "LabExams": None,
        "CreatedBy": None,
        "ContentHash": f'{replace_string_entryId}|{json_data_visit['entry']['visitId']}|{json_data_visit['entry']['wardUnitId']}|{support.convert_server_time_ddmmyyyhhmm(json_data_visit['entry']['onDate'])}|A00.0|Bệnh tả do Vibrio cholerae 01, typ sinh học cholerae CĐ|4451|3|{support.convert_server_time_ddmmyyyhhmm(support.convert_datetime_string_medical(server_datetime))}|4451||||PendingProcessing|{json_data_visit['entry']['medServiceId']}|80||tc|2|{json_data_visit['entry']['priceId']}|{json_data_visit['entry']['qmsNo']}||',
        "IsPassOnWarning": False
    }
    for item in json_response_get_drug:
        drug = item['productItem']
        px_item = {
            "ItemId": drug['itemId'],
            "ItemName": drug['name'],
            "ItemUnit": drug['unit'],
            "Qty": 1.0,
            "Notes": "",
            "UseNotes": "CÁCH DÙNG UỐNG",
            "UseWeekDay": 127,
            "UseDays": 1,
            "Attribute": 5,
            "IsPaid": False,
            "StoreId": item['invNowInStore']['storeId'],
            "InvSource": item['invNowInStore']['invSource'],
            "MedStrenght": drug['medStrenght'],
            "MedUseRoute": "Uống",
            "MedItem": {
                "ItemId": drug['itemId'],
                "InsIndex": drug['insIndex'],
                "Code": drug['code'],
                "Type": drug['type'],
                "ItemCat": drug['itemCat'],
                "ATC": drug['atc'],
                "Name": drug['name'],
                "Description": drug['description'],
                "NtlCode": drug['ntlCode'],
                "NtlName": drug['ntlName'],
                "Unit": drug['unit'],
                "PkgUnit": drug['pkgUnit'],
                "PkgUnitText": drug['pkgUnitText'],
                "UsageUnit": drug['usageUnit'],
                "PPP": drug['ppp'],
                "PPU": drug['ppu'],
                "MedAI": drug['medAI'],
                "MedUseRoute": drug['medUseRoute'],
                "MedTherapyRoot": drug['medTherapyRoot'],
                "MedDosageForm": drug['medDosageForm'],
                "MedStrenght": drug['medStrenght'],
                "MedGbCode": drug['medGbCode'],
                "RegNo": drug['regNo'],
                "MfrCode": drug['mfrCode'],
                "MfrName": drug['mfrName'],
                "MfrAddr": drug['mfrAddr'],
                "MfrCountry": drug['mfrCountry'],
                "InsCode": drug['insCode'],
                "InsName": drug['insName'],
                "InsPayRatio1": drug['insPayRatio1'],
                "Price": drug['price'],
                "Attribute": drug['attribute'],
                "DrugWarnings": drug['drugWarnings'],
                "StockCritLevel": drug['stockCritLevel'],
                "Status": drug['status'],
                "BidGroupCode": drug['bidGroupCode'],
                "BidPackageCode": drug['bidPackageCode'],
                "BidDocNo": drug['bidDocNo'],
                "SysFullName": drug['sysFullName'],
                "ProcessingMethodCode": drug['processingMethodCode'],
                "Note": drug['note'],
                "FullName": f"{drug['medAI']} ({drug['name']}), {drug['medStrenght']}",
                "IsInInsCat": True,
                "Remaining": item['qtyAvailables'],
                "InsPrice": item['amt'],
                "AttributeDisplay": "Thuộc danh mục bảo hiểm chi",
                "IsLocalPharmacy": False,
                "PlanCoefficient": 0.0,
                "PurchaseName": None
            },
            "Code": None,
            "InsBenefitType": None,
            "OnVisit": None,
            "WardAdmId": None,
            "TxVisitMedReturnId": None,
            "ApproveQty": None,
            "Dosage": ""
        }
        body['PxItems'].append(px_item)
        print("BODY:" + json.dumps(body))
        #        response = requests.put(url, json=body, headers=auth_header)
        #        assert response.status_code == 204
        return url, body, auth_header


def prepare_data_thread(count):
    result = []
    for i in range(count):
        url, body, auth_header = prepare_data_save_drug()
        result.append((url, body, auth_header))
    return result


def save_drug(url, body, auth_header):
    start_time = time.time()
    response = requests.put(url=url, json=body, headers=auth_header)
    end_time = time.time()
    print(f'START_TIME: {start_time} END_TIME:{end_time}')
    return response


@pytest.mark.parametrize("count", [
    2,
    3,
    4
])
def test_save_drugs_thread(count):
    Approve_Voucher_In()
    results_data = prepare_data_thread(count)
    urls_bodies_auth_headers = [(url, body, auth_header) for url, body, auth_header in results_data]
    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as executor:
        futures = [
            executor.submit(save_drug, url, body, auth_header)
            for url, body, auth_header in urls_bodies_auth_headers
        ]
    future_results = []
    for i, future in enumerate(concurrent.futures.as_completed(futures)):
        try:
            response = future.result()
            status_code = response.status_code
            print(f'FUTURE {i} STATUS_CODE: {status_code}')
            future_results.append(status_code)
        except Exception as e:
            print(f'Error: {e}')
            future_results.append(None)
    if future_results:
        print(f'DANH SÁCH TRẠNG THÁI {future_results}')
        count_204 = sum(1 for result in future_results if result == 204)
        assert count_204 == 1, f'Expected exactly one result with status code 204, but found {count_204}'


def test_save_drug_normal():
    url, body, auth_header = prepare_data_save_drug()
    response = requests.put(url=url, json=body, headers=auth_header)
    assert response.status_code == 204


''' response_TxVisits = get_TxVisits_EntryID(json_data_visit, auth_header)
 txVisitId = response_TxVisits.json()['txVisitId']
 body['TxVisit'] = {
     "TxVisitId": txVisitId,
     "Type": 1,
     "OnDate": body['CreateOn'],
     "PxDays": 1,
     "Attribute": 2,
     "VisitEntryId": entryId,
     "CreateById": 4451,
     "CreateOn": support.convert_datetime_string_medical(get_server_datetime()),
     "CreateByStaffName": None
 }
 response = requests.put(url=url, json=body, headers=auth_header)
 assert response.status_code == 204'''
