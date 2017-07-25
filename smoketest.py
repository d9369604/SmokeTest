import unittest
from search_test import SearchTest
from play_funtionality_test import PlayFuncTest
from homepage_test import HomePageTest

# get all tests
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
play_fun_test = unittest.TestLoader().loadTestsFromTestCase(PlayFuncTest)
homepage_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suit combining above tests
smoke_tests = unittest.TestSuite([search_test, play_fun_test, homepage_test])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(smoke_tests)