# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from kkbox_builder import KKBOXBuilder


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver
        cls.kkbox = KKBOXBuilder(cls.driver)\
            .browser('chrome')\
            .maximizeWindow()\
            .login('garycheng@kkbox.com', '131438')\
            .goto('Search')\
            .build()

    def testSearchLinkinParkAndPlay(self):
        song_name = self.kkbox\
            .search("Linkin Park")\
            .selectArtist(0)\
            .play(0)\
            .getSongName()
        self.assertEqual(song_name, u"What I've Done (Album Version)(過去的我)")

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.kkbox.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
