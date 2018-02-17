"""
Проверить наличия элементов во вкладке Идеии и смыслы
URL: https://interneturok.ru/"	На странице отображаются: http://joxi.ru/E2pLd3xcBvY912
"""

import time
from selenium.webdriver.common.by import By
from Interneturok.web_services.app.SetUp import StartInterneturokClassMethod


class CheckIdea(StartInterneturokClassMethod):
    def test_1_a_open_blick_idea(self):
        self.driver.find_element_by_link_text("Идеи и смыслы").click()
        time.sleep(0.5)

    def test_notification_displayed_ideas_and_meanings(self):
        self.assertEqual(u"Идеи и смыслы", self.driver.find_element_by_css_selector("span.subjects__grades-nav-current").text)

    def test_button_back_main_page(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.subjects__grades-nav-back-text"))

    def test_board_grades1(self):
        self.assertEqual(u"Математика за 20 уроков\nОбщие идеи", self.driver.find_element_by_xpath("//div/main//div/ul/li[1]").text)

    def test_board_grades2(self):
        self.assertEqual(u"Основы рационального поведения\nИнструменты размышления", self.driver.find_element_by_xpath(
            "//a[contains(@href, '/idei-i-smysly/osnovy-ratsionalnogo-povedeniya')]").text)

    def test_board_grades3(self):
        self.assertEqual(u"Дискуссии и обсуждения\nЛитература, ...", self.driver.find_element_by_xpath(
            "//a[contains(@href, '/idei-i-smysly/diskussii-i-obsuzhdeniya')]").text)

    def test_board_grades4(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Полезные интервью"))

    def test_board_grades5(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Основные понятия истории"))

    def test_button_subjects(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Предметы"))

    def test_button_grades(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Классы"))
