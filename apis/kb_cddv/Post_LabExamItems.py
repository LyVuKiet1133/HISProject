import pytest
import requests

from apis.config import get_auth_header
from data.Urls import URLS
from apis.kb_cddv.Add_items_labexams import add_items_to_labexams


def add_items_to_labexams():
    auth_header = get_auth_header()
    response_labExIds = add_items_to_labexams()
    json_data_labExIds = response_labExIds.json()
    url = URLS.API_LabExamItems
    body = [json_data_labExIds]
    print("Body" + body)
