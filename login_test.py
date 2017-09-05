import unittest
from base_test_case import BaseTestCase
from login_page import LoginPage
from homepage import HomePage
from expected_result import SearchExpected
from locators import SearchLocators
from search import SearchRegion
from test_data import SearchTestData


class LoginTest(BaseTestCase):

    def test_login_success(self):
        login_page = LoginPage(self.driver)
        homepage = login_page.loginAs(username, password)
        self.assertTrue(homepage.isLoggedin)

    def test_wrong_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_account(username)
        login_page.enter_passwd("123")
        homepage = login_page.submit()
        self.assertFalse(homepage.isLoggedin)

if __name__ == '__main__':
    unittest.main(verbosity=2)
