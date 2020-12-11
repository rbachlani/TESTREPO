import random

from PageObject.ActivationPage import Activation
from PageObject.LoginPage import Login
from Utilities.customeLogger import LogGen
from PageObject.BuyModule import BuyMode

class Test_001_Login:
    txtemailaddress = "sophia1@mailinator.com"
    logger = LogGen.loggen()

    # def test_case1(self, setup):
        # self.logger.info("********Test case1**********")
        # self.logger.info("********verify Sign**********")
        # self.driver = setup
        #
        # self.lp = Login(self.driver)
        #
        # self.lp.clickSkip()
        # self.lp.setSignInEmailaddress(self.txtemailaddress)
        # self.lp.setSignInPassword("Admin@1234")
        # self.lp.clickSignIn()
        # self.lp.clickTestModule()
        # self.lp.clickLesson1()
        # self.lp.clickStartLesson()
        # self.lp.SelectContentType1()
        # self.lp.clickNext()
        # self.driver.implicitly_wait(30)
        # self.lp.clickRelativeLayout()
        # self.lp.clickRelativeLayout()
        # self.lp.SelectContentType2()
        # self.lp.SelectContentType3()
        # self.lp.clickCompleteLesson()
        # self.lp.clickPointsConfirmation()
        # self.lp.clickLesson2()
        # self.lp.clickStartLesson()
        # self.lp.SelectContentType1()
        # self.lp.clickCompleteLesson()
        # self.lp.clickCompleteModule()
        # self.lp.clickProfile()
        # self.lp.clickSettings()
        # self.lp.clickLogout()
        # self.lp.clickConfirmLogout()
    #     self.lp.clickRegistration()
    #     username = str("automator" + str(random.randint(1, 1000)))
    #     self.lp.setEmailaddress(username + "@mailinator.com")
    #     self.lp.clickSignup()
    #     self.lp.setFirstname(username)
    #     self.lp.setLastname("test")
    #     self.lp.setPassowrd("Admin@1234")
    #     self.lp.setConfirmpassword("Admin@1234")
    #     self.lp.clickToggle()
    #     self.lp.clickCheckboxterm()
    #     self.lp.clickSignupregister()
    #     self.lp.clickRegisOK()
    #
    #     Activation.setupChrome(self).get("https://www.mailinator.com/")
    #     self.Ap = Activation(self.driver)
    #
    #     self.Ap.SetEmailID(username + "@mailinator.com")
    #     self.Ap.openMailBox()
    #     self.Ap.clickOnFirstEmail()
    #     self.Ap.clickActivate()
    #     self.lp.setSignInEmailaddress(username + "@mailinator.com")
    #     self.lp.setSignInPassword("Admin@1234")
    #     self.lp.clickSignIn()
    #     self.lp.clickSkip()
    #     self.lp.ConfirmPoints()
    #     self.lp.clickProfile()
    #     self.lp.clickSettings()
    #     self.lp.clickLogout()
    #     self.lp.clickConfirmLogout()

    def test_case2(self, setup):
        self.logger.info("********Test case1**********")
        self.logger.info("********verify Sign**********")
        self.driver = setup

        self.Bm = BuyMode(self.driver)
        self.logger.info("********Test case 2**********")
        self.logger.info("********verify Sign**********")
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.clickSkip()
        self.lp.setSignInEmailaddress("automator930@mailinator.com")
        self.lp.setSignInPassword("Admin@1234")
        self.lp.clickSignIn()
        self.Bm.ViewRecommended()
        self.Bm.SearchModule("8000")

        self.Bm.selectModule()
        self.Bm.clickAddtoCart()
        self.Bm.clickCheckOut()
        self.Bm.clickCheckOutOverlay()
        self.Bm.clickAddPayment()
        self.Bm.setCardNo("4242424242424242")
        self.Bm.setExpiryDate("1222")
        self.Bm.setCVC("123")
        self.Bm.setZipCode("74450")
        self.Bm.setCardHolderName("Raheel")
        self.Bm.setAddress("Test Address")
        self.Bm.setCountry("PK")
        self.Bm.setRegion("SDH")
        self.Bm.setCity("KHI")
        self.Bm.doScroll()
        self.Bm.clickNext()
        self.Bm.clickCollapse()
        self.Bm.clickNext()
        self.Bm.clickPlaceOrder()
        self.Bm.clickBadgeConfirmation()
        self.Bm.clickPointConfirmation()

