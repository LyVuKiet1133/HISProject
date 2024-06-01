import time

import pytest

from apis.CurrentServerDateTime import get_server_datetime
from apis.config import put_api, simultaneously, get_auth_header
from apis.kb_tutruc.AddTxVisitMedList import Add_TxVisit_MedList
from apis.kb_tutruc.Delete_Drug_TT import delete_drug_tt
from data.Urls import URLS
import requests


def confirm_create_voucher_out():
    auth_header = get_auth_header()
    response_medilist, json_data_visit = Add_TxVisit_MedList()
    json_data_medilist = response_medilist.json()
    OnDate = get_server_datetime()
    CreateOn = get_server_datetime()
    txVisitId = json_data_medilist[0]['txVisitId']
    storeId = json_data_medilist[0]['storeId']
    url = URLS.API_CONFIRM_CREATE_VOUCHER_OUT

    bd = {
        "imsGetInvNowWithBy": None,
        "Voucher": {
            "CreateBy": None,
            "VoucherExt": None,
            "voucher": {
                "Type": 60,
                "OnDate": OnDate,
                "StoreId": storeId,
                "TxVisitId": txVisitId,
                "VisitEntryId": None,
                "InvSource": 0,
                "CreateById": 4451,
                "CreateOn": CreateOn,
                "InvStatus": 0,
                "InvStatusDescription": None,
                "ProcStatusDescription": None,
                "CustomerName": None,
                "InvoiceText": None
            },
            "ImsSource": None,
            "Type": 60,
            "OnDate": OnDate,
            "StoreId": storeId,
            "TxVisitId": txVisitId,
            "VisitEntryId": None,
            "InvSource": 0,
            "CreateById": 4451,
            "CreateOn": CreateOn,
            "InvStatus": 0,
            "InvStatusDescription": None,
            "ProcStatusDescription": None,
            "CustomerName": None,
            "InvoiceText": None
        },
        "voucherOuts": None,
        "voucherOutInvs": None,
        "InvRequests": [],
        "VoucherExt": None,
        "VoucherOutExts": None,
        "RequestByInventory": None
    }
    body = create_invRequest_body(json_data_medilist, bd)
    print(f'Body: {body}')
    return url, body, auth_header


def prepare_data(count):
    result = []
    for i in range(count):
        url, body, auth_header = confirm_create_voucher_out()
        result.append((url, body, auth_header))
    return result


def create_invRequest_item(json_data_medilist):
    item = {
        "StoreId": json_data_medilist['storeId'],
        "ItemId": json_data_medilist['itemId'],
        "Qty": json_data_medilist['qty'],
        "QtyInvNow": None,
        "Amt": json_data_medilist['amt'],
        "InvSource": json_data_medilist['invSource'],
        "IsReqToStoreIns": None,
        "Status": None,
        "InvOuts": None,
        "Price": None,
        "InsPrice": None,
        "TxVisitMedId": json_data_medilist['id']
    }
    return item


def create_invRequest_body(json_data_medilist, body):
    for data in json_data_medilist:
        item = create_invRequest_item(data)
        body['InvRequests'].append(item)
    return body


@pytest.mark.parametrize('count', [
    2
])
def test_save_drug_tt_simultaneously(count):
    results = prepare_data(count)
    urls_bodies_auth_headers = [(url, body, auth_header) for url, body, auth_header in results]
    future_results_status = simultaneously(count, urls_bodies_auth_headers, 'post')
    count_200 = sum(1 for result_status in future_results_status if result_status == 200)
    assert count_200 == 1, f'Expected exactly one result with status code 200, but found {count_200}'
