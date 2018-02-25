import unittest
from Checks_PopUp_in_lesson_paid.User_not_auth.test_1_Платный_урок_проверка_через_все_места import \
    CheckAppearancePopUpInAllPlaces
from Checks_PopUp_in_lesson_paid.User_not_auth.test_2_Платный_урок_проверка_через_кнопку_Оплатить_абонемент import \
    ClickButtonBuyTicketInPayLesson
from Checks_PopUp_in_lesson_paid.User_not_auth.test_3_Платный_урок_проверка_через_кнопку_Войти import \
    ClickButtonSignInPayLesson

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(CheckAppearancePopUpInAllPlaces))
suite.addTest(unittest.makeSuite(ClickButtonBuyTicketInPayLesson))
suite.addTest(unittest.makeSuite(ClickButtonSignInPayLesson))
