import unittest
from base_test_case import BaseTestCase
from login_page import LoginPage
from homepage import HomePage
from expected_result import SearchExpected
from locators import SearchLocators
from search import SearchRegion
from test_data import SearchTestData


class SearchTest(BaseTestCase):

    def test_case_1_login_page_loaded(self):
        page = LoginPage(self.driver)
        page.navigate()
        self.assertTrue(page.check_page_loaded())

    def test_case_2_login(self):
        page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        page.enter_account()
        page.enter_pwd_and_submit()
        self.assertTrue(home_page.check_page_loaded())

    def test_case_3_search_nothing(self):
        search_region = SearchRegion(self.driver)
        search_region.search_nothing()
        self.assertEqual(SearchExpected.ALERT_INFO, search_region.alert_info)
        search_region.close_alert_info()
        self.assertTrue(search_region.check_alert_status(), 'alert info still there')

    def test_case_4_search_special_character(self):
        search_region = SearchRegion(self.driver)
        search_region.search_for('!')
        self.assertIn(SearchExpected.ARTISTS_NO_MATCH, self.driver.page_source)

    def test_case_5_previews_search_result(self):
        search_region = SearchRegion(self.driver)
        search_region.refresh()
        search_region.just_enter(SearchTestData.ARTIST)
        self.assertTrue(search_region.check_titles(
            SearchLocators.PREVIEWS_TITLE, SearchExpected.PREVIEWS_TITLE))
        self.assertTrue(search_region.img_compare(
            'search_previews.png', 'golden_previews.png'))

    def test_case_6_search_artist(self):
        search_region = SearchRegion(self.driver)
        search_region.refresh()
        search_region.search_for(SearchTestData.ARTIST)
        self.assertTrue(search_region.check_search_result_info(SearchTestData.ARTIST))
        self.assertTrue(search_region.check_titles(
            SearchLocators.RESULT_TITLE, SearchExpected.RESULT_TITLE))
        self.assertTrue(search_region.img_compare(
            'search_result.png', 'artists_img.png'
        ))
        self.assertTrue(search_region.check_song_list(
            SearchLocators.SONG_LIST, SearchExpected.SONG_NUM, SearchExpected.SONG_INFO
        ))



if __name__ == '__main__':
    unittest.main(verbosity=2)
