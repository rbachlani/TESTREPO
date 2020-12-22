



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
    menu_AccountInfo="com.km.emotika:id/tvAccountInfo"
    SubMenu_ChangeName="com.km.emotika:id/tvName"
    txt_FirstName="com.km.emotika:id/etFirstName"
    txt_LastName="com.km.emotika:id/etLastName"
    btn_Save="com.km.emotika:id/tvSave"
    lbl_Email="com.km.emotika:id/tvEmail"
    SubMenu_ChangePassword="com.km.emotika:id/tvChangePassword"
    txt_OldPassword="com.km.emotika:id/etTemporaryPassword"
    txt_NewPassword="com.km.emotika:id/etNewPassword"
    txt_ConfirmPassword="com.km.emotika:id/etConfirmPassword"
    btn_ConfirmPasswordChange="com.km.emotika:id/tvConfirm"
    btn_flipNotifications="com.km.emotika:id/cbSetting"
    menu_TransactionHistory="com.km.emotika:id/tvTransactionHistory"
    btn_goBack="com.km.emotika:id/ivback"
    Menu_TermsAndConditions="com.km.emotika:id/tvTermCondition"
    Menu_PrivacyPolicy="com.km.emotika:id/tvPrivacyPolicy"
    Menu_Support="com.km.emotika:id/tvSupport"
    Menu_FriendInvite="com.km.emotika:id/tvInviteFriend"
    btn_CopyLink="com.km.emotika:id/tvCopyLink"
    btn_ok="com.km.emotika:id/tvOk"
    btn_Share="com.km.emotika:id/llShare"
    btn_Sms="//hierarchy/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[6]/android.widget.TextView[1]"
    txt_RecipientsName="com.android.mms:id/compose_recipients_name"
    btn_Send="com.android.mms:id/send_button"
    btn_Logout="com.km.emotika:id/tvLogout"
    btn_ContactUs="com.km.emotika:id/tvContactUs"
    btn_ShareFeedBack="com.km.emotika:id/tvShareFeedback"
    btn_ReportProblem="	com.km.emotika:id/tvReporProblem"
    btn_Cancel="com.km.emotika:id/tvCancel"

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





