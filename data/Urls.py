class URLS():
    url_1081 = 'http://192.168.110.16:1081'
    url_1082 = 'http://192.168.110.16:1082'
    url_1083 = 'http://192.168.110.16:1083'
    url_1084 = 'http://192.168.110.16:1084'
    url_1086 = 'http://192.168.110.16:1086'

    API_LOGIN = f'{url_1081}/Users/Login/kietlv?pwd=202cb962ac59075b964b07152d234b70'
    # tiếp nhận
    API_CREATE_PATIENT = f'{url_1083}/Patients'
    API_CREATE_PATIENT_INSURANCE = f'{url_1083}/PatientInsurances/?dateOfBirth='
    API_CURRENT_SERVER_DATETIME = f'{url_1082}/Masters/CurrentServerDateTime'
    API_CREATE_VISIT = f'{url_1083}/Visits/?visitOn=20240511125645&noSetProcessingPending=False&isPassCreatePaymentTicket=False&isPassVisitOnSameDay=False'
    # khám bệnh
    API_SAVE_MEDICAL = f'{url_1083}/VisitEntries/27811?forceNull=True&ptFullAddress=Khu+Ph%E1%BB%91+Su%E1%BB%91i+Tre%2C+Ph%C6%B0%E1%BB%9Dng+Su%E1%BB%91i+Tre%2C+Th%C3%A0nh+ph%E1%BB%91+Long+Kh%C3%A1nh%2C+T%E1%BB%89nh+%C4%90%E1%BB%93ng+Nai&isPassMedAIValid=&isPassMedAIValidOtherPx=False&isPassInteraction=False&isRemoveAllConsulation=True&isUpdateEntryValOnly=False&isBackupStatus=True'
    # Kê thuốc
    API_GET_DRUG = f'{url_1086}/InvNowAvailables/GetInventoriesForBooking/?isInsurrance=True&name=&medAI=&fullName=&LengthLimit=20&fullNameOrCode=False&attribute=&isNoLoadItems=False'
    API_TxVisitMeds_TxVisitIds = f'{url_1084}/TxVisitMeds/TxVisitIds'
    API_TxVisits_EntryID = f'{url_1084}/TxVisits/28412?attribute=2'
    API_Prescriptions_TxVisitIds = f'{url_1084}/Prescriptions/TxVisitIds'
    API_TxVisitMeds_Entries = f'{url_1084}/TxVisitMeds/Entries'
    # Lưu DV:
    API_ADD_ITEMS_TO_LABEXAMS = f'{url_1084}/LabExams/AddWithItems?ptFullAddress=Khu+Ph%E1%BB%91+Su%E1%BB%91i+Tre%2C+Ph%C6%B0%E1%BB%9Dng+Su%E1%BB%91i+Tre%2C+Th%C3%A0nh+ph%E1%BB%91+Long+Kh%C3%A1nh%2C+T%E1%BB%89nh+%C4%90%E1%BB%93ng+Nai'
    API_LabExamItems = f'{url_1084}/LabExamItems/LabExamIds?ExcludedAttribute=&serviceTypeL0=&isLoadDelete=False'
    API_AVAIlABLE_DRUG_STORE = f'{url_1086}/InvNowAvailables/GetInventoriesForBooking/?isInsurrance=True&name=&medAI=&fullName=&LengthLimit=20&fullNameOrCode=True&attribute=&isNoLoadItems=True'
    # Dược
    API_VERIFY_STORE_CHECKVOUOUT = f'{url_1086}/InvNowInStores/VerifyInStoreCheckVouOut?storeId=24&withBys=11'
    API_CREATE_VOUCHER_OUT = f'{url_1086}/Vouchers/CreateVoucherOut/3?withBy=11'
    API_CREATE_VOUCHER_IN = f'{url_1086}/Vouchers/CreateAndSaveVoucherIn'
    API_APPROVE_VOUCHER_IN = f'{url_1086}/Vouchers/ApproveVouIn/3'
    # Tủ trực khám bệnh:
    API_ADD_TXVISIT_MEDLIST = f'{url_1084}/TxVisitMeds/AddTxVisitMedList'
    API_GET_DRUG_TUTRUC = f'{url_1086}/InvNowInStores/FindInventory/7?storeids=155&CheckInventory=7&IsViewSummary=True'
    API_CONFIRM_CREATE_VOUCHER_OUT = f'{url_1086}/InvNowInStores/ConfirmAndCreateVoucherOut/3?isCheckExp=True'
    API_DELETE_DUG_TT = f'{url_1084}/TxVisitMeds/131522,131523'
    API_GET_TXVISITMEDS = f'{url_1084}/TxVisitMeds/41088'
    API_UPDATE_VOU_OUT_RX = f'{url_1086}/Vouchers/UpdateVouOutRX/3?StoreId=155&TxVisitId=41093&withBy=0'