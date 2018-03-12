"""
Проверить наличия элементов на странице Алгебра 8 класс в  Header
Пользователь не авторизован
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://joxi.ru/vAWbBDLHkK1YM2
"""

from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod


class ChecksAllElementsTheHeadersUserNotAuth(StartInterneturokClassMethod):
    def test_001_open_page(self):
        self.driver.get("https://fast-staging.interneturok.ru/algebra/8-klass")

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
        self.assertEqual(u"Войти", self.driver.find_element_by_css_selector("span.button_login").text)
