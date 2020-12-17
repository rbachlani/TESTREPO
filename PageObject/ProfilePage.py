



class Profile:
    button_PaymentDetails = "com.km.emotika:id/tvPaymentDetail"
    button_AddNewPayment = "com.km.emotika:id/tvAddNew"
    button_SavePayment = "com.km.emotika:id/tvSave"
    button_SubmitVisaProcess = "com.km.emotika:id/czv_submit_button"
    Radiobtn_VisaProcess  =   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[1]"

    CheckBoxbtn1_VisaProcess = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.CheckBox[1]"

    CheckBoxbtn2_VisaProcess = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.CheckBox[2]"

    CheckBoxbtn3_VisaProcess = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.CheckBox[3]"

    txtbox_VisaProcess="com.km.emotika:id/czv_text_entry"

    def __init__(self,driver):
        self.driver = driver

    def settxtVisaProcess(self,txtCode):
        self.driver.find_element_by_id(self.txtbox_VisaProcess).clear()
        self.driver.find_element_by_id(self.txtbox_VisaProcess).send_keys(txtCode)


    def SubmitRadioVisaProcess(self):
        self.driver.find_element_by_xpath(self.Radiobtn_VisaProcess).click()

    def SubmitChkBx1VisaProcess(self):
        self.driver.find_element_by_xpath(self.CheckBoxbtn1_VisaProcess).click()

    def SubmitChkBx2VisaProcess(self):
        self.driver.find_element_by_xpath(self.CheckBoxbtn2_VisaProcess).click()

    def SubmitChkBx3VisaProcess(self):
        self.driver.find_element_by_xpath(self.CheckBoxbtn3_VisaProcess).click()

    def SubmitVisaProcess(self):
        self.driver.find_element_by_id(self.button_SubmitVisaProcess).click()

    def ViewPaymentDetails(self):
        self.driver.find_element_by_id(self.button_PaymentDetails).click()

    def AddNewPayment(self):
        self.driver.find_element_by_id(self.button_AddNewPayment).click()

    def SavePayment(self):
        self.driver.find_element_by_id(self.button_SavePayment).click()





