from supports import Windriver
from appium import webdriver
from data.TestData import TestData


def openApp():
    app_path = TestData.APP_PATH
    desired_caps = {
        "app": app_path,
        "platformName": "Windows",
        "deviceName": "WindowsPC",
        "ms:waitForAppLaunch": "10"
    }
    Windriver.start()
    driver_app = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=desired_caps
    )
    return driver_app


if __name__ == "__main__":
    driver = openApp()
