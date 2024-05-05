from appium.webdriver.common.mobileby import MobileBy

from screens.BaseScreen import BaseScreen


class LoginPage(BaseScreen):
    username_txf = (MobileBy.ACCESSIBILITY_ID, "txtAccName")
    password_txf = (MobileBy.ACCESSIBILITY_ID, "txtPassword")
    login_btn = (MobileBy.ACCESSIBILITY_ID, "loignbtn")

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, username: str, password: str):
        self.do_send_keys(self.username_txf, username)
        self.do_send_keys(self.password_txf, password)
        self.do_click(self.login_btn)
