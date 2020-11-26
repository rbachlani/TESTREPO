import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class readConfig:
    @staticmethod
    def getDesiredCapabilities():
        desired_cap=config.get('common info','desired_cap')
        return desired_cap
    @staticmethod
    def getServerurl():
        serverurl=config.get('common info','serverurl')
        return serverurl
    @staticmethod
    def getEmailaddress():
        emailaddress = config.get('common info', 'emailaddress')
        return emailaddress

    @staticmethod
    def getFirstname():
        firstname = config.get('common info', 'firstname')
        return firstname

    @staticmethod
    def getLastname():
        lastname = config.get('common info', 'lastname')
        return lastname

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getConfirmpassword():
        confirmpassword = config.get('common info', 'confirmpassword')
        return confirmpassword