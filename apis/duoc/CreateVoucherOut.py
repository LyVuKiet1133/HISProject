import requests

from data.Urls import URLS
from apis.config import get_auth_header
from apis.CurrentServerDateTime import get_server_datetime


def Create_Voucher_Out():
    auth_header = get_auth_header()
    url = URLS.API_CREATE_VOUCHER_OUT
    body = {
        "imsGetInvNowWithBy": None,
        "Voucher": {
            "Type": 70,
            "OnDate": get_server_datetime(),
            "Description": " ",
            "StoreId": 24,
            "TxVisitId": None,
            "VisitEntryId": None,
            "RefStoreId": 28,
            "InvSource": 1,
            "CreateById": 4451,
            "CreateOn": get_server_datetime(),
            "InvStatus": 0,
            "InvStatusDescription": None,
            "ProcStatusDescription": None,
            "CustomerName": None,
            "InvoiceText": None
        },
        "voucherOuts": [
            {
                "PPU": 1,
                "VatPerc": 0,
                "LotId": 21985,
                "ItemId": 11272,
                "ItemSource": 1,
                "Qty": 1.0,
                "Status": 0
            },
            {
                "PPU": 1,
                "VatPerc": 0,
                "LotId": 21986,
                "ItemId": 11280,
                "ItemSource": 1,
                "Qty": 1.0,
                "Status": 0
            }
        ],
        "voucherOutInvs": None,
        "InvRequests": [],
        "VoucherExt": None,
        "VoucherOutExts": None,
        "RequestByInventory": None
    }
    response = requests.post(url=url, json=body, headers=auth_header)
    print("URL: ", url)
    assert response.status_code == 200
    print("RESPONSE: ", response.json())
    return response


# Response:
'''
{
  "imsGetInvNowWithBy": null,
  "voucher": {
    "voucherId": 51172,
    "voucherNo": "KCTH.OIN.24.05.0007",
    "type": 70,
    "onDate": "2024-05-25T22:16:06.5282421+07:00",
    "description": " ",
    "storeId": 24,
    "custId": null,
    "stmId": null,
    "medRcdId": null,
    "txVisitId": null,
    "visitEntryId": null,
    "orderId": null,
    "bidId": null,
    "refVoucherId": null,
    "refStoreId": 28,
    "frPxId": null,
    "category": null,
    "invSource": 1,
    "reasonCode": null,
    "invoiceNo": null,
    "invoiceCode": null,
    "invoiceDate": null,
    "deliverName": null,
    "receiverName": null,
    "deliverPhone": null,
    "createById": 4451,
    "createOn": "2024-05-25T22:19:27.0616957+07:00",
    "invStatus": 3,
    "procStatus": 0,
    "attribute": null,
    "confirmNo": null,
    "totalAmt": null,
    "totalAmtVat": null,
    "totalAmtCost": null,
    "bidCustId": null,
    "hasGroupProducts": null
  },
  "voucherOuts": [{
    "id": 190381,
    "voucherId": 51172,
    "ppu": 1,
    "saleAmt": 1000.0000,
    "vatPerc": 0,
    "vatAmt": 0,
    "txVisitMedId": null,
    "insPrice": 1000.000,
    "price": 1000.000,
    "insAmt": 1000.0000,
    "stmDetailId": null,
    "procStatus": null,
    "lotId": 21985,
    "itemId": 11272,
    "itemSource": 1,
    "qty": 1.0,
    "amt": 1000.0000,
    "status": 3
  }, {
    "id": 190382,
    "voucherId": 51172,
    "ppu": 1,
    "saleAmt": 1000.0000,
    "vatPerc": 0,
    "vatAmt": 0,
    "txVisitMedId": null,
    "insPrice": 1000.000,
    "price": 1000.000,
    "insAmt": 1000.0000,
    "stmDetailId": null,
    "procStatus": null,
    "lotId": 21986,
    "itemId": 11280,
    "itemSource": 1,
    "qty": 1.0,
    "amt": 1000.0000,
    "status": 3
  }],
  "voucherOutInvs": [{
    "id": 191155,
    "vouOutId": 190381,
    "lotId": 21985,
    "vouInId": 60037,
    "itemId": 11272,
    "qty": 1.000,
    "insPrice": 1000.000,
    "price": 1000.000,
    "insAmt": 1000.00,
    "amt": 1000.00,
    "refVouInId": null
  }, {
    "id": 191156,
    "vouOutId": 190382,
    "lotId": 21986,
    "vouInId": 60038,
    "itemId": 11280,
    "qty": 1.000,
    "insPrice": 1000.000,
    "price": 1000.000,
    "insAmt": 1000.00,
    "amt": 1000.00,
    "refVouInId": null
  }],
  "invRequests": [],
  "voucherExt": null,
  "voucherOutExts": null,
  "requestByInventory": null
}
'''
