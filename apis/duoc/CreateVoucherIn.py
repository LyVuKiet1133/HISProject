import requests

from data.Urls import URLS
from apis.config import get_auth_header
from apis.CurrentServerDateTime import get_server_datetime
from supports.support import convert_datetime_string_medical
from apis.duoc.CreateVoucherOut import Create_Voucher_Out
import pytest


def Create_Voucher_In():
    auth_header = get_auth_header()
    response_voucher_out = Create_Voucher_Out()
    json_voucher_out = response_voucher_out.json()
    onDate = json_voucher_out['voucher']['onDate']
    createOn = json_voucher_out['voucher']['createOn']
    refVoucherId = json_voucher_out['voucher']['voucherId']
    voucherOutInvs = json_voucher_out['voucherOutInvs']
    RefVouOutInvIds = [item['id'] for item in voucherOutInvs]
    url = URLS.API_CREATE_VOUCHER_IN
    body = {
        "Voucher": {
            "Type": 20,
            "OnDate": convert_datetime_string_medical(onDate),
            "Description": " ",
            "StoreId": 28,
            "TxVisitId": None,
            "VisitEntryId": None,
            "RefVoucherId": refVoucherId,
            "RefStoreId": 24,
            "InvSource": 1,
            "CreateById": 4451,
            "CreateOn": convert_datetime_string_medical(createOn),
            "InvStatus": 0,
            "InvStatusDescription": None,
            "ProcStatusDescription": None,
            "CustomerName": None,
            "InvoiceText": None
        },
        "VoucherIns": [
            {
                "Price": 1000.000,
                "VatPerc": 0,
                "VatAmt": 1000.00,
                "RefVouOutInvId": 191155,
                "LotId": 21985,
                "ItemId": 11272,
                "ItemSource": 1,
                "Qty": 1.000,
                "Amt": 1000.00,
                "Status": 0
            },
            {
                "Price": 1000.000,
                "VatPerc": 0,
                "VatAmt": 1000.00,
                "RefVouOutInvId": 191156,
                "LotId": 21986,
                "ItemId": 11280,
                "ItemSource": 1,
                "Qty": 1.000,
                "Amt": 1000.00,
                "Status": 0
            }
        ],
        "ItemLots": [],
        "ItemPrices": [],
        "RevocationVoucherIns": None
    }
    for i, ref_id in enumerate(RefVouOutInvIds):
        if i < len(body['VoucherIns']):
            body['VoucherIns'][i]['RefVouOutInvId'] = ref_id
    response = requests.post(url=url, json=body, headers=auth_header)
    print("URL: ", url)
    assert response.status_code == 200
    print("RESPONSE: ", response.json())
    return response


def test_create_voucher_in():
    Create_Voucher_In()
