# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


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


class MyMusicLocators:
    TITLE = (By.CSS_SELECTOR, 'h2.section-title.ng-binding')
    FAVORITE_IMG = (By.XPATH, "//img[@src='assets/images/my-favorite-cover.png']")
    SONG = (By.LINK_TEXT, 'back to black')
    PLAY_ICON_ON_SONG_PAGE = (By.CSS_SELECTOR, 'i.icon.icon-40.icon-40-headerplay')
    PAUSE_ICON_ON_PLAYER = (By.ID, 'pauseBtn')
    PLAY_ICON_ON_PLAYER = (By.ID, 'playBtn')
    PLAYER_BAR = (By.ID, 'playBar')


class LoginPageLocators:
    USER = (By.ID, 'uid')
    PWD = (By.ID, 'pwd')


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
