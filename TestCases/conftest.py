from appium import webdriver
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

