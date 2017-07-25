import unittest
from base_test_case import BaseTestCase
from login_page import LoginPage
from homepage import HomePage
from locators import HomePageLocators
from locators import MyMusicLocators
from my_music import MyMusic


class HomePageTest(BaseTestCase):

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

    def test_case_3_check_UI(self):
        homepage = HomePage(self.driver)
        self.assertTrue(homepage.check_user_name())
        self.assertTrue(homepage.check_app_icon())

    def test_case_4_check_slider_visible(self):
        homepage = HomePage(self.driver)
        self.assertTrue(homepage.check_slider_elem_visible())
        self.assertTrue(homepage.check_slider_img_visible())

    def test_case_5_check_slider_action(self):
        homepage = HomePage(self.driver)
        self.assertTrue(homepage.check_slider_focus_action())

    def test_case_6_check_new_songs(self):
        homepage = HomePage(self.driver)
        music = MyMusic(self.driver)
        self.assertTrue(homepage.check_new_song_img_visible())
        homepage.music_to(HomePageLocators.PLAY_NEW_SONG, btn_hidden=True)
        self.assertTrue(music.check_player_status('play'))
        homepage.music_to(MyMusicLocators.PAUSE_ICON_ON_PLAYER)

    def test_case_7_topic(self):
        homepage = HomePage(self.driver)
        homepage.click_coordinate(108, 170)
        homepage.scroll_down_by_keyboard()
        self.assertTrue(homepage.check_topic_status())

    def test_case_8_new_release(self):
        homepage = HomePage(self.driver)
        homepage.scroll_down_by_keyboard()
        self.assertTrue(homepage.check_genres())

if __name__ == '__main__':
    unittest.main(verbosity=2)
