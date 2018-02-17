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

from selenium.webdriver.common.by import By
from Interneturok.web_services.app.SetUp import StartInterneturokClassMethod
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.user import PaymNotYandexRu


class ChecksAllElementsInPopupFlash(StartInterneturokClassMethod):
    def test_001_open_popup_flash(self):
        self.driver.find_element_by_id("widget-container").click()

    def test_002_look_button_close(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "close"))

    def test_003_text1(self):
        self.assertEqual(u"Флешка InternetUrok.ru",
                         self.driver.find_element_by_css_selector("strong.sub-title._center-text").text)

    def test_004_text2(self):
        self.assertEqual(
            u"""Вы сможете загрузить уроки на свою флешку\nи заниматься без Интернета\nПодробнее об флешке""",
            self.driver.find_element_by_css_selector("span.products-benefits__text").text)

    def test_005_text3(self):
        self.assertEqual(
            u"""Для загрузки уроков нужно войти в свою\nучетную запись и оплатить абонемент.\nПодробнее об абонементе""",
            self.driver.find_element_by_xpath("//div[@id='widget-wrapper']/div/div/div/ul/li[2]/span[2]").text)

    def test_006_look_button_pay(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Оплатить абонемент"))

    def test_007_text5(self):
        self.assertEqual(u"У вас уже есть абонемент? Войти", self.driver.find_element_by_css_selector(
            "#widget-wrapper > div > div > div > div.more-holder.text-center").text)

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

    def test_009_open_popup_flash(self):
        self.driver.find_element_by_id("widget-container").click()

    def test_10_look_button_close(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "close"))

    def test_11_text1(self):
        self.assertEqual(u"Флешка InternetUrok.ru",
                         self.driver.find_element_by_css_selector("strong.sub-title._center-text").text)

    def test_12_text2(self):
        self.assertEqual(
            u"""Вы сможете загрузить уроки на свою флешку\nи заниматься без Интернета\nПодробнее об флешке""",
            self.driver.find_element_by_css_selector("span.products-benefits__text").text)

    def test_13_text3(self):
        self.assertEqual(
            u"""Для загрузки уроков нужно оплатить\nабонемент. Подробнее об абонементе""",
            self.driver.find_element_by_xpath("//div[@id='widget-wrapper']/div/div/div/ul/li[2]/span[2]").text)

    def test_14_look_button_pay(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Оплатить абонемент"))

    def test_15_authorization_user(self):
        driver = self.driver
        steps_main = MainPage(driver)
        user_step = PaymNotYandexRu(driver)
        steps_signIn = PopupSignIn(driver)
        driver.get("https://web-dev01.interneturok.ru/signout")
        steps_main.go_to_sgnIn()
        user_step.enter_email()
        user_step.enter_password()
        steps_signIn.click_button_login()
        driver.refresh()

    def test_16_open_popup_flash(self):
        self.driver.find_element_by_id("widget-container").click()

    def test_17_look_button_close(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "close"))

    def test_18_text1(self):
        self.assertEqual(u"Доступные для загрузки наборы уроков:",
                         self.driver.find_element_by_css_selector(
                             "#widget-availables-list > strong").text)

    def test_19_text2(self):
        self.assertEqual(
            u"Ваш список загрузки\nНа флешке нет уроков. Добавляйте уроки со страниц\nInternetUrok.ru и занимайтесь без интернета\nПодробнее о флешке",
            self.driver.find_element_by_css_selector("#widget-wrapper > div > div:nth-child(2)").text)

    def test_20_look_button_more_about_the_flash(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Подробнее о флешке"))
