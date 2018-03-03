"""
Проверить наличия элементов на главной странице в Header
Пользователь не авторизован
URL: https://interneturok.ru/"	"На странице отображаются: http://joxi.ru/E2pLd3xcBvV7K2
"""

from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod


class ChecksAllElementsTheHeadersUserNotAuth(StartInterneturokClassMethod):
    def test_logo_interneturok(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo_full.active"))

    def test_flash(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon.icon-flash"))

    def test_signIn(self):
        self.assertEqual(u"Войти", self.driver.find_element_by_class_name("button_login").text)
