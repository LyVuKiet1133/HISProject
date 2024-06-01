import requests

from data.Urls import URLS
from apis.config import get_auth_header
from apis.CurrentServerDateTime import get_server_datetime
from supports.support import convert_datetime_string_medical
from apis.duoc.CreateVoucherIn import Create_Voucher_In
import pytest


def Approve_Voucher_In():
    auth_header = get_auth_header()
    response_voucher_in = Create_Voucher_In()
    json_voucher_in = response_voucher_in.json()
    voucherId = json_voucher_in['voucher']['voucherId']
    voucherNo = json_voucher_in['voucher']['voucherNo']
    type = json_voucher_in['voucher']['type']
    onDate = json_voucher_in['voucher']['onDate']
    storeId = json_voucher_in['voucher']['storeId']
    refVoucherId = json_voucher_in['voucher']['refVoucherId']
    refStoreId = json_voucher_in['voucher']['refStoreId']
    invSource = json_voucher_in['voucher']['invSource']
    createOn = json_voucher_in['voucher']['createOn']

    url = URLS.API_APPROVE_VOUCHER_IN
    body = {
        "VoucherId": voucherId,
        "VoucherNo": voucherNo,
        "Type": type,
        "OnDate": onDate,
        "Description": "",
        "StoreId": storeId,
        "TxVisitId": None,
        "VisitEntryId": None,
        "RefVoucherId": refVoucherId,
        "RefStoreId": refStoreId,
        "InvSource": invSource,
        "InvoiceNo": "",
        "InvoiceCode": "",
        "DeliverName": "",
        "DeliverPhone": "",
        "CreateById": 4451,
        "CreateOn": createOn,
        "InvStatus": 2,
        "InvStatusDescription": "Đã cập nhật tồn kho",
        "ProcStatusDescription": None,
        "CustomerName": None,
        "InvoiceText": ""
    }
    response = requests.put(url=url, json=body, headers=auth_header)
    print("URL: ", url)
    assert response.status_code == 204
    print("RESPONSE: ", response)
    return response


def test_approve_voucher_in():
    Approve_Voucher_In()
