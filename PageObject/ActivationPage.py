from selenium import webdriver
#
# class test_chromebrowser:
#     driver2=webdriver.Chrome()
#     driver2.get("https://www.mailinator.com/")
#     driver2.find_element_by_xpath("//input[@id='addOverlay']").clear()
#     driver2.find_element_by_xpath("//input[@id='addOverlay']").send_keys("abcd")
#     driver2.find_element_by_xpath("//button[@id='go-to-public']").click()

class Activation:

    setemail="//input[@id='addOverlay']"

    def __init__(self,driver):
        self.driver = driver

    def setupChrome(self):
        driver2 = webdriver.Chrome()
        driver2.implicitly_wait(30)
        return driver2

    def SetEmailID(self,emailid):
        self.driver.find_element_by_xpath(self.setemail).clear()
        self.driver.find_element_by_xpath(self.setemail).send_keys(emailid)
