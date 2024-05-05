from screens.Login_screen import LoginPage
import pytest

from test.BaseTest import BaseTest


class Test_login(BaseTest):

    def test_login(self):
        self.login_screen = LoginPage(self.driver)
        self.login_screen.do_login("ducpn", "123")
