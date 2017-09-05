from base import BasePage
from homepage import HomePage
from selenium.webdriver.common.by import By
from test_data import LoginTestData


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.check_page_loaded()

    def loginAs(self, username, password):
        self.enter_account(username)
        self.enter_passwd(password)
        self.submit()
        return HomePage(self.driver)

    def check_page_loaded(self):
        if not self.driver.find_element(*LoginPageLocators.USER):
            raise Exception('Login page not loaded')

    def enter_account(self, username):
        self.driver.find_element(*LoginPageLocators.USER).send_keys(username)
        return self

    def enter_passwd(self, password):
        pwd = self.driver.find_element(*LoginPageLocators.PWD)
        pwd.send_keys(password)
        return self

    def submit(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()


class LoginPageLocators:
    USER = (By.ID, 'uid')
    PWD = (By.ID, 'pwd')
    LOGIN_BTN = (By.ID, 'login-btn')