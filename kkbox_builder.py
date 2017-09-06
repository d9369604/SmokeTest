from login_page import LoginPage
from search_page import SearchPage


class KKBOXBuilder:
    def __init__(self, driver):
        self.driver = driver
        self.browser_type = None
        self.maximize_window = None
        self.login_tag = None
        self.user = None
        self.pwd = None
        self.goto_page = None
        self.close_browser = None

    def browser(self, browser_type):
        self.browser_type = browser_type
        return self

    def maximizeWindow(self):
        self.maximize_window =True
        return self

    def login(self, username, password):
        self.user = username
        self.pwd = password
        self.login_tag = True
        return self

    def goto(self, page):
        self.goto_page = page
        return self

    def build(self):
        if self.browser_type.lower() == 'chrome':
            self.driver = self.driver.Chrome()

        if self.maximize_window:
            self.driver.maximize_window()

        if self.login_tag:
            LoginPage(self.driver).loginAs(self.user, self.pwd)

        if self.goto_page:
            if self.goto_page.lower() == 'search':
                return SearchPage(self.driver)
