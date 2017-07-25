import re
from base import BasePage
from locators import MyMusicLocators
from time import sleep


class MyMusic(BasePage):

    def check_page_loaded(self):
        icon = self.driver.find_element(*MyMusicLocators.FAVORITE_IMG)
        return True if self.wait_visible(icon) else False

    def play_music(self):
        self.click_elem(MyMusicLocators.SONG)
        play_icon = self.driver.find_element(*MyMusicLocators.PLAY_ICON_ON_SONG_PAGE)
        self.wait_visible(play_icon)
        play_icon.click()
        try:
            alert = self.wait_alert()
            alert.accept()
        except Exception:
            pass

    def check_icon_visible(self, locator):
        pause_icon = self.driver.find_element(*locator)
        return True if self.wait_visible(pause_icon) else False

    def check_player_status(self, status):
        if status == 'play':
            if not self.check_icon_visible(MyMusicLocators.PAUSE_ICON_ON_PLAYER):
                return False
        else:
            if not self.check_icon_visible(MyMusicLocators.PLAY_ICON_ON_PLAYER):
                return True
        pattern = re.compile("width:(.*)%;")
        start = self.find_element(*MyMusicLocators.PLAYER_BAR).get_attribute('style')
        start = pattern.match(start).group(1)
        sleep(5)
        end = self.find_element(*MyMusicLocators.PLAYER_BAR).get_attribute('style')
        end = pattern.match(end).group(1)
        if status == 'play':
            return True if float(end) > float(start) else False
        else:
            return True if float(end) == float(start) else False
