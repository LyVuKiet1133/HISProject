from support import Windriver
from appium import webdriver


def openApp():
    app_path = r"C:\Users\VANTHANG\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\InfomedHISLK\InfomedHISLK.appref-ms"
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
