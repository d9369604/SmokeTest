# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from login_page import LoginPage
from search import SearchRegion


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #login
        cls.driver = webdriver.Chrome()
        LoginPage(cls.driver).loginAs('garycheng@kkbox.com', '131438')

    def testSearchLinkinParkAndPlay(self):
        song_name = SearchRegion(self.driver)\
            .search("Linkin Park")\
            .selectArtist(0)\
            .play(0)\
            .getSongName()
        self.assertEqual(song_name, u"What I've Done (Album Version)(過去的我)")

    @classmethod
    def tearDownClass(cls):
        # quit browser
        time.sleep(3)
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
