import os
import pyautogui
from opencv import compare
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """All page objects inherit from this"""

    def __init__(self, driver, url=None):
        # self._validate_page(driver)
        self.driver = driver
        self.url = url

    def navigate(self):
        self.driver.get(self.url)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def refresh(self):
        self.driver.refresh()

    def scroll_down(self, elem=None):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if not elem:
            self.driver.execute_script("window.scrollTo(0, 500);")
        else:
            elem.execute_script("window.scrollTo(0, 500);")

    def scroll_down_by_keyboard(self):
        for i in range(10):
            pyautogui.press('down')

    def click_coordinate(self, x, y):
        pyautogui.click(x, y)

    def click_elem(self, locator):
        self.driver.find_element(*locator).click()

    def click_hidden_elem(self, elem):
        self.driver.execute_script("$(arguments[0]).click();", elem)

    def check_img_visible(self, img_elem):
        self.wait_visible(img_elem)
        return self.driver.execute_script("return arguments[0].complete\
         && typeof arguments[0].naturalWidth != \"undefined\" && arguments[0].naturalWidth > 0", img_elem)

    def wait_visible(self, elem):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of(elem))

    def wait_alert(self):
        return WebDriverWait(self.driver, 5).until(EC.alert_is_present())

    def screen_shot(self, filename):
        img_file = os.path.join(os.getcwd(), 'image', filename)
        if os.path.exists(img_file):
            os.remove(img_file)
        self.driver.get_screenshot_as_file(img_file)

    def img_compare(self, filename, template):
        self.screen_shot(filename)
        img_file = os.path.join(os.getcwd(), 'image', filename)
        template_file = os.path.join(os.getcwd(), 'image', 'golden', template)
        return compare(img_file, template_file)

    def music_to(self, btn_locator, btn_hidden=False):
        icon = self.driver.find_element(*btn_locator)
        if btn_hidden:
            self.click_hidden_elem(icon)
        else:
            self.wait_visible(icon)
            icon.click()
        try:
            alert = self.wait_alert()
            alert.accept()
        except Exception:
            pass



    # @abstractmethod
    # def _validate_page(self, driver):
    #     return
    #
    # """ Region define functionality available through all page objects"""
    # @property
    # def search(self):
    #     from search import SearchRegion
    #     return SearchRegion(self.driver)


class InvalidPageException(Exception):
    """ Throw this	exception	when you don't find the correct page """
    pass

