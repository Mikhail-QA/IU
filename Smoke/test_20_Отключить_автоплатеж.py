import allure
import time
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.pageprofile import PageProfile
from POM.user import VratchGlavYandexRu


@allure.feature("Отключить автоплатёж")
@allure.story("Пользовательм оставить отзыв и убедиться приходу отзыва на почту Менеджера ИУ")
class DisableAutoPayment(StartInterneturok):
    def test_user_off_auto_payment(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = VratchGlavYandexRu(driver)
        profile_steps = PageProfile(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email/password"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти в ЛК"):
            profile_steps.go_to_my_profile()
            time.sleep(1)
        with allure.step("В виджете абонемент нажать на кнопку Выкл автоплатёж"):
            profile_steps.click_button_off_autopayment()
            time.sleep(1.5)
        with allure.step("В появившемся тултипе нажать на кнопку ДА"):
            profile_steps.click_in_popup1_off_autopayment()
        with allure.step("В появившемся поп-апе нажать на кнопку ДА"):
            profile_steps.click_in_popup2_off_autopayment()
        with allure.step("Обновить страницу"):
            self.driver.refresh()
        with allure.step("В ЛК, в виджете абонемента статус автоплатежа поменялся на ВЫКЛ"):
            assert (u"Выкл.", self.driver.find_element_by_css_selector("a.link_dotted").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
