from homepage import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://play.kkbox.com/')
        self.check_page_loaded()

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
        return self

    def isPasswordIncorrect(self):
        return self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE)

    def check_page_loaded(self):
         WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'uid'))
         )

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
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'div.alert.ng-isolate-scope.alert-error')
