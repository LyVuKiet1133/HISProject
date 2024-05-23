import time

import requests
import pytest
from apis.config import get_auth_header
from data.Urls import URLS
from data.Patients import Patient
from supports import support
import concurrent.futures


# @pytest.fixture(scope='session')
def create_patient():
    start_time = time.time()
    auth_header = get_auth_header()
    patient = Patient.random_patient()
    body = {
        "PatientCode": "SimulatedCode",
        "FullPatientCode": "SimulatedCode",
        "FirstName": patient.first_name,
        "LastName": patient.last_name,
        "Dob": "1990-01-01T00:00:00+07:00",
        "Gender": 1,
        "IdCardNo": "",
        "MobileNo": "",
        "Nationality": "VN",
        "Ethnic": "01",
        "Country": "VN",
        "City": "75",
        "District": "732",
        "Ward": "26095",
        "Address": patient.address,
        "Occupation": 10,
        "EmployerName": "",
        "EmployerAddr": "",
        "TaxCode": "",
        "RelativeName": "",
        "RelativeAddr": "",
        "RelativePhone": "",
        "RelativeType": 0,
        "Status": 1,
        "FullName": patient.first_name + " " + patient.last_name,
        "FullAddress": "Khu phố Suối Tre"
    }
    response = requests.post(URLS.API_CREATE_PATIENT, json=body, headers=auth_header)
    print(response.json())
    assert response.status_code == 201
    json_data = response.json()
    patientId = json_data['patientId']
    nationality = json_data['nationality']
    city = json_data['city']
    district = json_data['district']
    ward = json_data['ward']
    address = json_data['address']
    srcFullName = json_data['srcFullName']
    ethnic = json_data['ethnic']
    occupation = json_data['occupation']
    dob = json_data['dob']
    '''assert patientId is not None
    patient = Patient(patientId=patientId, nationality=nationality, city=city, district=district,
                      ward=ward, address=address, srcFullName=srcFullName, ethnic=ethnic, occupation=occupation,
                      dob=dob)'''
    end_time = time.time()
    print(f'Request sent at: {start_time}, Response received at: {end_time}')
    return json_data

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Lên lịch hai yêu cầu POST đồng thời
        futures = [executor.submit(create_patient) for _ in range(2)]

        # Chờ và lấy kết quả từ các Future
        for future in concurrent.futures.as_completed(futures):
            try:
                status_code, patient = future.result()
                print(f'Status Code: {status_code}')
                print(f'Patient ID: {patient.patientId}')
            except Exception as e:
                print(f'Generated an exception: {e}')

if __name__ == "__main__":
    main()
