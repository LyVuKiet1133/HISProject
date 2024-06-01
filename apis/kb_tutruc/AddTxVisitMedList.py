import requests

from apis.CurrentServerDateTime import get_server_datetime
from apis.config import get_auth_header
from apis.kb_ketoa.SaveMedical import save_medical_examination
from apis.kb_tutruc.Get_thuoc_tutruc import get_drug_tt
from apis.tiepnhan.Create_Visit import create_visit
from data.Urls import URLS
from apis.kb_ketoa.get_TxVisits import get_TxVisits_EntryID


def Add_TxVisit_MedList():
    auth_header = get_auth_header()
    json_data_visit = create_visit()
    save_medical_examination(json_data_visit, auth_header)
    server_datetime = get_server_datetime()
    reponse_drug_tt = get_drug_tt()
    json_data_drug_tt = reponse_drug_tt.json()
    response_TxVisits = get_TxVisits_EntryID(json_data_visit, auth_header)
    json_data_TxVisits = response_TxVisits.json()
    txVisitId = json_data_TxVisits['txVisitId']
    onDate = json_data_TxVisits['onDate']
    url = URLS.API_ADD_TXVISIT_MEDLIST
    body = create_body(json_data_drug_tt, txVisitId, onDate, server_datetime, json_data_visit)
    print(f'Body: {body}')
    response = requests.post(url=url, json=body, headers=auth_header)
    print(f'URL: {url}')
    print(f'RESPONSE: {response.json()}')
    assert response.status_code == 201
    return response, json_data_visit


def create_body_item(productItem, itemPrice, inventory, txVisitId, onDate, server_datetime, json_data_visit):
    insCardId = json_data_visit['insCardId']
    Qty = 1.0
    InsPrice = itemPrice['insPrice']
    Amt = Qty * InsPrice
    body_item = {
        "TxVisitId": txVisitId,
        "ItemId": productItem['itemId'],
        "ItemName": productItem['name'],
        "ItemUnit": productItem['unit'],
        "Qty": Qty,
        "UseDays": 1,
        "Attribute": 4,
        "IsPaid": False,
        "Status": 1,
        "OnDate": onDate,
        "Price": itemPrice['price'],
        "InsPrice": itemPrice['insPrice'],
        "Amt": Amt,
        "StoreId": inventory['storeId'],
        "InvSource": inventory['invSource'],
        "Type": productItem['type'],
        "InsBenefitRatio": 80,
        "InsPriceRatio": productItem['insPayRatio1'],
        "MedAI": productItem['medAI'],
        "MedStrenght": productItem['medStrenght'],
        "MedUseRoute": "Tiêm" if productItem["medUseRoute"] == 210 else "Khác",
        "MedUsageUnit": productItem["usageUnit"],
        "CreateById": 4451,
        "CreateOn": server_datetime,
        "InputDataByUserId": 4451,
        "MedItem": {
            "ItemId": productItem['itemId'],
            "InsIndex": productItem['insIndex'],
            "Code": productItem['code'],
            "Type": productItem['type'],
            "ItemCat": productItem['itemCat'],
            "ATC": productItem['atc'],
            "Name": productItem['name'],
            "Description": productItem['description'],
            "NtlCode": productItem['ntlCode'],
            "NtlName": productItem['ntlName'],
            "Unit": productItem['unit'],
            "PkgUnit": productItem['pkgUnit'],
            "PkgUnitText": productItem['pkgUnitText'],
            "UsageUnit": productItem['usageUnit'],
            "PPP": productItem['ppp'],
            "PPU": productItem['ppu'],
            "MedAI": productItem['medAI'],
            "MedUseRoute": productItem['medUseRoute'],
            "MedDosageForm": productItem['medDosageForm'],
            "MedStrenght": productItem['medStrenght'],
            "RegNo": productItem['regNo'],
            "MfrCode": productItem['mfrCode'],
            "MfrName": productItem['mfrName'],
            "MfrAddr": "",
            "MfrCountry": productItem['mfrCountry'],
            "InsCode": productItem['insCode'],
            "InsName": productItem['insName'],
            "InsPayRatio1": productItem['insPayRatio1'],
            "Attribute": productItem['attribute'],
            "DrugWarnings": productItem['drugWarnings'],
            "StockCritLevel": productItem['stockCritLevel'],
            "Status": productItem['status'],
            "BidGroupCode": productItem['bidGroupCode'],
            "BidPackageCode": productItem['bidPackageCode'],
            "BidDocNo": productItem['bidDocNo'],
            "SysFullName": productItem['sysFullName'],
            "ProcessingMethodCode": productItem['processingMethodCode'],
            "Note": productItem['note'],
            "FullName": f"{productItem['name']} ({productItem['name']}), {productItem['medStrenght']}",
            "IsInInsCat": True,
            "Remaining": 0.0,
            "InsPrice": 0.0,
            "AttributeDisplay": "Thuộc danh mục bảo hiểm chi",
            "IsLocalPharmacy": False,
            "PlanCoefficient": 0.0,
            "PurchaseName": None
        },
        "Code": productItem['code'],
        "InsBenefitType": None,
        "OnVisit": None,
        "WardAdmId": None,
        "TxVisitMedReturnId": None,
        "InsCardId": insCardId,
        "ApproveQty": None,
        "Dosage": ""
    }
    return body_item


