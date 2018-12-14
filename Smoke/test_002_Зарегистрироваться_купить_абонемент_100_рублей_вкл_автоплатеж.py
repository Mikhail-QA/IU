import allure
import unittest

import time

from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupRegistration
from POM.user import VratchGlavYandexRu
from POM.pageprofile import PageProfile
from POM.setUp import StartInterneturok


@allure.feature("Покупка абонемента")
@allure.story("Регистрация, покупка абонемента за 100 рублей с вкл автоплатежом")
class CreateAccountAndBuyTicket100YesAutoPayment(StartInterneturok):
    def test_buy_ticket_per_100_rubles(self):
        driver = self.driver
        steps_main = MainPage(driver)
        steps_user = VratchGlavYandexRu(driver)
        steps_popup = PopupRegistration(driver)
        steps_in_profile = PageProfile(driver)

        with allure.step("Нажать на кнопку Войти"):
            steps_main.go_to_sgnIn()
        with allure.step("В поп-апе регистрации нажать Зарегистрироваться"):
            steps_popup.go_to_popup_registration()
        with allure.step("Ввожу email=vratch.glav@yandex.ru/password=123456"):
            steps_user.reg_enter_email()
            steps_user.reg_enter_password()
        with allure.step("Нажать на кнопку Зарегистрироваться"):
            steps_popup.click_sign_up()
        with allure.step("Перейти в мой профиль"):
            steps_in_profile.go_to_my_profile()
        with allure.step("В ЛК, в виджете абонемент нажать на кнопку оплатить абонемент"):
            steps_in_profile.click_button_buy_subscription()
        with allure.step("В поп-апе оплаты нажать на кнопку Оплатить абонемент"):
            steps_in_profile.popup_click_buy_subscription()
        with allure.step("На сайте ЯК ввести данные карты"):
            steps_in_profile.enter_data_card()
        with allure.step("Вернулся в Мой профиль"):
            steps_in_profile.go_to_my_profile()
            time.sleep(30)
        with allure.step("Обновить страницу"):
            self.driver.refresh()
        with allure.step("В виджете отображается купленный абонемент с вкл автопродлением и тарифом 31 день"):
            self.assertIn("Осталось:\n31 день\nАвтопродление:\n\nВкл.\nПодробнее об абонементе Продлить абонемент",
                          driver.find_element_by_class_name("profile-abonement__body").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
