from data.Urls import URLS
import pytest
import requests
from apis.config import get_auth_header


def post_TxVisitMeds_TxVisitIds(TxVisitIds, auth_header):
    url = URLS.API_TxVisitMeds_TxVisitIds
    body = []
    body = body.append(TxVisitIds)
    response = requests.post(url=url, json=body, headers=auth_header)
    return response
