import time
from base import BasePage
from locators import SearchLocators
from expected_result import SearchExpected
# from test_data import SearchTestData
from selenium.common.exceptions import NoSuchElementException


class SearchRegion(BasePage):

    def search_for(self, item):
        self.driver.find_element(*SearchLocators.SEARCH_FORM).send_keys(item)
        self.driver.find_element(*SearchLocators.SEARCH_BTN).click()
        self.driver.find_element(*SearchLocators.SEARCH_MESSAGE)

    def search_nothing(self):
        self.driver.find_element(*SearchLocators.SEARCH_BTN).click()
        # time to let info appear
        time.sleep(1)

    def just_enter(self, item):
        self.driver.find_element(*SearchLocators.SEARCH_FORM).send_keys(item)
        # time to wait for pop up previews
        time.sleep(5)

    # def check_previews_titles(self):
    #     result = [elem.text in SearchExpected.PREVIEWS_TITLE
    #               for elem in self.driver.find_elements(*SearchLocators.PREVIEWS_TITLE)]
    #     return True if all(result) else False

    def check_titles(self, locator, expected):
        result = [elem.text in expected for elem in self.driver.find_elements(*locator)]
        return True if all(result) else False

    def check_search_result_info(self, item):
        result_title = self.driver.find_element(*SearchLocators.SEARCH_MESSAGE)
        return True if item in result_title.text else False

    def check_song_list(self, locator, expected_num, expected_info):
        list_elem = self.driver.find_elements(*locator)
        if not self.check_song_num(list_elem, expected_num):
            return False
        if not self.check_song_info(list_elem, expected_info):
            return False
        return True

    def check_song_num(self, elem, expected):
        return True if expected == len(elem) else False

    def check_song_info(self, list_elems, expected):
        song_info = [elem for elem in list_elems
                     if elem.find_element(*SearchLocators.SONG).text == SearchExpected.SONG_NAME]
        res = [info.text in expected for info in song_info]
        return True if all(res) else False

    def close_alert_info(self):
        self.driver.find_element(*SearchLocators.ALERT_CLOSE_BTN).click()
        # time to let info disappear
        time.sleep(2)

    def check_alert_status(self):
        try:
            self.driver.find_element(*SearchLocators.ALERT_INFO)
            return False
        except NoSuchElementException:
            return True

    @property
    def alert_info(self):
        alert_info = self.driver.find_element(*SearchLocators.ALERT_INFO)
        return alert_info.text
