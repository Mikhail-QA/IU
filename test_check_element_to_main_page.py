import unittest
from Web_services.Main_page.Check_all_elements_the_home_page_is_displayed.test_пользователь_авторизован_проверка_Header import \
    ChecksAllElementsTheHeadersUserAuth
from Web_services.Main_page.Check_all_elements_the_home_page_is_displayed.test_пользователь_не_авторизован_проверка_Header import \
    ChecksAllElementsTheHeadersUserNotAuth

from Web_services.Main_page.Check_all_elements_the_home_page_is_displayed.test_попап_оставить_отзыв import CheckPopupReview

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(ChecksAllElementsTheHeadersUserNotAuth))
suite.addTest(unittest.makeSuite(CheckPopupReview))
suite.addTest(unittest.makeSuite(ChecksAllElementsTheHeadersUserAuth))