def create_body(response_data, txVisitId, onDate, server_datetime, json_data_visit):
    body = []
    for data in response_data:
        productItem = data['productItem']
        itemPrice = data['itemPrice']
        inventory = data['inventory']
        body_item = create_body_item(productItem, itemPrice, inventory, txVisitId, onDate, server_datetime,
                                     json_data_visit)
        body.append(body_item)
    return body


'''[{
  "modelMethod": null,
  "txVisitMedReturnId": null,
  "insCardId": 1018799,
  "id": 131458,
  "txVisitId": 41031,
  "itemId": 13413,
  "itemName": "Lidonalin",
  "itemUnit": "Ống",
  "qty": 1.0,
  "notes": null,
  "doseMO": null,
  "doseNO": null,
  "doseAN": null,
  "doseEV": null,
  "txtDoseMO": null,
  "txtDoseNO": null,
  "txtDoseAN": null,
  "txtDoseEV": null,
  "doseOther": null,
  "useNotes": null,
  "useWeekDay": null,
  "useDays": 1,
  "attribute": 4,
  "status": 1,
  "onDate": "2024-05-27T16:45:00",
  "price": 4830.000,
  "insPrice": 4830.000,
  "amt": 4830.000,
  "storeId": 155,
  "usePerDay": null,
  "qtyPerUse": null,
  "invSource": 1,
  "type": 1,
  "insBenefitRatio": 80,
  "insPriceRatio": 100,
  "optId": null,
  "ceilingPrice": null,
  "insAmt": null,
  "ptCoPayAmt": null,
  "labExamId": null,
  "confirmDate": null,
  "txVisitTradMedId": null,
  "medAI": "Lidocain+Adrenalin",
  "medStrenght": "36mg+18mcg/1,8ml",
  "medUseRoute": "Tiêm",
  "medUsageUnit": "Ống",
  "createById": 4451,
  "createOn": "2024-05-27T16:46:29.2780088+07:00",
  "inputDataByUserId": 4451,
  "procId": null
}, {
  "modelMethod": null,
  "txVisitMedReturnId": null,
  "insCardId": 1018799,
  "id": 131459,
  "txVisitId": 41031,
  "itemId": 11830,
  "itemName": "Huyết thanh kháng độc tố uốn ván tinh chế (SAT)",
  "itemUnit": "Ống",
  "qty": 1.0,
  "notes": null,
  "doseMO": null,
  "doseNO": null,
  "doseAN": null,
  "doseEV": null,
  "txtDoseMO": null,
  "txtDoseNO": null,
  "txtDoseAN": null,
  "txtDoseEV": null,
  "doseOther": null,
  "useNotes": null,
  "useWeekDay": null,
  "useDays": 1,
  "attribute": 4,
  "status": 1,
  "onDate": "2024-05-27T16:45:00",
  "price": 25263.000,
  "insPrice": 25263.000,
  "amt": 25263.000,
  "storeId": 155,
  "usePerDay": null,
  "qtyPerUse": null,
  "invSource": 1,
  "type": 1,
  "insBenefitRatio": 80,
  "insPriceRatio": 100,
  "optId": null,
  "ceilingPrice": null,
  "insAmt": null,
  "ptCoPayAmt": null,
  "labExamId": null,
  "confirmDate": null,
  "txVisitTradMedId": null,
  "medAI": "Huyết thanh kháng độc tố uốn ván tinh chế",
  "medStrenght": "Huyết thanh kháng độc tố uốn ván tinh chế, (1500 IU/ống)",
  "medUseRoute": "Tiêm",
  "medUsageUnit": "Ống",
  "createById": 4451,
  "createOn": "2024-05-27T16:46:29.2780088+07:00",
  "inputDataByUserId": 4451,
  "procId": null
}]'''