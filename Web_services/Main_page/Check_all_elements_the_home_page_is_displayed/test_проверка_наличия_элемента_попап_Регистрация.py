"""
Проверка наличия элементов в попапе Регистрации
URL: https://interneturok.ru/users/sign_in?tab=regTab"	На странице отображаются: http://joxi.ru/52aykXDUGlv0O2
"""

import allure
import time
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов в поп-апе Регистрации")
class CheckPopupReg(StartInterneturokClassMethod):
    @allure.step("Открыть поп-ап Регистрации")
    def test_001_open_popup(self):
        driver = self.driver
        steps_user = PopupSignIn(driver)
        steps_main = MainPage(driver)
        steps_main.go_to_sgnIn()
        steps_user.go_to_popup_registration()
        time.sleep(0.5)

    @allure.step("Проверить наличие текста и элементов в popup-header, popup-switcher__wrap, popup-subtitle")
    def test_header_elements_and_text_displayed(self):
        with allure.step("В header поп-ап присутствует текст (Зарегистрируйтесь)"):
            self.assertEqual(u"Зарегистрируйтесь",
                             self.driver.find_element_by_css_selector("h5.popup-header__title").text)
        with allure.step("В header поп-ап присутствует кнопка крестик (закрыть)"):
            self.assertTrue(self.is_element_present(By.CLASS_NAME, "popup-header__close"))
        with allure.step("В элементе popup-switcher отображается текст (Регистрация)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Регистрация"))
        with allure.step(
                "В поп-апе Регистрации отображается передвижной ползунок перключателя с Авторизации/Регистрации"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.switcher.popup-switcher"))
        with allure.step("В элементе popup-switcher отображается текст (Вход)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Вход"))
        with allure.step("В элементе popup-subtitle отображается текст (Быстрая регистрация)"):
            self.assertEqual(u"Быстрая регистрация",
                             self.driver.find_element_by_css_selector("span.popup-subtitle").text)

    @allure.step("Проверить наличия иконок соцсетей")
    def test_social_button_displayed(self):
        with allure.step("Отображается иконока ВК"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_vk"))
        with allure.step("Отображается иконока Одноклассники"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_od"))
        with allure.step("Отображается иконока Mail.ru"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_mm"))
        with allure.step("Отображается иконока Facebook"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_fb"))
        with allure.step("Отображается иконока Google"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_google"))
        with allure.step("Отображается иконока Twitter"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_tw"))
        with allure.step("Отображается иконока Yandex.ru"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_ya"))

    @allure.step("Проверить наличие текста и элементов в popup-separator, popup-form__body")
    def test_Body_elements_and_text_displayed(self):
        with allure.step("В элементе popup-separator__title отображается текст (или)"):
            self.assertEqual(u"или", self.driver.find_element_by_css_selector("div.popup-separator__title").text)
        with allure.step("В элементе label.popup-label отображается текст (E-mail)"):
            self.assertEqual("E-mail", self.driver.find_element_by_css_selector("label.popup-label").text)
        with allure.step("Отображается поле ввода E-mail"):
            self.assertTrue(self.is_element_present(By.XPATH, "//label[1]/input"))
        with allure.step("В элементе popup-label_password отображается текст (Пароль)"):
            self.assertEqual(u"Пароль",
                             self.driver.find_element_by_css_selector("label.popup-label_password").text)
        with allure.step("Отображается поле ввода Password"):
            self.assertTrue(self.is_element_present(By.XPATH, "//label[2]/input"))
        with allure.step("Отображается кнопка показать пароль"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.password-eye"))

    @allure.step("Проверить наличие текста и элементов в popup-select select__wrap, popup-footer")
    def test_Footer_elements_and_text_displayed(self):
        with allure.step("Отображается текст (Вы являетесь:)"):
            self.assertEqual(u"Вы являетесь:",
                             self.driver.find_element_by_css_selector("span.select__title").text)
        with allure.step("Отображается выпадающий списк выбора роли регистрации"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.options-selector "))
        with allure.step("Отображается кнопка Зарегистрироваться"):
            self.assertTrue(
                self.is_element_present(By.CSS_SELECTOR, "button.popup-button"))
        with allure.step(
                "Отображается информационный текст под кнопкой Зарегистрироваться (Нажимая кнопку «Зарегистрироваться», я принимаю)"):
            self.assertEqual(u"Нажимая кнопку «Зарегистрироваться», я принимаю",
                             self.driver.find_element_by_css_selector("div.popup-rules > span").text)
        with allure.step("Отображается ссылка (Пользовательское соглашение)"):
            self.assertEqual(u"Пользовательское соглашение",
                             self.driver.find_element_by_link_text(u"Пользовательское соглашение").text)
