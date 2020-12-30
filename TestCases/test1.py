import random
import time
import pytest

from PageObject.ActivationPage import Activation
from PageObject.LoginPage import Login
from Utilities.customeLogger import LogGen
from PageObject.BuyModule import BuyMode
from PageObject.ProfilePage import Profile

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

    # def test_case2(self, setup):
    #     self.logger.info("********Test case1**********")
    #     self.logger.info("********verify Sign**********")
    #     self.driver = setup
    #
    #     self.Bm = BuyMode(self.driver)
    #     self.logger.info("********Test case 2**********")
    #     self.logger.info("********verify Sign**********")
    #     self.driver = setup
    #     self.lp = Login(self.driver)
    #     self.lp.clickSkip()
    #     self.lp.setSignInEmailaddress("automator257@mailinator.com")
    #     self.lp.setSignInPassword("Admin@1234")
    #     self.lp.clickSignIn()
    #     self.Bm.ViewRecommended()
    #     self.Bm.SearchModule("8000")
    #
    #     self.Bm.selectModule()
    #     self.Bm.clickAddtoCart()
    #     self.Bm.clickCheckOut()
    #     self.Bm.clickCheckOutOverlay()
    #     self.Bm.clickAddPayment()
    #     self.Bm.setCardNo("4000000000003063")
    #     self.Bm.setExpiryDate("1222")
    #     self.Bm.setCVC("123")
    #     self.Bm.setZipCode("74450")
    #     self.Bm.setCardHolderName("Raheel")
    #     self.Bm.setAddress("Test Address")
    #     self.Bm.setCountry("PK")
    #     self.Bm.setRegion("SDH")
    #     self.Bm.setCity("KHI")
    #     self.Bm.doScroll()
    #     self.Bm.clickNext()
    #     self.driver.find_element_by_id("com.km.emotika:id/czv_submit_button").click()
    #     self.Bm.clickCollapse()
    #     self.Bm.clickNext()
    #     self.Bm.clickPlaceOrder()
    #     self.Bm.clickBadgeConfirmation()
    #     self.Bm.clickPointConfirmation()

    def funclogin(self, setup):
        self.logger.info("********Test case1**********")
        self.logger.info("********verify Sign**********")
        self.driver = setup
        self.Bm = BuyMode(self.driver)
        self.driver = setup
        self.lp = Login(self.driver)
        # self.lp = Login(self.driver)
        # self.lp = Login(self.driver)

        self.lp.clickSkip()
        self.lp.setSignInEmailaddress("automator605@mailinator.com")
        self.lp.setSignInPassword("Admin@1234")
        self.lp.clickSignIn()
        self.lp.clickProfile()
        time.sleep(3)
        self.lp.clickSettings()
        self.driver = setup
        self.Pp = Profile(self.driver)
        self.Pp.ViewPaymentDetails()
        time.sleep(3)
        self.Pp.AddNewPayment()

    def ProfileLogin(self, setup):
        self.logger.info("********Test case1**********")
        self.logger.info("********verify Sign**********")
        self.driver = setup
        self.Bm = BuyMode(self.driver)
        self.driver = setup
        self.lp = Login(self.driver)
        # self.lp = Login(self.driver)
        # self.lp = Login(self.driver)
        self.lp.clickSkip()
        self.lp.setSignInEmailaddress("automator605@mailinator.com")
        self.lp.setSignInPassword("Admin@1234")
        self.lp.clickSignIn()
        time.sleep(3)
        self.lp.doScroll()
        self.lp.clickProfile()
        time.sleep(3)
        self.lp.clickSettings()

    @pytest.mark.test1
    def test_case1(self,setup):
        self.funclogin(setup)
        self.Bm.setCardNo("4000000000003246")
        self.Bm.setExpiryDate("1222")
        self.Bm.setCVC("123")
        self.Bm.setZipCode("74450")
        self.Bm.setCardHolderName("Raheel")
        self.Bm.setAddress("Test Address")
        self.Bm.setCountry("PK")
        self.Bm.setRegion("SDH")
        self.Bm.setCity("KHI")
        self.Pp.SavePayment()
        self.driver.implicitly_wait(30)
        self.Pp.SubmitRadioVisaProcess()
        self.Pp.SubmitVisaProcess()
        self.driver.implicitly_wait(30)
        self.lp.ReturnHome()
        if self.driver.find_element_by_id("com.km.emotika:id/rbProfile").is_displayed():
            assert True

        else:
            assert False

    @pytest.mark.test2
    def test_case2(self,setup):
        self.funclogin(setup)
        self.Bm.setCardNo("4000000000003238")
        self.Bm.setExpiryDate("1222")
        self.Bm.setCVC("123")
        self.Bm.setZipCode("74450")
        self.Bm.setCardHolderName("Raheel")
        self.Bm.setAddress("Test Address")
        self.Bm.setCountry("PK")
        self.Bm.setRegion("SDH")
        self.Bm.setCity("KHI")
        self.Pp.SavePayment()
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.Pp.settxtVisaProcess("424242")
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.Pp.SubmitVisaProcess()
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.lp.ReturnHome()
        if self.driver.find_element_by_id("com.km.emotika:id/rbProfile").is_displayed():
            assert True

        else:
            assert False

    @pytest.mark.test3
    def test_case3(self,setup):
        self.funclogin(setup)
        self.Bm.setCardNo("4000000000003253")
        self.Bm.setExpiryDate("1222")
        self.Bm.setCVC("123")
        self.Bm.setZipCode("74450")
        self.Bm.setCardHolderName("Raheel")
        self.Bm.setAddress("Test Address")
        self.Bm.setCountry("PK")
        self.Bm.setRegion("SDH")
        self.Bm.setCity("KHI")
        self.Pp.SavePayment()
        self.driver.implicitly_wait(30)
        self.Pp.SubmitChkBx1VisaProcess()
        self.Pp.SubmitChkBx2VisaProcess()
        self.driver.implicitly_wait(30)
        self.Pp.SubmitChkBx3VisaProcess()
        self.Pp.SubmitVisaProcess()
        self.driver.implicitly_wait(30)
        self.lp.ReturnHome()
        if self.driver.find_element_by_id("com.km.emotika:id/rbProfile").is_displayed():
            assert True

        else:
            assert False

    @pytest.mark.test4
    def test_case4(self,setup):
        self.funclogin(setup)
        self.Bm.setCardNo("4000000000003063")
        self.Bm.setExpiryDate("1222")
        self.Bm.setCVC("123")
        self.driver.implicitly_wait(30)
        self.Bm.setZipCode("74450")
        self.Bm.setCardHolderName("Raheel")
        self.Bm.setAddress("Test Address")
        self.Bm.setCountry("PK")
        self.Bm.setRegion("SDH")
        self.Bm.setCity("KHI")
        self.Pp.SavePayment()
        self.driver.implicitly_wait(30)
        #self.Pp.SubmitVisaProcess()
        self.lp.ReturnHome()
        if self.driver.find_element_by_id("com.km.emotika:id/rbProfile").is_displayed():
            assert True

        else:
            assert False

    @pytest.mark.test5
    def test_case5(self,setup):
        self.funclogin(setup)
        self.Bm.setCardNo("4000000000003220")
        self.Bm.setExpiryDate("1222")
        self.Bm.setCVC("123")
        self.Bm.setZipCode("74450")
        self.Bm.setCardHolderName("Raheel")
        self.Bm.setAddress("Test Address")
        self.Bm.setCountry("PK")
        self.Bm.setRegion("SDH")
        self.Bm.setCity("KHI")
        self.Pp.SavePayment()
        self.driver.implicitly_wait(30)
        self.Pp.SubmitVisaProcess()
        self.driver.implicitly_wait(30)
        self.lp.ReturnHome()

        if self.driver.find_element_by_id("com.km.emotika:id/rbProfile").is_displayed():
            assert True

        else:
            assert False


    @pytest.mark.test6
    def test_case6(self,setup):
        self.ProfileLogin(setup)
        self.driver = setup
        self.Pp = Profile(self.driver)
        # self.Pp.ClickAccountInfoMenu()
        # self.Pp.ClickChangeNameSubMenu()
        # self.Pp.setFirstName("Raheel")
        # self.Pp.setLastName("Bachlani")
        # self.Pp.ClickNameSave()
        # self.Pp.ClickChangePasswordSubMenu()
        # self.Pp.setOldPassword("Admin@12345")
        # self.Pp.setNewPassword("Admin@1234")
        # self.Pp.setConfirmNewPassword("Admin@1234")
        # self.Pp.ClickConfirmPasswordChange()
        # self.Pp.ClickOK()
        self.driver = setup
        self.lp = Login(self.driver)
        time.sleep(3)
        # self.lp.clickSettings()
        # self.Pp.FlipNotifications()
        # time.sleep(3)
        # self.Pp.FlipNotifications()
        self.Pp.ClickTransactionHistoryMenu()
        # self.Pp.ClickTransactionHistoryMenu2()
        time.sleep(3)
        self.Pp.ClickGoBack()
        self.Pp.ClickInviteFriendMenu()
        self.Pp.ClickCopyLink()
        self.Pp.ClickOkButton()
        self.Pp.ClickShareButton()
        self.Pp.ClickSMSOption()
        time.sleep(3)
        self.Pp.clickRecipientField()
        self.Pp.setRecipientNumber("03445880607")
        self.Pp.ClickSendButton()
        # TouchAction(driver).press(x=487, y=631).move_to(x=460, y=2139).release().perform()