import pytest
from apis.config import get_auth_header
from apis.kb_ketoa.get_TxVisits import get_TxVisits_EntryID
from data.Urls import URLS
import requests


def delete_drug_tt(json_data_visit, auth_header):
    response_TxVisitMeds = get_TxVisitMeds(json_data_visit, auth_header)
    UpdateVouOutRX(response_TxVisitMeds.json(), auth_header)
    txVisitMeds_list = [str(data['id']) for data in response_TxVisitMeds.json()]
    replaced_txVisitMeds = '131522,131523'
    txVisitMeds_string = ",".join(txVisitMeds_list)
    url = URLS.API_DELETE_DUG_TT.replace(replaced_txVisitMeds, txVisitMeds_string)
    print("URL: " + url)
    response = requests.delete(url=url, headers=auth_header)
    assert response.status_code == 200
    print(f'Message: Xóa thành công')
    return response


def get_TxVisitMeds(json_data_visit, auth_header):
    response_TxVisit = get_TxVisits_EntryID(json_data_visit, auth_header)
    txVisitId = response_TxVisit.json()['txVisitId']
    replaced_txVisitId = '41088'
    url = URLS.API_GET_TXVISITMEDS.replace(replaced_txVisitId, str(txVisitId))
    response = requests.get(url=url, headers=auth_header)
    assert response.status_code == 200
    print(f"RESPONSE: {response.json()}")
    return response


def UpdateVouOutRX(json_response_TxVisitMeds, auth_header):
    replaced_StoreId = '155'
    replaced_TxVisitId = '41093'
    body = []
    url = URLS.API_UPDATE_VOU_OUT_RX.replace(replaced_TxVisitId, str(json_response_TxVisitMeds[0]['txVisitId'])).replace(
        replaced_StoreId, str(json_response_TxVisitMeds[0]['storeId']))
    for data in json_response_TxVisitMeds:
        body_item = {
            "TxVisitMedId": data['id'],
            "ItemId": data['itemId'],
            "ItemSource": 1,
            "Qty": 0.0,
            "Amt": data['amt']
        }
        body.append(body_item)
    response = requests.post(url=url, json=body, headers=auth_header)
    assert response.status_code == 200
    print(f'URL: {url}')
    print(f'BODY: {body}')
    return response
