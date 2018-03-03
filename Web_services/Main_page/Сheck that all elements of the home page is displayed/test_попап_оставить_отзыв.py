"""
Проверка наличия элементов в попапе Оставить отзыв
URL:https://interneturok.ru/feedbacks/new"	На странице отображаются: http://joxi.ru/ZrJ4XBoH1Q6Z32
"""
import time
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu


class CheckPopupReview(StartInterneturokClassMethod):
    def test_001_open_popup(self):
        self.driver.find_element_by_css_selector("a.review__button").click()

    def test_002_check_text_in_block(self):
        self.assertEqual(u"Спасибо, что решили написать!",
                         self.driver.find_element_by_class_name("popup-header").text)

    def test_003_look_button_close(self):
        self.assertTrue(self.is_element_present(By.CLASS_NAME, "popup-header__close"))

    def test_004_check_text_in_block_header(self):
        self.assertEqual(u"Нам важны все Ваши отзывы: и одобрение, и критика.",
                         self.driver.find_element_by_xpath("//div/div[2]/div/div/p[1]").text)
        self.assertEqual(
            u"""Если Вы хотите указать на наши недостатки,\nпожалуйста, опишите их как можно подробнее.\nМы хотим знать, что именно Вам не понравилось,\nи исправить это.""",
            self.driver.find_element_by_xpath("//div/div[2]/div/div/p[2]").text)

    def test_005_field_feedback_sender(self):
        self.assertEqual(u"Ваше имя", self.driver.find_element_by_css_selector("label.popup-label").text)

        self.assertTrue(self.is_element_present(By.XPATH, "//label[1]/input"))

    def test_006_field_feedback_email(self):
        self.assertEqual("E-mail",
                         self.driver.find_element_by_xpath("//label[2]").text)

        self.assertTrue(self.is_element_present(By.XPATH, "//label[2]/input"))

    def test_007_field_feedback_content(self):
        self.assertEqual(u"Текст отзыва",
                         self.driver.find_element_by_xpath("//label[3]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//label[3]/textarea"))

    def test_008_field_feedbakc_form(self):
        self.assertEqual(u"Откуда вы о нас узнали?",
                         self.driver.find_element_by_xpath("//label[4]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//label[4]/input"))

    def test_009_button_commit_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.popup-button"))

    def test_10_authorization_user(self):
        driver = self.driver
        steps_main = MainPage(driver)
        user_step = AutopaymentMailRu(driver)
        steps_signIn = PopupSignIn(driver)

        self.driver.find_element_by_class_name("popup-header__close").click()
        time.sleep(1)
        steps_main.go_to_sgnIn()
        user_step.enter_email()
        user_step.enter_password()
        steps_signIn.click_button_login()

    def test_11_open_popup(self):
        self.driver.find_element_by_css_selector("div.review_open").click()

    def test_12_check_text_in_block(self):
        self.assertEqual(u"Спасибо, что решили написать!",
                         self.driver.find_element_by_class_name("popup-header").text)

    def test_13_look_button_close(self):
        self.assertTrue(self.is_element_present(By.CLASS_NAME, "popup-header__close"))

    def test_14_check_text_in_block_header(self):
        self.assertEqual(u"Нам важны все Ваши отзывы: и одобрение, и критика.",
                         self.driver.find_element_by_xpath("//div/div[2]/div/div/p[1]").text)
        self.assertEqual(
            u"""Если Вы хотите указать на наши недостатки,\nпожалуйста, опишите их как можно подробнее.\nМы хотим знать, что именно Вам не понравилось,\nи исправить это.""",
            self.driver.find_element_by_xpath("//div/div[2]/div/div/p[2]").text)

    def test_15_field_feedback_sender(self):
        self.assertEqual(u"Ваше имя", self.driver.find_element_by_css_selector("label.popup-label").text)

        self.assertEqual(u"Мишка", self.driver.find_element_by_xpath("//label[1]/input").get_attribute("value"))

    def test_16_field_feedback_email(self):
        self.assertEqual("E-mail",
                         self.driver.find_element_by_xpath("//label[2]").text)
        self.assertEqual("autopayment@mail.ru",
                         self.driver.find_element_by_xpath("//label[2]/input").get_attribute("value"))

    def test_17_field_feedback_content(self):
        self.assertEqual(u"Текст отзыва",
                         self.driver.find_element_by_xpath("//label[3]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//label[3]/textarea"))

    def test_18_field_feedback_form(self):
        self.assertEqual(u"Откуда вы о нас узнали?",
                         self.driver.find_element_by_xpath("//label[4]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//label[4]/input"))

    def test_19_button_commit_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.popup-button"))
