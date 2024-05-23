import pytest
import requests
from data.Urls import URLS
from apis.config import get_auth_header


#@pytest.fixture(scope="session")
def get_server_datetime():
    auth_header = get_auth_header()
    response = requests.get(URLS.API_CURRENT_SERVER_DATETIME, headers=auth_header)
    json_data = response.json()
    print(json_data)
    assert response.status_code == 200
    return json_data


def test_get_server_datetime():
    time = get_server_datetime()
    print(time)
