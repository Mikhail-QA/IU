import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.pageprofile import PageProfile
from POM.user import PaymNotYandexRu


@allure.feature("Продлить абонемент")
@allure.story("Авторизоваться с абонементом, продлить абонемент")
class SignInAndExtendSubscription(StartInterneturok):
    def test_user_extend_subscription(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = PaymNotYandexRu(driver)
        profile_steps = PageProfile(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email=paym.not@yandex.ru/password=123456"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти в ЛК"):
            profile_steps.go_to_my_profile()
        with allure.step("В ЛК, в виджете абонемент нажать на кнопку продлить абонемент"):
            profile_steps.click_extend_subscription()
        with allure.step("В поп-апе оплаты нажать на кнопку Оплатить"):
            profile_steps.popup_click_buy_subscription()
        with allure.step("На сайте ЯК ввести данные карты"):
            profile_steps.enter_data_card()
        with allure.step("Вернуться в ЛК"):
            profile_steps.go_to_my_profile()
        with allure.step("Обновить страницу"):
            self.driver.refresh()
        with allure.step("После продления абонемента в виджете отображается дата 62 дня"):
            self.assertIn("Осталось:\n62 дня\nАвтопродление:\n\nВкл.\nПодробнее об абонементе Продлить абонемент",
                          driver.find_element_by_class_name("profile-abonement__body").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
