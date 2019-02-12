import allure
import unittest

import time

from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupRegistration
from POM.user import PaymentnotMailRu
from POM.pageprofile import PageProfile
from POM.setUp import StartInterneturok


@allure.feature("Покупка абонемента")
@allure.story("Регистрация, покупка абонемента за 900 рублей с вкл автоплатежом")
class CreateAccountAndBuyTicket900YesAutoPayment(StartInterneturok):
    def test_buy_ticket_per_900_rubles(self):
        driver = self.driver
        steps_main = MainPage(driver)
        steps_user = PaymentnotMailRu(driver)
        steps_popup = PopupRegistration(driver)
        steps_in_profile = PageProfile(driver)

        with allure.step("Нажать на кнопку Войти"):
            steps_main.go_to_sgnIn()
        with allure.step("В поп-апе регистрации нажать Зарегистрироваться"):
            steps_popup.go_to_popup_registration()
        with allure.step("Ввожу email=payment.not@mail.ru/password=123456"):
            steps_user.reg_enter_email()
            steps_user.reg_enter_password()
        with allure.step("Нажать на кнопку Зарегистрироваться"):
            steps_popup.click_sign_up()
        with allure.step("Перейти в мой профиль"):
            steps_in_profile.go_to_my_profile()
        with allure.step("В ЛК, в виджете абонемент нажать на кнопку оплатить абонемент"):
            steps_in_profile.click_button_buy_subscription()
        with allure.step("В поп-апе оплаты выбрать тариф 365 дней"):
            steps_in_profile.choose_subscription_365_day()
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
        with allure.step("В виджете отображается купленный абонемент с вкл автопродлением и тарифом 366 дней"):
            self.assertIn("Осталось:\n366 дней\nАвтопродление:\n\nВкл.\nПодробнее об абонементе Продлить абонемент",
                          driver.find_element_by_class_name("profile-abonement__body").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
