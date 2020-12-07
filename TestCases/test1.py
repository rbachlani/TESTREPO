from Utilities.readProperties import readConfig
import random
from Utilities.customeLogger import LogGen
from PageObject.LoginPage import Login
from PageObject.ActivationPage import Activation
import time


class Test_001_Login:
    txtemailaddress = "sophia1@mailinator.com"
    logger = LogGen.loggen()

    def test_case1(self, setup):
        self.logger.info("********Test case1**********")
        self.logger.info("********verify Sign**********")
        self.driver = setup

        self.lp = Login(self.driver)

        self.lp.clickSkip()
        self.lp.setSignInEmailaddress(self.txtemailaddress)
        self.lp.setSignInPassword("Admin@1234")
        self.lp.clickSignIn()
        self.lp.clickTestModule()
        self.lp.clickLesson1()
        self.lp.clickStartLesson()
        self.lp.SelectContentType1()
        self.lp.clickNext()
        self.driver.implicitly_wait(30)
        self.lp.clickRelativeLayout()
        self.lp.clickRelativeLayout()
        self.lp.SelectContentType2()
        self.lp.SelectContentType3()
        self.lp.clickCompleteLesson()
        self.lp.clickPointsConfirmation()
        self.lp.clickLesson2()
        self.lp.clickStartLesson()
        self.lp.SelectContentType1()
        self.lp.clickCompleteLesson()
        self.lp.clickCompleteModule()
        self.lp.clickProfile()
        self.lp.clickSettings()
        self.lp.clickLogout()
        self.lp.clickConfirmLogout()
        self.lp.clickRegistration()
        username = str("automator" + str(random.randint(1, 1000)))
        self.lp.setEmailaddress(username + "@mailinator.com")
        self.lp.clickSignup()
        self.lp.setFirstname(username)
        self.lp.setLastname("test")
        self.lp.setPassowrd("Admin@1234")
        self.lp.setConfirmpassword("Admin@1234")
        self.lp.clickToggle()
        self.lp.clickCheckboxterm()
        self.lp.clickSignupregister()
        self.lp.clickRegisOK()

        Activation.setupChrome(self).get("https://www.mailinator.com/")
        self.Ap = Activation(self.driver)

        self.Ap.SetEmailID(username + "@mailinator.com")
        self.Ap.openMailBox()
        self.Ap.clickOnFirstEmail()
        self.Ap.clickActivate()
        self.lp.setSignInEmailaddress(username + "@mailinator.com")
        self.lp.setSignInPassword("Admin@1234")
        self.lp.clickSignIn()
        self.lp.clickSkip()
        self.lp.ConfirmPoints()
        self.lp.clickProfile()
        self.lp.clickSettings()
        self.lp.clickLogout()
        self.lp.clickConfirmLogout()
