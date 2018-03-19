"""
Проверить наличия элементов на главной странице в Footer
URL: https://interneturok.ru/"	На странице отображаются: http://joxi.ru/8AnW6anuqN8BPr
"""

import allure
from selenium.webdriver.common.by import By
from Web_services.URL import SubjectPage
from Web_services.app.SetUp import StartInterneturokClassMethod


@allure.feature("Страница Предмет-Класс (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов и текста в Footer")
class ChecksAllElementsInSubjectPageThePageInFooter(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 8 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = SubjectPage(StartInterneturokClassMethod)
        go_page.go_algebra_8_grade()

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
        with allure.step("В блоке Отзывы отображается ссылка (СМИ о нас)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"СМИ о нас"))

    def test_block_cooperation_displayed(self):
        with allure.step("Отображается название блока (Сотрудничество)"):
            self.assertEqual(u"Сотрудничество", self.driver.find_element_by_xpath("//nav/div/div[3]/h4[1]").text)
        with allure.step("В блоке Сотрудничество отображается ссылка Участие в проекте"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Участие в проекте"))
        with allure.step("В блоке Сотрудничество отображается ссылка Методический кабинет"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Методический кабинет"))
        with allure.step("В блоке Сотрудничество отображается ссылка Партнеры"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Партнеры"))
        with allure.step("В блоке Сотрудничество отображается ссылка Благодарности"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Благодарности"))

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
        with allure.step("В блоке О проекте отображается ссылка (Абонемент / поддержка сайта)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Абонемент / поддержка сайта"))
        with allure.step("В блоке О проекте отображается ссылка (Контактная информация)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Контактная информация"))

    def test_text_apps_for_your_tablet_displayed_the_screen(self):
        with allure.step("В подвале сайта отображается текст (Приложения для планшета:)"):
            self.assertEqual(u"Приложения для планшета:",
                             self.driver.find_element_by_css_selector("div.footer__copyrights-app").text)

    def test_icon_android_displayed(self):
        with allure.step("В подвале сайта в Приложения для планшета отображается иконка (Android)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-android"))

    def test_icon_apple_displayed(self):
        with allure.step("В подвале сайта в Приложения для планшета отображается иконка (iOS)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-ios"))

    def test_text_we_in_social_networks(self):
        with allure.step("В подвале сайта отображается текст (Мы в соцсетях:)"):
            self.assertEqual(u"Мы в соцсетях:",
                             self.driver.find_element_by_css_selector("div.footer__copyrights-social").text)

    def test_icon_vk_displayed(self):
        with allure.step("В подвале сайта в Мы в соцсетях отображается иконка (ВК)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-vk"))

    def test_icon_facebook_displayed(self):
        with allure.step("В подвале сайта в Мы в соцсетях отображается иконка (Facebook)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-fb"))

    def test_icon_od_displayed(self):
        with allure.step("В подвале сайта в Мы в соцсетях отображается иконка (Одноклассники)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-ok"))

    def test_icon_youtube_displayed(self):
        with allure.step("В подвале сайта в Мы в соцсетях отображается иконка (YouTube)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-yt"))

    def test_text_interda_displayed_the_screen(self):
        with allure.step("В подвале сайта отображается текст (© 2010-2018 000 «Интерда»)"):
            self.assertEqual(u"© 2010-2018 000 «Интерда»",
                             self.driver.find_element_by_css_selector("p.footer__copyrights-text").text)
        with allure.step("В подвале сайта отображается текст (Условия пользования сайтом)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Условия пользования сайтом"))
        with allure.step("В подвале сайта отображается текст (Политика конфиденциальности)"):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Политика конфиденциальности"))
            # self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-sitemap"))
