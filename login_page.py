from homepage import HomePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.check_page_loaded()
        self.isPasswordIncorrect = False

    def loginAs(self, username, password):
        self.enter_account(username)
        self.enter_passwd(password)
        self.submit()
        return HomePage(self.driver)

    def loginError(self, username, password):
        # fixme
        self.enter_account(username)
        self.enter_passwd(password)
        self.submit()
        self.check_error_message()
        return self

    def check_page_loaded(self):
        # if not self.driver.find_element(*LoginPageLocators.USER):
        #     raise Exception('login page is not loaded')
        try:
            self.driver.find_element(*LoginPageLocators.USER)
        except NoSuchElementException:
            raise Exception('Login page is not loaded')

    def enter_account(self, username):
        self.driver.find_element(*LoginPageLocators.USER).send_keys(username)
        return self

    def enter_passwd(self, password):
        pwd = self.driver.find_element(*LoginPageLocators.PWD)
        pwd.send_keys(password)
        return self

    def check_error_message(self):
        error_message = self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE)
        if WebDriverWait(self.driver, 5).until(EC.visibility_of(error_message)):
            self.isPasswordIncorrect = True

    def submit(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()


class LoginPageLocators:
    USER = (By.ID, 'uid')
    PWD = (By.ID, 'pwd')
    LOGIN_BTN = (By.ID, 'login-btn')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'div.alert.ng-isolate-scope.alert-error')
