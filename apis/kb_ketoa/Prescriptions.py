from data.Urls import URLS
import pytest
import requests
from apis.config import get_auth_header


def post_Prescriptions_TxVisitIds(TxVisitIds, auth_header):
    url = URLS.API_Prescriptions_TxVisitIds
    body = []
    body = body.append(TxVisitIds)
    response = requests.post(url=url, json=body, headers=auth_header)
    return response
