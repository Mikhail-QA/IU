"""
Проверить наличия элементов на главной странице в Header
Пользователь не авторизован
URL: https://interneturok.ru/"	"На странице отображаются: http://joxi.ru/E2pLd3xcBvV7K2
"""
import allure
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов в Header для не авторизованного пользователя")
class ChecksAllElementsTheHeadersUserNotAuth(StartInterneturokClassMethod):
    @allure.step("Элемент Логотип отображается")
    def test_logo_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo_full.active"))

    @allure.step("Элемент Флешка отображается")
    def test_flash_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon.icon-flash"))

    @allure.step("Кнопка Войти отображается")
    def test_signIn_is_displayed(self):
        self.assertEqual(u"Войти", self.driver.find_element_by_css_selector("span.button.button_login").text)
