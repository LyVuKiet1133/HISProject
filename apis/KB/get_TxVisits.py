import pytest
from apis.config import get_auth_header
from data.Urls import URLS
import requests


def get_TxVisits_EntryID(json_data_visit, auth_header):
    replaced_string_entryId = "28412"
    replace_string_entryId = str(json_data_visit['entry']['entryId'])
    url = URLS.API_TxVisits_EntryID.replace(replaced_string_entryId, replace_string_entryId)
    response = requests.get(url=url, headers=auth_header)
    return response
