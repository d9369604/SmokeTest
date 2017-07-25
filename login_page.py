from base import BasePage
from locators import LoginPageLocators
from test_data import LoginTestData


class LoginPage(BasePage, object):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver, LoginTestData.URL)
        # super(LoginPage, self).__init__(driver, 'file:///C:/Users/Gary/Desktop/test.html')

    def check_page_loaded(self):
        return True if self.driver.find_element(*LoginPageLocators.USER) else False

    def enter_account(self):
        self.driver.find_element(*LoginPageLocators.USER).send_keys(LoginTestData.ACCOUNT)

    def enter_pwd_and_submit(self):
        pwd = self.driver.find_element(*LoginPageLocators.PWD)
        pwd.send_keys(LoginTestData.PWD)
        pwd.submit()
