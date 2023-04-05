from Pages import base_site

class BasePage(base_site):
    _username_xpath = "//*[@name='username']"
    _password_xpath = '//*[name="password"]'


    def login(self):
        pass