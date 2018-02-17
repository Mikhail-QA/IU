"""
Проверка наличия элементов в попапе Авторизации
URL: https://interneturok.ru/users/sign_in?tab=authTab"	На странице отображаются: http://joxi.ru/gmvOq1NUxeZez2
"""

from selenium.webdriver.common.by import By
from Interneturok.web_services.app.SetUp import StartInterneturokClassMethod
from POM.main_page import MainPage


class CheckPopupAuth(StartInterneturokClassMethod):
    def test_001_open_popup(self):
        driver = self.driver
        steps_main = MainPage(driver)
        steps_main.go_to_sgnIn()

    def test_header_text_and_elements_displayed(self):
        self.assertEqual(u"Войдите в профиль",
                         self.driver.find_element_by_css_selector("h5.popup-header__title").text)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.popup-header__close"))
        self.assertEqual(u"Вход", self.driver.find_element_by_link_text(u"Вход").text)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.switcher__button"))
        self.assertEqual(u"Регистрация", self.driver.find_element_by_link_text(u"Регистрация").text)
        self.assertEqual(u"Быстрый вход",
                         self.driver.find_element_by_css_selector("span.popup-subtitle").text)

    def test_social_button_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_vk"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_od"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_mm"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_fb"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_google"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_tw"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-social.icon-social_ya"))

    def test_Body_text_and_elements_displayed(self):
        self.assertEqual(u"или", self.driver.find_element_by_css_selector("div.popup-separator__title").text)
        self.assertEqual("E-mail", self.driver.find_element_by_css_selector("label.popup-label").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//label/input[1]"))
        self.assertEqual(u"Пароль",
                         self.driver.find_element_by_css_selector("label.popup-label_password").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//label[2]/input"))
        self.assertTrue(self.is_element_present(By.CLASS_NAME, "password-eye"))
        self.assertTrue(self.is_element_present(By.ID, "remember"))
        self.assertEqual(u"Запомнить меня",
                         self.driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/label/span").text)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Забыли пароль?"))

    def test_Footer_element_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.popup-button"))
