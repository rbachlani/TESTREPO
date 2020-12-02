from appium import webdriver
# from selenium import webdriver
import pytest

desired_cap = {
    "platformName": "Android",
    "deviceName": "a2820db5",
    "app": "C:\\Users\\Raheel Bachlani\\Desktop\\app-debug.apk",
}
@pytest.fixture()
def setup():
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
    driver.implicitly_wait(30)
    return driver

# #
# @pytest.fixture()
# def setupChrome():
#     driver2 = webdriver.Chrome()
#     driver2.implicitly_wait(30)
#     return driver2
