class URLS():
    url_1081 = 'http://192.168.110.8:1081'
    url_1082 = 'http://192.168.110.8:1082'
    url_1083 = 'http://192.168.110.8:1083'
    API_LOGIN = f'{url_1081}/Users/Login/ducpn?pwd=202cb962ac59075b964b07152d234b70'
    API_CREATE_PATIENT = f'{url_1083}/Patients'
    API_CREATE_PATIENT_INSURANCE = f'{url_1083}/PatientInsurances/?dateOfBirth='
    API_CURRENT_SERVER_DATETIME = f'{url_1082}/Masters/CurrentServerDateTime'
    API_CREATE_VISIT = f'{url_1083}/Visits/?visitOn=20240511125645&noSetProcessingPending=False&isPassCreatePaymentTicket=False&isPassVisitOnSameDay=False'
