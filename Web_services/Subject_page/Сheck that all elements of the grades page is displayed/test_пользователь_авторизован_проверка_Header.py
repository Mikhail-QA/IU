"""
Проверить наличия элементов на странице Алгебра 8 класс в Header
Пользователь авторизован
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://joxi.ru/82Q0wVOH13jPlm
"""
from selenium.webdriver.common.by import By
from Interneturok.web_services.app.SetUp import StartInterneturokClassMethod
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.main_page import MainPage


class ChecksAllElementsTheHeadersUserNotAuth(StartInterneturokClassMethod):
    def test_001_go(self):
        StartInterneturokClassMethod = self.driver
        steps_main = MainPage(StartInterneturokClassMethod)
        steps_user = AutopaymentMailRu(StartInterneturokClassMethod)
        steps_popup = PopupSignIn(StartInterneturokClassMethod)
        steps_main.go_to_sgnIn()
        steps_user.enter_email()
        steps_user.enter_password()
        steps_popup.click_button_login()

    def test_002_open_page(self):
        self.driver.get("https://staging.interneturok.ru/algebra/8-klass")

    def test_logo_interneturok(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo.header__logo"))

    def test_button_subjects_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//header/div[1]/div[2]"))

    def test_button_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//header/div[1]/div[1]"))

    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.header-search__wraps"))

    def test_flash(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon-flash"))

    def test_signIn(self):
        self.assertEqual(u"Мой профиль", self.driver.find_element_by_css_selector("div.header__menu_profile").text)
