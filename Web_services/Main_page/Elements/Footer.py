"""
Проверить наличия элементов на главной странице в Footer
URL: https://interneturok.ru/"	На странице отображаются: http://joxi.ru/8AnW6anuqN8BPr
"""

import allure
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов и текста на главной страницы в Footer")
class ChecksAllElementsThePageInFooter(StartInterneturokClassMethod):
    def test_block_education_center_displayed(self):
        with allure.step("Отображается название блока (Центр образования)"):
            self.assertEqual(u"Центр образования",
                             self.driver.find_element_by_xpath("//nav/div/div[1]/h4[1]").text)
        with allure.step("В блоке Центр образования отображается ссылка (Домашняя школа)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Домашняя школа"))
        with allure.step("В блоке Центр образования отображается ссылка (Репетитор ЕГЭ)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Репетитор ЕГЭ"))
        with allure.step("В блоке Центр образования отображается ссылка (Univertv.ru)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, "Univertv.ru"))

    def test_block_reviews_displayed(self):
        with allure.step("Отображается название блока (Отзывы)"):
            self.assertEqual(u"Отзывы", self.driver.find_element_by_xpath("//nav/div/div[2]/h4[1]").text)
        with allure.step("В блоке Отзывы отображается ссылка (Отзывы пользователей)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Отзывы пользователей"))
        with allure.step("В блоке Отзывы отображается ссылка (Упоминания в СМИ)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Упоминания в СМИ"))

    def test_block_cooperation_displayed(self):
        with allure.step("Отображается название блока (Сотрудничество)"):
            self.assertEqual(u"Сотрудничество", self.driver.find_element_by_xpath("//nav/div/div[3]/h4[1]").text)
        with allure.step("В блоке Сотрудничество отображается ссылка Участие в проекте"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Участие в проекте"))
        with allure.step("В блоке Сотрудничество отображается ссылка Методический кабинет"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Методический кабинет"))

    def test_block_about_the_project_displayed(self):
        with allure.step("Отображается название блока (О проекте)"):
            self.assertEqual(u"О проекте", self.driver.find_element_by_xpath("//nav/div/div[4]/h4[1]").text)
        with allure.step("В блоке О проекте отображается ссылка (О проекте)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"О проекте"))
        with allure.step("В блоке О проекте отображается ссылка (Наши учителя)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Наши учителя"))
        with allure.step("В блоке О проекте отображается ссылка (Мы и государство)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Мы и государство"))
        with allure.step("В блоке О проекте отображается ссылка (Часто задаваемые вопросы)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Часто задаваемые вопросы"))
        with allure.step("В блоке О проекте отображается ссылка (Абонемент)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Абонемент"))
        with allure.step("В блоке О проекте отображается ссылка (Контактная информация)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Контактная информация"))

    def test_text_apps_for_your_tablet_displayed_the_screen(self):
        with allure.step("В подвале сайта отображается текст (Приложения для планшета:)"):
            self.assertEqual(u"Приложения для планшета:",
                             self.driver.find_element_by_css_selector("div.cp-text-app").text)

    def test_icon_android_displayed(self):
        with allure.step("В подвале сайта в Приложения для планшета отображается иконка (Android)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.cp-icon-android"))

    def test_icon_apple_displayed(self):
        with allure.step("В подвале сайта в Приложения для планшета отображается иконка (iOS)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.cp-icon-ios"))

    def test_text_we_in_social_networks(self):
        with allure.step("В подвале сайта отображается текст (Мы в соцсетях:)"):
            self.assertEqual(u"Мы в соцсетях:",
                             self.driver.find_element_by_css_selector("div.cp-text").text)

    def test_icon_vk_displayed(self):
        with allure.step("В подвале сайта в Мы в соцсетях отображается иконка (ВК)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.cp-icon-vk"))

    def test_icon_facebook_displayed(self):
        with allure.step("В подвале сайта в Мы в соцсетях отображается иконка (Facebook)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.cp-icon-fb"))

    def test_icon_od_displayed(self):
        with allure.step("В подвале сайта в Мы в соцсетях отображается иконка (Одноклассники)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.cp-icon-ok"))

    def test_icon_youtube_displayed(self):
        with allure.step("В подвале сайта в Мы в соцсетях отображается иконка (YouTube)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.cp-icon-yt"))

    def test_text_interda_displayed_the_screen(self):
        with allure.step(
                "В подвале сайта отображается текст (© 2010-2021 000 «Интерда»\nУсловия пользования сайтом\nПолитика конфиденциальности)"):
            self.assertEqual(u'© 2010-2021 000 «Интерда»\nУсловия пользования сайтом\nПолитика конфиденциальности',
                             self.driver.find_element_by_css_selector("div.cp-copyrights").text)

    def test_icon_sk_displayed(self):
        with allure.step('В подвале сайта отображается иконка SK участник'):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.cp-icon-sk"))
