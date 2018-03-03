"""
Проверить наличия элементов на главной странице в Footer
URL: https://interneturok.ru/"	На странице отображаются: http://joxi.ru/8AnW6anuqN8BPr
"""

from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod


class Checks_all_elements_the_page_in_footer(StartInterneturokClassMethod):
    def test_block_education_center_displayed(self):
        self.assertEqual(u"Центр образования",
                         self.driver.find_element_by_xpath("//nav/div/div[1]/h4[1]").text)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Домашняя школа"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Репетитор ЕГЭ"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Univertv.ru"))

    def test_block_reviews_displayed(self):
        self.assertEqual(u"Отзывы", self.driver.find_element_by_xpath("//nav/div/div[2]/h4[1]").text)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Отзывы пользователей"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"СМИ о нас"))

    def test_block_cooperation_displayed(self):
        self.assertEqual(u"Сотрудничество", self.driver.find_element_by_xpath("//nav/div/div[3]/h4[1]").text)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Участие в проекте"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Методический кабинет"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Партнеры"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Благодарности"))

    def test_block_about_the_project_displayed(self):
        self.assertEqual(u"О проекте", self.driver.find_element_by_xpath("//nav/div/div[4]/h4[1]").text)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"О проекте"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Наши учителя"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Мы и государство"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Часто задаваемые вопросы"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Абонемент / поддержка сайта"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Контактная информация"))

    def test_text_apps_for_your_tablet_displayed_the_screen(self):
        self.assertEqual(u"Приложения для планшета:",
                         self.driver.find_element_by_css_selector("div.footer__copyrights-app").text)

    def test_icon_android_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-android"))

    def test_icon_apple_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-ios"))

    def test_text_we_in_social_networks(self):
        self.assertEqual(u"Мы в соцсетях:",
                         self.driver.find_element_by_css_selector("div.footer__copyrights-social").text)

    def test_icon_vk_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-vk"))

    def test_icon_facebook_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-fb"))

    def test_icon_od_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-ok"))

    def test_icon_youtube_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-yt"))

    def test_text_interda_displayed_the_screen(self):
        self.assertEqual(u"© 2010-2018 000 «Интерда»",
                         self.driver.find_element_by_css_selector("p.footer__copyrights-text").text)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Условия пользования сайтом"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Политика конфиденциальности"))
        # self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.icon-sitemap"))

