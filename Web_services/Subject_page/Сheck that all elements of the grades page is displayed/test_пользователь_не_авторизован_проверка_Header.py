"""
Проверить наличия элементов на странице Алгебра 8 класс в  Header
Пользователь не авторизован
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://joxi.ru/vAWbBDLHkK1YM2
"""

import allure
from selenium.webdriver.common.by import By
from Web_services.Subject_page.URL import UrlLesson
from Web_services.app.SetUp import StartInterneturokClassMethod


@allure.feature("Страница Предмет-Класс (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов в Header для не авторизованного пользователя")
class ChecksAllElementsTheHeadersUserNotAuth(StartInterneturokClassMethod):
    @allure.step("Авторизоваться пользователем")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = UrlLesson(StartInterneturokClassMethod)
        go_page.go_algebra_8_grade()

    @allure.step("Элемент Логотип отображается")
    def test_logo_interneturok(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo.header__logo"))

    @allure.step("Кнопка Предметы отображается")
    def test_button_subjects_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//header/div[1]/div[2]"))

    @allure.step("Кнопка Классы отображается")
    def test_button_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//header/div[1]/div[1]"))

    @allure.step("Элемент Поиск отображается")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.header-search__wraps"))

    @allure.step("Кнопка Флешка отображается")
    def test_button_flash(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon-flash"))

    @allure.step("Кнопка Войти отображается")
    def test_button_enter_is_displayed(self):
        self.assertEqual(u"Войти", self.driver.find_element_by_css_selector("span.button_login").text)
