import pytest
import requests
from data.Urls import URLS


#@pytest.fixture(scope='session')
def get_token():
    response = requests.get(URLS.API_LOGIN)
    assert response.status_code == 200
    json_data = response.json()
    token = json_data['token']
    return token


#@pytest.fixture(scope='session')
def get_auth_header():
    token = get_token()
    return {'Authorization': f'Bearer {token}'}
