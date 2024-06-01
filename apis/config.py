import pytest
import requests
from data.Urls import URLS
import time
import concurrent.futures


# @pytest.fixture(scope='session')
def get_token():
    response = requests.get(URLS.API_LOGIN)
    assert response.status_code == 200
    json_data = response.json()
    token = json_data['token']
    return token


# @pytest.fixture(scope='session')
def get_auth_header():
    token = get_token()
    return {'Authorization': f'Bearer {token}'}


def post_api(url, body, auth_header):
    start_time = time.time()
    response = requests.post(url=url, json=body, headers=auth_header)
    end_time = time.time()
    print(f'START_TIME: {start_time} END_TIME:{end_time}')
    return response


def put_api(url, body, auth_header):
    start_time = time.time()
    response = requests.put(url=url, json=body, headers=auth_header)
    end_time = time.time()
    print(f'START_TIME: {start_time} END_TIME:{end_time}')
    return response


def get_api(url, auth_header):
    start_time = time.time()
    response = requests.get(url=url, headers=auth_header)
    end_time = time.time()
    print(f'START_TIME: {start_time} END_TIME:{end_time}')
    return response


def delete_api(url, auth_header):
    start_time = time.time()
    response = requests.put(url=url, headers=auth_header)
    end_time = time.time()
    print(f'START_TIME: {start_time} END_TIME:{end_time}')
    return response


def simultaneously(count, urls_bodies_auth_headers, method):
    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as executor:
        if method == 'post':
            futures = [
                executor.submit(post_api, url, body, auth_header)
                for url, body, auth_header in urls_bodies_auth_headers
            ]
        elif method == 'put':
            futures = [
                executor.submit(put_api, url, body, auth_header)
                for url, body, auth_header in urls_bodies_auth_headers
            ]
        elif method == 'delete':
            futures = [
                executor.submit(delete_api, url, auth_header)
                for url, _, auth_header in urls_bodies_auth_headers
            ]
    future_results_status = []
    for i, future in enumerate(concurrent.futures.as_completed(futures)):
        try:
            response = future.result()
            status_code = response.status_code
            print(f'FUTURE {i} STATUS_CODE: {status_code}')
            future_results_status.append(status_code)
        except Exception as e:
            print(f'Error: {e}')
            future_results_status.append(None)
    if future_results_status:
        print(f'Status_List: {future_results_status}')
    return future_results_status
#        count_204 = sum(1 for result in future_results if result == 204)
#        assert count_204 == 1, f'Expected exactly one result with status code 204, but found {count_204}'
