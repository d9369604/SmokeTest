import time
from expected_result import SearchExpected
from artist_page import ArtistPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def search(self, item):
        self.driver.find_element(*SearchLocators.SEARCH_FORM).send_keys(item)
        self.driver.find_element(*SearchLocators.SEARCH_BTN).click()
        return self

    def selectArtist(self, index):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SearchLocators.ARTISTS)
        )
        self.driver.find_elements(*SearchLocators.ARTISTS)[index].click()
        return ArtistPage(self.driver)

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

class SearchLocators:
    SEARCH_BTN = (By.ID, 'search_btn_cnt')
    SEARCH_FORM = (By.XPATH, "//input[@class='search_hint ng-pristine ng-untouched ng-valid']")
    SEARCH_MESSAGE = (By.CSS_SELECTOR, 'h5.message.ng-binding')
    ALERT_INFO = (By.XPATH, "//div[@ng-show='!$messageTemplate']")
    ALERT_CLOSE_BTN = (By.CLASS_NAME, 'cg-notify-close')
    PREVIEWS_TITLE = (By.XPATH, "//a[@class='catlb ui-corner-all ng-binding']")
    RESULT_TITLE = (By.CSS_SELECTOR, 'h2.section-title.ng-binding')
    SONG_LIST = (By.XPATH, "//tr[@context-menu='right-main-songMode']")
    SONG = (By.XPATH, "//td[@class='ng-binding']")
    ARTISTS = (By.CSS_SELECTOR, 'h4.item-h.artist-name')
