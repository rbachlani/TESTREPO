from appium.webdriver.common.touch_action import TouchAction

class BuyMode:
    btn_AddtoCart="com.km.emotika:id/tvAddToCArt"
    btn_Checkout="com.km.emotika:id/tvCheckout"
    btn_CheckoutOverlay="com.km.emotika:id/llCheckout"
    btn_AddPayment="com.km.emotika:id/tvName"
    txt_CardNo="com.km.emotika:id/et_card_number"
    txt_ExpiryDate="com.km.emotika:id/et_expiry"
    txt_CVC="com.km.emotika:id/et_cvc"
    txt_ZipCode="com.km.emotika:id/et_postal_code"
    txt_CardHolderName="com.km.emotika:id/etYourName"
    txt_Address="com.km.emotika:id/etAddress"
    txt_Country="com.km.emotika:id/etCountry"
    txt_Region="com.km.emotika:id/etState"
    txt_City="com.km.emotika:id/etCity"
    btn_Next="com.km.emotika:id/tvNext"
    btn_NextOverlay="com.km.emotika:id/llNext"
    btn_PlaceOrder="com.km.emotika:id/tvPlaceOrder"
    btn_BadgeOk="com.km.emotika:id/tvBtnText"
    btn_PointsOk="com.km.emotika:id/tvBtnText"
    btn_ViewRecommended="com.km.emotika:id/tvRecommendedSeeAll"
    btn_moduleselection="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView"
    txt_moduleSearch="com.km.emotika:id/etSearch"
    view_BillingInfo="com.km.emotika:id/tvAddBillingInfo"
    scrollView="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout"
    btn_gobacktoModuleDetail = "com.km.emotika:id/ivback"
    label_mycart="com.km.emotika:id/tvMyCart"
    screen_CardDetail="com.km.emotika:id/llCardDetail"

    def __init__(self,driver):
        self.driver = driver

    def clickCardDetail(self):
        self.driver.find_element_by_id(self.screen_CardDetail).click()

    def clickMyCart(self):
        self.driver.find_element_by_id(self.label_mycart).click()

    def doScroll(self):
        TouchAction(self.driver)   .press(x=41, y=1084)   .move_to(x=26, y=346)   .release()   .perform()

    def doScroll2(self):
        TouchAction(self.driver).press(x=48, y=978).move_to(x=43, y=529).release().perform()

    def clickBack(self):
        self.driver.find_element_by_id(self.btn_gobacktoModuleDetail).click()

    def clickAddtoCart(self):
        self.driver.find_element_by_id(self.btn_AddtoCart).click()

    def clickCheckOut(self):
        self.driver.find_element_by_id(self.btn_Checkout).click()

    def clickCheckOutOverlay(self):
        self.driver.find_element_by_id(self.btn_CheckoutOverlay).click()

    def clickAddPayment(self):
        self.driver.find_element_by_id(self.btn_AddPayment).click()

    def setCardNo(self, cardNo):
        self.driver.find_element_by_id(self.txt_CardNo).clear()
        self.driver.find_element_by_id(self.txt_CardNo).send_keys(cardNo)

    def setExpiryDate(self, expiryDate):
        self.driver.find_element_by_id(self.txt_ExpiryDate).clear()
        self.driver.find_element_by_id(self.txt_ExpiryDate).send_keys(expiryDate)

    def setCVC(self, CVCno):
        self.driver.find_element_by_id(self.txt_CVC).clear()
        self.driver.find_element_by_id(self.txt_CVC).send_keys(CVCno)

    def setZipCode(self, zipCode):
        self.driver.find_element_by_id(self.txt_ZipCode).clear()
        self.driver.find_element_by_id(self.txt_ZipCode).send_keys(zipCode)

    def setCardHolderName(self, cardHolderName):
        self.driver.find_element_by_id(self.txt_CardHolderName).clear()
        self.driver.find_element_by_id(self.txt_CardHolderName).send_keys(cardHolderName)

    def setAddress(self, Address):
        self.driver.find_element_by_id(self.txt_Address).clear()
        self.driver.find_element_by_id(self.txt_Address).send_keys(Address)

    def setCountry(self, Country):
        self.driver.find_element_by_id(self.txt_Country).clear()
        self.driver.find_element_by_id(self.txt_Country).send_keys(Country)

    def setRegion(self, Region):
        self.driver.find_element_by_id(self.txt_Region).clear()
        self.driver.find_element_by_id(self.txt_Region).send_keys(Region)

    def setCity(self, City):
        self.driver.find_element_by_id(self.txt_City).clear()
        self.driver.find_element_by_id(self.txt_City).send_keys(City)

    def selectModule(self):
        self.driver.find_element_by_xpath(self.btn_moduleselection).click()

    def ViewRecommended(self):
        self.driver.find_element_by_id(self.btn_ViewRecommended).click()

    def clickNext(self):
        self.driver.find_element_by_id(self.btn_Next).click()

    def clickNextOverlay(self):
        self.driver.find_element_by_id(self.btn_NextOverlay).click()


    def clickPlaceOrder(self):
        self.driver.find_element_by_id(self.btn_PlaceOrder).click()

    def clickBadgeConfirmation(self):
        self.driver.find_element_by_id(self.btn_BadgeOk).click()

    def clickPointConfirmation(self):
        self.driver.find_element_by_id(self.btn_PointsOk).click()

    def SearchModule(self, Searchtxt):
        self.driver.find_element_by_id(self.txt_moduleSearch).clear()
        self.driver.find_element_by_id(self.txt_moduleSearch).send_keys(Searchtxt)

    def ViewBillingInfo(self):
        self.driver.find_element_by_id(self.view_BillingInfo).click()
