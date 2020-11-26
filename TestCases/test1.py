from appium import webdriver
from Utilities.readProperties import readConfig
import random
from Utilities.customeLogger import LogGen
from PageObject.LoginPage import Login


class Test_001_Login:
    # serverurl = readConfig.getServerurl()
    # emailaddress = readConfig.getEmailaddress()
    # firstname = readConfig.getFirstname()
    # lastname = readConfig.getLastname()
    # password = readConfig.getPassword()
    # confirmpassword = readConfig.getConfirmpassword()

    logger = LogGen.loggen()

    def test_case1(self, setup):
        self.logger.info("********Test case1**********")
        self.logger.info("********verify Sign**********")
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.clickSkip()
        self.lp.setSignInEmailaddress("sophia1@mailinator.com")
        self.lp.setSignInPassword("Admin@1234")
        self.lp.clickSignIn()
        self.lp.clickTestModule()
        self.lp.clickProfile()
        self.lp.clickSettings()
        self.lp.clickLogout()
        self.lp.clickConfirmLogout()
        self.lp.clickRegistration()
        username = str("automator"+str(random.randint(1, 1000)))
        self.lp.setEmailaddress(username+"@mailinator.com")
        self.lp.clickSignup()
        self.lp.setFirstname(username)
        self.lp.setLastname("test")
        self.lp.setPassowrd("Admin@1234")
        self.lp.setConfirmpassword("Admin@1234")
        self.lp.clickToggle()
        self.lp.clickCheckboxterm()
        self.lp.clickSignupregister()
        self.lp.clickRegisOK()
