import unittest
import allure
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.setUp import StartInterneturok
from POM.user import AutopaymentMailRu


@allure.feature("Авторизация/Регистрация")
@allure.story("Авторизоваться пользователем и убедиться что пользователь может выйти из учётной записи")
class CheckingOutProfile(StartInterneturok):
    def test_click_button_exit(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = AutopaymentMailRu(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email=autopayment@mail.ru/password=123456"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Навести курсор мышки на кнопку Мой профиль"):
            main_steps.hover_mouse_to_button_my_profile()
        with allure.step("В открытом списке вкладок Мой профиль нажать на кнопку Выйти"):
            main_steps.click_button_exit_in_tab_my_profile()
        with allure.step("После выхода из ЛК кнопка называется Войти"):
            self.assertEqual(u"Войти", driver.find_element_by_css_selector("span.button_login").text)
        with allure.step("Обновить страницу"):
            self.driver.refresh()
        with allure.step("Для не авторизованного пользователя отображается кнопка Войти"):
            self.assertEqual(u"Войти", driver.find_element_by_css_selector("span.button_login").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
