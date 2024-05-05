
from support import OpenHISApp
import pytest


@pytest.fixture(scope='class')
def init_driver(request):
    driver = OpenHISApp.openApp()
    request.cls.driver = driver
    yield driver
    driver.close()
