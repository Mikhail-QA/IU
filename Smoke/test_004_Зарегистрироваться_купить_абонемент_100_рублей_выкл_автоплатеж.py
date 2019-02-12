import allure
import unittest

import time

from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupRegistration
from POM.user import PaymNotYandexRu
from POM.pageprofile import PageProfile


@allure.feature("Покупка абонемента")
@allure.story("Регистрация, покупка абонемента за 100 рублей с выкл автоплатежом")
class CreateAccountAndBuyTicket100NoAutoPayment(StartInterneturok):
    def test_buy_ticket_per_100_rubles(self):
        driver = self.driver
        steps_main_page = MainPage(driver)
        steps_popup = PopupRegistration(driver)
        steps_user = PaymNotYandexRu(driver)
        steps_in_profile = PageProfile(driver)
        with allure.step("Нажать на кнопку Войти"):
            steps_main_page.go_to_sgnIn()
        with allure.step("В поп-апе регистрации нажать Зарегистрироваться"):
            steps_popup.go_to_popup_registration()
        with allure.step("Ввожу email/password = paym.not@yandex.ru"):
            steps_user.reg_enter_email()
            steps_user.reg_enter_password()
        with allure.step("Нажать на кнопку Зарегистрироваться"):
            steps_popup.click_sign_up()
        with allure.step("Перейти в мой профиль"):
            steps_in_profile.go_to_my_profile()
        with allure.step("В ЛК, в виджете абонемент нажать на кнопку оплатить абонемент"):
            steps_in_profile.click_button_buy_subscription()
        with allure.step("В поп-апе оплаты отключить автоплатеж"):
            steps_in_profile.popup_click_enable_autopayment()
        with allure.step("В поп-апе оплаты нажать на кнопку Оплатить абонемент"):
            steps_in_profile.popup_click_buy_subscription()
        with allure.step("На сайте ЯК ввести данные карты"):
            steps_in_profile.enter_data_card()
        with allure.step("Вернулся в Мой профиль"):
            steps_in_profile.go_to_my_profile()
            time.sleep(30)
        with allure.step("Обновить страницу"):
            self.driver.refresh()
            assert (self.driver.find_element_by_css_selector(".profile-abonement__row:nth-child(1)"))
        with allure.step("В виджете отображается купленный абонемент без автоплатежа с тарифом 31 день"):
            self.assertIn("Осталось:\n31 день\nАвтопродление:\nВыкл.\nПодробнее об абонементе Продлить абонемент",
                          driver.find_element_by_class_name("profile-abonement__body").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
