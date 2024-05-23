import pytest
from apis.config import get_auth_header
from data.Urls import URLS
import requests
import json


# @pytest.fixture(scope='session')
def get_drug():
    auth_header = get_auth_header()
    url = URLS.API_GET_DRUG
    body = {
        "StoreIds": [
            28
        ],
        "InvSources": None,
        "LotIds": None,
        "ItemIds": [
            11272
        ],
        "IgnoreItemIds": None,
        "VouStatus": None,
        "IgnoreStoreId": False,
        "IgnoreLotId": False,
        "IgnoreInvSource": False,
        "ItemCatIds": None,
        "ItemTypes": None,
        "BidIds": None,
        "ProviderIds": None,
        "IgnoreItemCatIds": None,
        "TakeOnlyGroupInStoreHospital": None,
        "TakeOnlyItemIns": None
    }
    response = requests.post(url, json=body, headers=auth_header)
    assert response.status_code == 200
    json_response_get_drug = response.json()

    '''if response.status_code == 200:
        json_response_get_drug = response.json()
        with open('getDrugs.json', 'w', encoding='utf-8') as f:
            json.dump(json_response_get_drug, f, ensure_ascii=False, indent=4)
    else:
        print(f"Failed to get response from API . Status code: {response.status_code}")'''
    return json_response_get_drug


def test_get_drug():
    response = get_drug()
    assert response.status_code == 200
