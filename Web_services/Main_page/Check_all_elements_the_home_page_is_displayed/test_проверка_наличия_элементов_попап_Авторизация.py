"""
Проверка наличия элементов в попапе Авторизации
URL: https://interneturok.ru/users/sign_in?tab=authTab"	На странице отображаются: http://joxi.ru/gmvOq1NUxeZez2
"""

import allure
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod
from POM.main_page import MainPage


@allure.feature("Главная страница поп-ап Авторизации/Регистрации")
@allure.story("Проверка наличия элементов в поп-апе Авторизации")
class CheckPopupAuth(StartInterneturokClassMethod):
    @allure.step("Открыть поп-ап Авторизации")
    def test_001_open_popup(self):
        driver = self.driver
        steps_main = MainPage(driver)
        steps_main.go_to_sgnIn()

    @allure.step("Проверить наличие текста и элементов в popup-header, popup-switcher__wrap, popup-subtitle")
    def test_header_text_and_elements_displayed(self):
        with allure.step("В header поп-ап присутствует текст (Войдите в профиль)"):
            self.assertEqual(u"Войдите в профиль",
                             self.driver.find_element_by_css_selector("h5.popup-header__title").text)
        with allure.step("В header поп-ап присутствует кнопка крестик (закрыть)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.popup-header__close"))
        with allure.step("В элементе popup-switcher отображается текст (Вход)"):
            self.assertEqual(u"Вход", self.driver.find_element_by_link_text(u"Вход").text)
        with allure.step(
                "В поп-апе Регистрации отображается передвижной ползунок перключателя с Авторизации/Регистрации"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.switcher__button"))
        with allure.step("В элементе popup-switcher отображается текст (Регистрация)"):
            self.assertEqual(u"Регистрация", self.driver.find_element_by_link_text(u"Регистрация").text)
        with allure.step("В элементе popup-subtitle отображается текст (Быстрый вход)"):
            self.assertEqual(u"Быстрый вход",
                             self.driver.find_element_by_css_selector("span.popup-subtitle").text)

    @allure.step("Проверить наличия иконок соцсетей")
    def test_social_button_displayed(self):
        with allure.step("Отображается иконока ВК"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_vk"))
        with allure.step("Отображается иконока Одноклассники"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_od"))
        with allure.step("Отображается иконока Mail.ru"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_mm"))
        with allure.step("Отображается иконока Facebook"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_fb"))
        with allure.step("Отображается иконока Google"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_google"))
        with allure.step("Отображается иконока Twitter"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_tw"))
        with allure.step("Отображается иконока Yandex.ru"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_ya"))

    @allure.step("Проверить наличие текста и элементов в popup-separator, popup-form__body")
    def test_Body_text_and_elements_displayed(self):
        with allure.step("В элементе popup-separator__title отображается текст (или)"):
            self.assertEqual(u"или", self.driver.find_element_by_css_selector("div.popup-separator__title").text)
        with allure.step("В элементе label.popup-label отображается текст (E-mail)"):
            self.assertEqual("E-mail", self.driver.find_element_by_css_selector("label.popup-label").text)
        with allure.step("Отображается поле ввода E-mail"):
            self.assertTrue(self.is_element_present(By.XPATH, "//label/input[1]"))
        with allure.step("В элементе popup-label_password отображается текст (Пароль)"):
            self.assertEqual(u"Пароль",
                             self.driver.find_element_by_css_selector("label.popup-label_password").text)
        with allure.step("Отображается поле ввода Password"):
            self.assertTrue(self.is_element_present(By.XPATH, "//label[2]/input"))
        with allure.step("Отображается кнопка показать пароль"):
            self.assertTrue(self.is_element_present(By.CLASS_NAME, "password-eye"))
        with allure.step("Отображается чек-бокс (Запомнить меня)"):
            self.assertTrue(self.is_element_present(By.ID, "remember"))
        with allure.step("Отображается текст (Запомнить меня)"):
            self.assertEqual(u"Запомнить меня",
                             self.driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/label/span").text)
        with allure.step("Отображается кнопка (Забыли пароль)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Забыли пароль?"))

    @allure.step("В поп-апе отображается кнопка Войти")
    def test_Footer_element_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.popup-button"))
