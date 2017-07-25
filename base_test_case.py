import unittest
from selenium import webdriver
from login_page import LoginPage


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        # cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.close()
        # pass
