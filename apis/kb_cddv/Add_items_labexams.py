import pytest
import requests

from apis.CurrentServerDateTime import get_server_datetime
from apis.config import get_auth_header
from data.Urls import URLS
from apis.tiepnhan.Create_Visit import create_visit
from supports import support


def test_add_items_to_labexams():
    auth_header = get_auth_header()
    json_data_visit = create_visit()
    server_datetime = get_server_datetime()
    onDate = support.convert_datetime_string_medical(server_datetime)
    url = URLS.API_ADD_ITEMS_TO_LABEXAMS
    body = {
        "PatientId": json_data_visit['patientId'],
        "RefNo": "Re",
        "OnDate": onDate,
        "LabReqById": 4451,
        "LabReqNotes": "",
        "DxICD": "A00",
        "DxText": "Bệnh tả",
        "Attribute": 1,
        "FrVisitEntryId": json_data_visit['entry']['entryId'],
        "CreateOn": server_datetime,
        "CreateById": 4451,
        "Status": 1,
        "WardUnitId": 36,
        "ServiceName": None,
        "LabExamItems": [
            {
                "LabExId": 1,
                "MedServiceId": 389,
                "PriceId": 1084744,
                "InsBenefitType": json_data_visit['insBenefitType'],
                "InsBenefitRatio": json_data_visit['insBenefitRatio'],
                "InsCardId": json_data_visit['insCardId'],
                "Qty": 1.0,
                "Price": 68300.0,
                "InsPrice": 68300.0,
                "InsPriceRatio": 100,
                "Amt": 68300.0,
                "Attribute": 1,
                "ByProviderId": 552,
                "DiscAmtSeq": 0,
                "MedServiceTypeL0": 2,
                "MedServiceTypeL2": 6,
                "MedServiceTypeL3": 25,
                "NonSubclinical": False,
                "TypeL0Code": None,
                "ByProviderCode": "XQ1",
                "ByProviderName": "Phòng X quang",
                "ServiceGroupName": "Chẩn đoán hình ảnh",
                "ServiceTypeL3Name": "X-Quang",
                "ServiceCode": "xq08",
                "ServiceName": "Chụp Xquang Chausse III",
                "InsBenefitTypeName": "BHYT",
                "ReqDate": None,
                "AttrString": "Chờ thanh toán",
                "PaidAttrString": "Chờ thanh toán",
                "ServiceTypeOrderIndex": 0,
                "MedItemType": 1,
                "MedItem": None,
                "Checked": None,
                "OnDate": onDate,
                "TotalInvoiceAmtRound": None,
                "TotalReceiptAmtRound": None,
                "PtAmt": 0.0,
                "PtAmtRound": 0.0,
                "PtAmtPaid": 0.0,
                "PtCoPayAmt": 13660.0,
                "PtCoPayAmtRound": 0.0,
                "InsAmt": 54640.0,
                "InsAmtRound": 0.0,
                "DiscAmt": 0.0,
                "ReqBy": None
            },
            {
                "LabExId": 1,
                "MedServiceId": 3962,
                "PriceId": 1081529,
                "InsBenefitType": json_data_visit['insBenefitType'],
                "InsBenefitRatio": json_data_visit['insBenefitRatio'],
                "InsCardId": json_data_visit['insCardId'],
                "Qty": 1.0,
                "Price": 12200.0,
                "InsPrice": 12200.0,
                "InsPriceRatio": 100,
                "Amt": 12200.0,
                "Attribute": 1,
                "ByProviderId": 592,
                "DiscAmtSeq": 0,
                "MedServiceTypeL0": 18,
                "MedServiceTypeL2": 17,
                "MedServiceTypeL3": 51,
                "NonSubclinical": False,
                "TypeL0Code": None,
                "ByProviderCode": "KCC",
                "ByProviderName": "Khoa Cấp cứu",
                "ServiceGroupName": "Thủ thuật",
                "ServiceTypeL3Name": "Thủ thuật loại 3 (Giá mới)",
                "ServiceCode": "tt3m19",
                "ServiceName": "Hút đờm hầu họng",
                "InsBenefitTypeName": "BHYT",
                "ReqDate": None,
                "AttrString": "Chờ thanh toán",
                "PaidAttrString": "Chờ thanh toán",
                "ServiceTypeOrderIndex": 0,
                "MedItemType": 1,
                "MedItem": None,
                "Checked": None,
                "OnDate": onDate,
                "TotalInvoiceAmtRound": None,
                "TotalReceiptAmtRound": None,
                "PtAmt": 0.0,
                "PtAmtRound": 0.0,
                "PtAmtPaid": 0.0,
                "PtCoPayAmt": 2440.0,
                "PtCoPayAmtRound": 0.0,
                "InsAmt": 9760.0,
                "InsAmtRound": 0.0,
                "DiscAmt": 0.0,
                "ReqBy": None
            }
        ],
        "ItemI0": {
            "LabExId": 1,
            "MedServiceId": 389,
            "PriceId": 1084744,
            "InsBenefitType": json_data_visit['insBenefitType'],
            "InsBenefitRatio": json_data_visit['insBenefitRatio'],
            "InsCardId": json_data_visit['insCardId'],
            "Qty": 1.0,
            "Price": 68300.0,
            "InsPrice": 68300.0,
            "InsPriceRatio": 100,
            "Amt": 68300.0,
            "Attribute": 1,
            "ByProviderId": 552,
            "DiscAmtSeq": 0,
            "MedServiceTypeL0": 2,
            "MedServiceTypeL2": 6,
            "MedServiceTypeL3": 25,
            "NonSubclinical": False,
            "TypeL0Code": None,
            "ByProviderCode": "XQ1",
            "ByProviderName": "Phòng X quang",
            "ServiceGroupName": "Chẩn đoán hình ảnh",
            "ServiceTypeL3Name": "X-Quang",
            "ServiceCode": "xq08",
            "ServiceName": "Chụp Xquang Chausse III",
            "InsBenefitTypeName": "BHYT",
            "ReqDate": None,
            "AttrString": "Chờ thanh toán",
            "PaidAttrString": "Chờ thanh toán",
            "ServiceTypeOrderIndex": 0,
            "MedItemType": 1,
            "MedItem": None,
            "Checked": None,
            "OnDate": onDate,
            "TotalInvoiceAmtRound": None,
            "TotalReceiptAmtRound": None,
            "PtAmt": 0.0,
            "PtAmtRound": 0.0,
            "PtAmtPaid": 0.0,
            "PtCoPayAmt": 13660.0,
            "PtCoPayAmtRound": 0.0,
            "InsAmt": 54640.0,
            "InsAmtRound": 0.0,
            "DiscAmt": 0.0,
            "ReqBy": None
        },
        "FullAddress": None
    }
    response = requests.post(url=url, json=body, headers=auth_header)
    assert response.status_code == 201
    json_data = response.json()
    print("URL: ", url)
    print(json_data)
    return response
