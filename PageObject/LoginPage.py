
class Login:
    txt_signin_username="com.km.emotika:id/etEmailAddress"
    # txt_signin_username = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.EditText"
    txt_signin_password="com.km.emotika:id/etPassword"
    btn_signIn="com.km.emotika:id/btnLogin"
    selectTestModule="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"
    selectTestLesson1="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView"
    selectTestLesson2 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView"
    btn_gobacktoModuleDetail="com.km.emotika:id/ivback"
    btn_startlesson="com.km.emotika:id/tvStartLesson"
    btn_SelectContenttype1option = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.CheckBox[2]"
    btn_next="com.km.emotika:id/tvNext"
    btn_selectRelativeLayout = "com.km.emotika:id/mainRelativeLayout"
    btn_SelectContenttype2option = " /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.CheckBox[2]"
    btn_SelectContenttype3option = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.CheckBox[3]"

    btn_CompleteLesson="com.km.emotika:id/tvComplete"
    btn_gobackHome="com.km.emotika:id/llGoBackHome"
    btn_CompleteModule="com.km.emotika:id/tvBtnText"
    btn_PointsConfirmation="com.km.emotika:id/tvBtnText"
    btn_profile="com.km.emotika:id/rbProfile"
    btn_settings="com.km.emotika:id/ivSetting"
    btn_logout="com.km.emotika:id/tvLogout"
    btn_ConfirmLogout="com.km.emotika:id/tvYes"
    button_skip_xpath="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView"
    button_registration_id="com.km.emotika:id/tvSignup"
    textbox_emailaddress_id="com.km.emotika:id/etSignupEmailAddress"
    button_signup_id="com.km.emotika:id/btnSignup"
    textbox_firstname_id="com.km.emotika:id/etSignUpFirstname"
    textbox_lastname_id="com.km.emotika:id/etSignUpLastName"
    textbox_password_id="com.km.emotika:id/etSignupPassword"
    textbox_confirmpassword_id="com.km.emotika:id/etConfirmPassword"
    toggle_notification_id="com.km.emotika:id/cbNotify"
    checkbox_terms_id="com.km.emotika:id/cbTermsAndCondition"
    button_signupregister_id="com.km.emotika:id/btnSignUp"
    button_registok_id="com.km.emotika:id/tvOk"





    def __init__(self,driver):
        self.driver = driver


    def clickSkip(self):
        self.driver.find_element_by_xpath(self.button_skip_xpath).click()

    def clickRegistration(self):
        self.driver.find_element_by_id(self.button_registration_id).click()

    def clickSignIn(self):
        self.driver.find_element_by_id(self.btn_signIn).click()

    def clickTestModule(self):
        self.driver.find_element_by_xpath(self.selectTestModule).click()

    def clickLesson1(self):
        self.driver.find_element_by_xpath(self.selectTestLesson1).click()

    def clickStartLesson(self):
        self.driver.find_element_by_id(self.btn_startlesson).click()

    def SelectContentType1(self):
        self.driver.find_element_by_xpath(self.btn_SelectContenttype1option).click()

    def clickNext(self):
        self.driver.find_element_by_id(self.btn_next).click()

    def clickRelativeLayout(self):
        self.driver.find_element_by_id(self.btn_selectRelativeLayout).click()

    def SelectContentType2(self):
        self.driver.find_element_by_xpath(self.btn_SelectContenttype2option).click()

    def SelectContentType3(self):
        self.driver.find_element_by_xpath(self.btn_SelectContenttype3option).click()

    def clickCompleteLesson(self):
        self.driver.find_element_by_id(self.btn_CompleteLesson).click()

    def clickCompleteModule(self):
        self.driver.find_element_by_id(self.btn_CompleteModule).click()

    def clickPointsConfirmation(self):
        self.driver.find_element_by_id(self.btn_gobackHome).click()

    def clickLesson2(self):
        self.driver.find_element_by_xpath(self.selectTestLesson2).click()

    def clickBack(self):
        self.driver.find_element_by_id(self.btn_gobacktoModuleDetail).click()

    def clickProfile(self):
        self.driver.find_element_by_id(self.btn_profile).click()

    def clickSettings(self):
        self.driver.find_element_by_id(self.btn_settings).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.btn_logout).click()

    def clickConfirmLogout(self):
        self.driver.find_element_by_id(self.btn_ConfirmLogout).click()

    def setSignInEmailaddress(self,txtemailaddress):
        self.driver.find_element_by_id(self.txt_signin_username).clear()
        self.driver.find_element_by_id(self.txt_signin_username).send_keys(txtemailaddress)

    def setSignInPassword(self, txtpassword):
        self.driver.find_element_by_id(self.txt_signin_password).clear()
        self.driver.find_element_by_id(self.txt_signin_password).send_keys(txtpassword)

    def setEmailaddress(self,emailaddress):
        self.driver.find_element_by_id(self.textbox_emailaddress_id).clear()
        self.driver.find_element_by_id(self.textbox_emailaddress_id).send_keys(emailaddress)

    def clickSignup(self):
        self.driver.find_element_by_id(self.button_signup_id).click()

    def setFirstname(self,firstname):
        self.driver.find_element_by_id(self.textbox_firstname_id).clear()
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element_by_id(self.textbox_lastname_id).clear()
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(lastname)

    def setPassowrd(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def setConfirmpassword(self,confirmpassword):
        self.driver.find_element_by_id(self.textbox_confirmpassword_id).clear()
        self.driver.find_element_by_id(self.textbox_confirmpassword_id).send_keys(confirmpassword)

    def clickToggle(self):
        self.driver.find_element_by_id(self.toggle_notification_id).click()

    def clickCheckboxterm(self):
        self.driver.find_element_by_id(self.checkbox_terms_id).click()

    def clickSignupregister(self):
        self.driver.find_element_by_id(self.button_signupregister_id).click()

    def clickRegisOK(self):
        self.driver.find_element_by_id(self.button_registok_id).click()

    def ConfirmPoints(self):
        self.driver.find_element_by_id(self.btn_PointsConfirmation).click()