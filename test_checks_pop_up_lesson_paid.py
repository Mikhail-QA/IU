import unittest
# from Checks_PopUp_in_lesson_paid.User_not_auth.test_1_Платный_урок_проверка_через_все_места import \
#     CheckAppearancePopUpInAllPlaces
# from Checks_PopUp_in_lesson_paid.User_not_auth.test_2_Платный_урок_проверка_через_кнопку_Оплатить_абонемент import \
#     ClickButtonBuyTicketInPayLesson
# from Checks_PopUp_in_lesson_paid.User_not_auth.test_3_Платный_урок_проверка_через_кнопку_Войти import \
#     ClickButtonSignInPayLesson
from Checks_PopUp_in_lesson_paid.User_without_ticket_is_logged_in.test_1_Платный_урок_проверка_через_все_места import \
    UserAuthCheckAppearancePopUpInAllPlaces
# from Checks_PopUp_in_lesson_paid.User_without_ticket_is_logged_in.test_2_Платный_урок__проверка_через_кнопку_Оплатить_абонемент import \
#     UserAuthClickButtonBuyTicketInPayLesson
# from Checks_PopUp_on_page_abonement.User_not_auth.test_1_Проверка_через_кнопку_Оплатить_абонемент import \
#     ClickButtonBuyTicketOnPageAbonement
# from Checks_PopUp_on_page_abonement.User_without_ticket_is_logged_in.test_1_Проверка_через_кнопку_Оплатить_абонемент import \
#     UserAuthClickButtonBuyTicketOnPageAbonement

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(UserAuthCheckAppearancePopUpInAllPlaces))
# suite.addTest(unittest.makeSuite(UserAuthClickButtonBuyTicketInPayLesson))
# suite.addTest(unittest.makeSuite(CheckAppearancePopUpInAllPlaces))
# suite.addTest(unittest.makeSuite(ClickButtonBuyTicketInPayLesson))
# suite.addTest(unittest.makeSuite(ClickButtonSignInPayLesson))
# suite.addTest(unittest.makeSuite(ClickButtonBuyTicketOnPageAbonement))
# suite.addTest(unittest.makeSuite(UserAuthClickButtonBuyTicketOnPageAbonement))
