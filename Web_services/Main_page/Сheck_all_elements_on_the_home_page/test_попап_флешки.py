"""
1. Проверить наличия элементов в попапе Flash
Пользователь не авторизован
URL: https://interneturok.ru/"	На странице отображаются: http://joxi.ru/EA41kdxTDXaoJr
2. Проверить наличия элементов в попапе Flash
Пользователь авторизован, без абонемента
URL: https://interneturok.ru/"	На странице отображаются: http://joxi.ru/LmG4EgoHRBnJx2
3. Проверить наличия элементов в попапе Flash
Пользователь авторизован, с абонементом
URL:
"""

import pytest
import time
import allure
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.user import PaymNotYandexRu


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов в виджете Флешка")
# @pytest.mark.skip(reason="Убрали Флешку из проекта")
class ChecksAllElementsInPopupFlash(StartInterneturokClassMethod):
    @allure.step("Нажать на кнопку Флешка")
    def test_001_open_popup_flash(self):
        self.driver.find_element_by_css_selector("i.icon-flash").click()

    @allure.step("В поп-апе Флешка отображается кнопка Крестик(закрыть) ")
    def test_002_look_button_close(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.button-close"))

    @allure.step("Отображается заголовок с текстом (Флешка InternetUrok.ru)")
    def test_003_text1(self):
        self.assertEqual(u"Флешка InternetUrok.ru",
                         self.driver.find_element_by_css_selector("h3.title").text)

    @allure.step(
        "Отображается текст (Вы сможете загрузить уроки на свою флешку и заниматься без Интернета Подробнее о флешке)")
    def test_004_text2(self):
        self.assertEqual(
            u"""Вы можете загрузить уроки на свою флешку\nи заниматься без Интернета.\nПодробнее о флешке""",
            self.driver.find_element_by_css_selector(".__flash-info__b79b8 > div:nth-child(3) > div.text").text)

    @allure.step(
        "Отображается текст (Для загрузки уроков нужно войти в свою учетную запись и оплатить абонемент. Подробнее об абонементе")
    def test_005_text3(self):
        self.assertEqual(
            u"""Для загрузки уроков нужно войти в свою учётную запись и оплатить абонемент. Подробнее об абонементе""",
            self.driver.find_element_by_css_selector(".__flash-info__b79b8 > div:nth-child(4) > div.text").text)

    @allure.step("Отображается кнопка (Оплатить абонемент)")
    def test_006_look_button_pay(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.button-pay"))

    @allure.step("Отображается текст (У вас уже есть абонемент? Войти)")
    def test_007_text5(self):
        self.assertEqual(u"У Вас уже есть абонемент? Войти", self.driver.find_element_by_css_selector(
            "p.subscribe-already").text)
        self.driver.refresh()

    @allure.step("Авторизоваться пользователем без абонемента")
    def test_008_authorization_user(self):
        driver = self.driver
        steps_main = MainPage(driver)
        user_step = AutopaymentMailRu(driver)
        steps_signIn = PopupSignIn(driver)

        steps_main.go_to_sgnIn()
        user_step.enter_email()
        user_step.enter_password()
        steps_signIn.click_button_login()
        driver.refresh()
        time.sleep(3)

    @allure.step("Нажать на кнопку Флешка")
    def test_009_open_popup_flash(self):
        self.driver.find_element_by_css_selector("i.icon-flash").click()

    @allure.step("В поп-апе Флешка отображается кнопка Крестик(закрыть) ")
    def test_10_look_button_close(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.button-close"))

    @allure.step("Отображается заголовок с текстом (Флешка InternetUrok.ru)")
    def test_11_text1(self):
        self.assertEqual(u"Флешка InternetUrok.ru",
                         self.driver.find_element_by_css_selector("h3.title").text)

    @allure.step(
        "Отображается текст (Вы можете загрузить уроки на свою флешку и заниматься без Интернета. Подробнее об флешке)")
    def test_12_text2(self):
        self.assertEqual(
            u"""Вы можете загрузить уроки на свою флешку\nи заниматься без Интернета.\nПодробнее о флешке""",
            self.driver.find_element_by_css_selector(".__flash-info__b79b8 > div:nth-child(3) > div.text").text)

    @allure.step(
        "Отображается текст (Для загрузки уроков нужно оплатить абонемент. Подробнее об абонементе)")
    def test_13_text3(self):
        self.assertEqual(
            u"""Для загрузки уроков нужно оплатить абонемент. Подробнее об абонементе""",
            self.driver.find_element_by_css_selector(".__flash-info__b79b8 > div:nth-child(4) > div.text").text)

    @allure.step("Отображается кнопка (Оплатить абонемент)")
    def test_14_look_button_pay(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.button-pay"))
        self.driver.refresh()

    @allure.step("Авторизоваться пользователем с абонементом")
    def test_15_authorization_user(self):
        driver = self.driver
        steps_main = MainPage(driver)
        user_step = PaymNotYandexRu(driver)
        steps_signIn = PopupSignIn(driver)

        # driver.get("https://staging.interneturok.ru/")
        self.driver.delete_all_cookies()
        driver.refresh()
        steps_main.go_to_sgnIn()
        user_step.enter_email()
        user_step.enter_password()
        steps_signIn.click_button_login()
        time.sleep(10)
        driver.refresh()

    @allure.step("Нажать на кнопку Флешка")
    def test_16_open_popup_flash(self):
        self.driver.find_element_by_css_selector("i.icon-flash").click()

    @allure.step("В поп-апе Флешка отображается кнопка Крестик(закрыть) ")
    def test_17_look_button_close(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.button-close"))

    @allure.step("Отображается текст (Доступные для загрузки наборы уроков:)")
    def test_18_text1(self):
        self.assertEqual(u"Доступные для загрузки наборы уроков:",
                         self.driver.find_element_by_css_selector(
                             "h3.__flash-available-lessons__2288e-title").text)

    @allure.step("Отображается список бандлов к загрузке")
    def test_19_look_board_bandl(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.lessons-border"))

    @allure.step(
        "Отображается текст (Ваш список загрузки На флешке нет уроков. Добавляйте уроки со страниц InternetUrok.ru и занимайтесь без интернета Подробнее о флешке)")
    def test_20_text2(self):
        self.assertEqual(
            u"Ваш список загрузки\nНа флешке нет уроков. Добавляйте уроки со страниц InternetUrok.ru и занимайтесь без Интернета\nПодробнее о флешке",
            self.driver.find_element_by_css_selector("div.__flash-download-lessons__576bd").text)

    @allure.step("Отображается текст (Подробнее о флешке)")
    def test_21_look_button_more_about_the_flash(self):
        self.assertEqual("Подробнее о флешке",
                         self.driver.find_element_by_css_selector("a.button-about-flash").text)
