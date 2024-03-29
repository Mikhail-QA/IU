"""
Проверить наличия элементов на странице Алгебра 8 класс в Header
Пользователь авторизован
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://joxi.ru/82Q0wVOH13jPlm
"""
import allure
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.main_page import MainPage
from Web_services.URL import SubjectPage


@allure.feature("Страница Предмет-Класс (Алгебра 11 класс)")
@allure.story("Проверка наличия элементов в Header для авторизованного пользователя")
class ChecksAllElementsInSubjectPageTheHeadersUserAuth(StartInterneturokClassMethod):
    @allure.step("Авторизоваться пользователем")
    def test_000_logged_user(self):
        StartInterneturokClassMethod = self.driver
        steps_main = MainPage(StartInterneturokClassMethod)
        steps_user = AutopaymentMailRu(StartInterneturokClassMethod)
        steps_popup = PopupSignIn(StartInterneturokClassMethod)
        go_page = SubjectPage(StartInterneturokClassMethod)
        steps_main.go_to_sgnIn()
        steps_user.enter_email()
        steps_user.enter_password()
        steps_popup.click_button_login()
        go_page.go_algebra_8_grade()

    @allure.step("Элемент Логотип отображается")
    def test_logo_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo.header__logo"))

    @allure.step("Кнопка Предметы отображается")
    def test_button_subjects_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.header-menu-grades"))

    @allure.step("Кнопка Классы отображается")
    def test_button_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.header-menu-subjects"))

    @allure.step("Элемент Поиск отображается")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    @allure.step("Кнопка Мой профиль отображается")
    def test_button_signIn_is_displayed(self):
        self.assertEqual(u"Мой профиль", self.driver.find_element_by_css_selector("div.header__menu_profile").text)

    @allure.step("Кнопка меню-бургер отображается")
    def test_button_signIn_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.header-userlinks_trigger"))
