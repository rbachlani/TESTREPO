from selenium import webdriver
from Utilities.customeLogger import LogGen
# class test_chromebrowser:
#     driver2=webdriver.Chrome()
#     driver2.get("https://www.mailinator.com/")
#     driver2.find_element_by_xpath("//input[@id='addOverlay']").clear()
#     driver2.find_element_by_xpath("//input[@id='addOverlay']").send_keys("abcd")
#     driver2.find_element_by_xpath("//button[@id='go-to-public']").click()

class Activation:
    logger = LogGen.loggen()
    setemail="//input[@id='addOverlay']"
    btn_go="//button[@id='go-to-public']"
    btn_SelectFirstEmail="body.nav-md.ng-scope:nth-child(2) div.container.body:nth-child(2) div.main_container div.right_col:nth-child(3) div.col-md-12.col-sm-12.col-xs-12:nth-child(5) div.x_panel div.x_content div.table-responsive:nth-child(1) table.table.table-striped.jambo_table tbody:nth-child(2) tr.even.pointer.ng-scope > td.ng-binding:nth-child(3)"
    btn_Activate="table.main-table:nth-child(1) tbody:nth-child(1) tr:nth-child(3) td:nth-child(1) a:nth-child(1) > button:nth-child(1)"
    dd=[]

    def __init__(self,driver):
        self.driver = driver
    @staticmethod
    def setupChrome(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        return self.driver

    def SetEmailID(self,emailid):
        self.driver.find_element_by_xpath(self.setemail).clear()
        self.driver.find_element_by_xpath(self.setemail).send_keys(emailid)

    def LaunchWeb(self,website):
        self.driver.get(website)

    def openMailBox(self):
        self.driver.find_element_by_xpath(self.btn_go).click()

    def clickOnFirstEmail(self):
        self.driver.find_element_by_css_selector(self.btn_SelectFirstEmail).click()

    def clickActivate(self):
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # iframe = self.driver.find_element_by_name('msg_body')
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_css_selector(self.btn_Activate).click()

