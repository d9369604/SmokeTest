import unittest
import time
from selenium import webdriver
from base_test_case import BaseTestCase
from login_page import LoginPage
from homepage import HomePage
from expected_result import SearchExpected
from locators import SearchLocators
from search import SearchRegion
from test_data import SearchTestData


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://play.kkbox.com/')

    def test_login_success(self):
        login_page = LoginPage(self.driver)
        homepage = login_page.loginAs('garycheng@kkbox.com', '131438')
        self.assertTrue(homepage.isLoggedin)

    def test_wrong_password(self):
        login_page = LoginPage(self.driver)
        error_page = login_page.loginError('garycheng@kkbox.com', '111')
        self.assertTrue(error_page.isPasswordIncorrect)

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
