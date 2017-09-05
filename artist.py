# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Artist:
    def __init__(self, driver):
        self.driver = driver
        self.check_page_load()
        self.song_playing = None

    def check_page_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ArtistLocator.PLAY_BTN)
        )

    def play(self, index):
        songs_name = self.driver.find_elements(*ArtistLocator.SONGS_NAME)
        song = songs_name[index]
        ActionChains(self.driver).move_to_element(song).double_click(song).perform()
        self.song_playing = songs_name[index]
        return self

    def getSongName(self):
        return self.song_playing.text


class ArtistLocator:
    PLAY_BTN = (By.CSS_SELECTOR, 'i.icon.icon-28.icon-28-b-play')
    SONGS = (By.CSS_SELECTOR, 'div.')
    SONGS_NAME = (By.XPATH, "//a[@ng-bind='::hotSong.song_name']")
