"""
Проверка наличия элементов в попапе Регистрации
URL: https://interneturok.ru/users/sign_in?tab=regTab"	На странице отображаются: http://joxi.ru/52aykXDUGlv0O2
"""

import time
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn


class CheckPopupReg(StartInterneturokClassMethod):
    def test_001_open_popup(self):
        driver = self.driver
        steps_user = PopupSignIn(driver)
        steps_main = MainPage(driver)
        steps_main.go_to_sgnIn()
        steps_user.go_to_popup_registration()
        time.sleep(0.5)

    def test_header_elements_and_text_displayed(self):
        self.assertEqual(u"Зарегистрируйтесь",
                         self.driver.find_element_by_css_selector("h5.popup-header__title").text)
        self.assertTrue(self.is_element_present(By.CLASS_NAME, "popup-header__close"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Регистрация"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.switcher.popup-switcher"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Вход"))
        self.assertEqual(u"Быстрая регистрация", self.driver.find_element_by_css_selector("span.popup-subtitle").text)

    def test_social_button_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_vk"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_od"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_mm"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_fb"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_google"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_tw"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social_ya"))

    def test_Body_elements_and_text_displayed(self):
        self.assertEqual(u"или", self.driver.find_element_by_css_selector("div.popup-separator__title").text)
        self.assertEqual("E-mail", self.driver.find_element_by_css_selector("label.popup-label").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//label[1]/input"))
        self.assertEqual(u"Пароль",
                         self.driver.find_element_by_css_selector("label.popup-label_password").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//label[2]/input"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.password-eye"))

    def test_Footer_elements_and_text_displayed(self):
        self.assertEqual(u"Вы являетесь:",
                         self.driver.find_element_by_css_selector("span.select__title").text)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.options-selector "))
        self.assertTrue(
            self.is_element_present(By.CSS_SELECTOR, "button.popup-button"))
        self.assertEqual(u"Нажимая кнопку «Зарегистрироваться», я принимаю",
                         self.driver.find_element_by_css_selector("div.popup-rules > span").text)
        self.assertEqual(u"Пользовательское соглашение",
                         self.driver.find_element_by_link_text(u"Пользовательское соглашение").text)
