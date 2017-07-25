import unittest
import audio_record
from base_test_case import BaseTestCase
from login_page import LoginPage
from homepage import HomePage
from locators import HomePageLocators
from locators import MyMusicLocators
from my_music import MyMusic


class PlayFuncTest(BaseTestCase):
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

    def test_case_3_enter_my_music_library(self):
        home_page = HomePage(self.driver)
        home_page.click_elem(HomePageLocators.MY_MUSIC_ICON)
        my_music = MyMusic(self.driver)
        self.assertTrue(my_music.check_page_loaded())
        self.assertTrue(home_page.img_compare('my_music.png', 'music_player.png'))

    def test_case_4_play_music(self):
        my_music = MyMusic(self.driver)
        my_music.play_music()
        self.assertTrue(my_music.check_icon_visible(MyMusicLocators.PAUSE_ICON_ON_PLAYER))
        self.assertTrue(my_music.img_compare('play_music.png', 'album_previews.png'))
        self.assertTrue(my_music.check_player_status('play'))

    def test_case_5_pause_play(self):
        my_music = MyMusic(self.driver)
        my_music.click_elem(MyMusicLocators.PAUSE_ICON_ON_PLAYER)
        self.assertTrue(my_music.check_player_status('pause'))
        my_music.click_elem(MyMusicLocators.PLAY_ICON_ON_PLAYER)
        self.assertTrue(my_music.check_player_status('play'))

    # def test_case_6_record_audio(self):
    #     audio_record.record()

if __name__ == '__main__':
    unittest.main(verbosity=2)
