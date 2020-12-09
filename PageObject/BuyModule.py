

class BuyMode:
    btn_AddtoCart="com.km.emotika:id/llAddToCart"
    btn_Checkout="com.km.emotika:id/llCheckout"
    btn_AddPayment="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView"
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
    btn_PlaceOrder="com.km.emotika:id/tvPlaceOrder"
    btn_BadgeOk="com.km.emotika:id/tvBtnText"
    btn_PointsOk="com.km.emotika:id/tvBtnText"
    btn_ViewRecommended="com.km.emotika:id/tvRecommendedSeeAll"
    btn_moduleselection="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView"

    def __init__(self,driver):
        self.driver = driver

    def clickAddtoCart(self):
        self.driver.find_element_by_xpath(self.btn_AddtoCart).click()

    def clickCheckOut(self):
        self.driver.find_element_by_id(self.btn_Checkout).click()

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

    def clickPlaceOrder(self):
        self.driver.find_element_by_id(self.btn_PlaceOrder).click()

    def clickBadgeConfirmation(self):
        self.driver.find_element_by_id(self.btn_BadgeOk).click()

    def clickPointConfirmation(self):
        self.driver.find_element_by_id(self.btn_PointsOk).click()
