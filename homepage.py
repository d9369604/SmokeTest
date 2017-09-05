# -*- coding: utf-8 -*-
import re
from test_data import LoginTestData
from test_data import HomePageTestData
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.isLoggedin()

    def isLoggedin(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(HomePageLocators.MORE_ICON)
        )

    def check_page_loaded(self):
        return self.driver.find_element(*HomePageLocators.MORE_ICON)

    def check_user_name(self):
        name = self.driver.find_element(*HomePageLocators.USER_NAME)
        account = LoginTestData.ACCOUNT.split('@')[0]
        return True if name.text == account else False

    def check_app_icon(self):
        return self.img_compare(HomePageTestData.HOMEPAGE_IMG, HomePageTestData.HOMEPAGE_ICON)

    def check_slider_elem_visible(self):
        if not self.wait_visible(self.driver.find_element(*HomePageLocators.SLIDER)):
            return False
        if not self.wait_visible(self.driver.find_element(*HomePageLocators.CAROUSEL)):
            return False
        return True

    def check_new_song_img_visible(self):
        elem = self.driver.find_element(*HomePageLocators.NEW_SONG)
        img = elem.find_element_by_tag_name('img')
        return self.check_img_visible(img)

    def check_slider_img_visible(self):
        # slider has two focus
        slider_focus = self.find_elements(*HomePageLocators.SLIDER_FOCUS)
        for slider in slider_focus:
            img = slider.find_element_by_tag_name('img')
            if not self.check_img_visible(img):
                return False
        return True

    def click_slider_btn(self, locator):
        btn = self.find_element(*locator)
        self.click_hidden_elem(btn)

    def get_slider_focus_x_location(self):
        slides = self.driver.find_element(*HomePageLocators.SLIDER_LIST)
        # width: 4800%; transition-duration: 0.6s; transform: translate3d(-456px, 0px, 0px);
        pattern = re.compile('.*translate3d\((.*)px, 0px, 0px\);')
        location = pattern.match(slides.get_attribute('style')).group(1)
        return location

    def get_focus_index(self):
        slides = self.driver.find_element(*HomePageLocators.SLIDER_LIST)
        slide_list = slides.find_elements_by_tag_name('li')
        index = 0
        for idx, slide in enumerate(slide_list):
            if slide.get_attribute('class') == HomePageTestData.SLIDER_FOCUS_CLASS_NAME:
                index = idx
                break
        return index

    def slider_focus_action(self, locator):
        init_idx = self.get_focus_index()
        init_pos = self.get_slider_focus_x_location()
        for i in range(3):
            self.click_slider_btn(locator)
            if not self.check_slider_img_visible():
                return False
            sleep(1)
        end_idx = self.get_focus_index()
        end_pos = self.get_slider_focus_x_location()
        if locator[1] == HomePageTestData.SLIDER_R_BTN:
            return True if end_idx - init_idx == 3 and end_pos < init_pos else False
        else:
            return True if init_idx - end_idx == 3 and end_pos > init_pos else False

    def check_slider_focus_action(self):
        actions = [HomePageLocators.SLIDER_R_BTN, HomePageLocators.SLIDER_L_BTN]
        for act in actions:
            if not self.slider_focus_action(act):
                return False
        return True

    def check_topic_status(self):
        topics = self.driver.find_element_by_tag_name('ol')
        topic_list = topics.find_elements_by_tag_name('li')
        for topic in topic_list:
            cover = topic.find_element_by_class_name('cover')
            img = cover.find_element_by_tag_name('img')
            if not self.check_img_visible(img):
                return False
            # info = topic.find_element_by_class_name('height-wrap').text
            info = topic.find_element_by_class_name('height-wrap')
            link = info.find_element_by_tag_name('a')
            if not self.wait_visible(link):
                return False
            sharer = topic.find_element_by_class_name('playlist-sharer')
            sharer_img = sharer.find_element_by_tag_name('img')
            if not self.check_img_visible(sharer_img):
                return False
            share_name = topic.find_element_by_css_selector('div.name.item-h')
            share_name_link = share_name.find_element_by_tag_name('a')
            if not self.wait_visible(share_name_link):
                return False
        return True

    def check_genres(self):
        genres = self.driver.find_element(*HomePageLocators.GENRES)
        genres_list = genres.find_elements_by_tag_name('li')
        if not genres_list[0].get_attribute('class') == 'ng-scope active':
            return False
        for idx, genre in enumerate(genres_list):
            if idx > 0:
                genre.click()
                sleep(1)
            if not genre.get_attribute('class') == 'ng-scope active':
                return False
            genre_previews = self.driver.find_element(*HomePageLocators.GENRES_PREVIEWS)
            album_list = genre_previews.find_elements_by_tag_name('li')
            for album in album_list:
                img = album.find_element_by_tag_name('img')
                if not self.check_img_visible(img):
                    return False
        return True


class HomePageLocators:
    MORE_ICON = (By.XPATH, "//button[@class='btn-more pull-right ng-binding ng-scope']")
    MY_MUSIC_ICON = (By.LINK_TEXT, u'我的音樂庫')
    USER_NAME = (By.CSS_SELECTOR, 'span.user-name.ng-binding')
    SLIDER = (By.ID, 'slider')
    CAROUSEL = (By.ID, 'carousel')
    SLIDER_FOCUS = (By.CSS_SELECTOR, 'li.ng-scope.flex-active-slide')
    SLIDER_LIST = (By.CLASS_NAME, 'slides')
    SLIDER_R_BTN = (By.CLASS_NAME, 'flex-next')
    SLIDER_L_BTN = (By.CLASS_NAME, 'flex-prev')
    NEW_SONG = (By.XPATH, "//div[@context-menu='right-main-preReleaseMode']")
    PLAY_NEW_SONG = (By.XPATH, "//a[@class='btn-play ng-scope']")
    GENRES = (By.CLASS_NAME, 'genres')
    GENRES_PREVIEWS = (By.CSS_SELECTOR, 'ul.cards.ng-scope')
