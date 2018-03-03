"""
Проверить наличия элементов на главной странице в Header
Пользователь авторизован
URL: https://interneturok.ru/"	На странице отображаются: http://joxi.ru/8AnW6anuqN8BPr
"""

import allure
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu


class ChecksAllElementsTheHeadersUserAuth(StartInterneturokClassMethod):
    def test_001_go(self):
        StartInterneturokClassMethod = self.driver
        steps_main = MainPage(StartInterneturokClassMethod)
        steps_user = AutopaymentMailRu(StartInterneturokClassMethod)
        steps_popup = PopupSignIn(StartInterneturokClassMethod)

        steps_main.go_to_sgnIn()
        steps_user.enter_email()
        steps_user.enter_password()
        steps_popup.click_button_login()

    @allure.step("Логотип отображается")
    def test_logo_interneturok(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo_full.active"))

    @allure.step("Флешка отображается")
    def test_flash(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon.icon-flash"))

    @allure.step("Кнопка Мой профиль отображается")
    def test_signIn(self):
        self.assertEqual(u"Мой профиль", self.driver.find_element_by_css_selector("div.header__menu_profile").text)
