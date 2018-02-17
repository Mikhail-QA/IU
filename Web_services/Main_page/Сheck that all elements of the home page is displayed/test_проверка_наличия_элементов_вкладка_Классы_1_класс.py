"""
Проверить наличия элементов во вкладке ""Классы --> 1 класс""
URL: https://interneturok.ru/grades/1?_=1503573733002"	На странице отображаются: http://joxi.ru/EA41kdxTDXKbjr
"""

import time
from selenium.webdriver.common.by import By
from Interneturok.web_services.app.SetUp import StartInterneturokClassMethod


class CheckAllElementsTheGrades(StartInterneturokClassMethod):
    def test_001_click_button_grades(self):
        self.driver.find_element_by_xpath("//main/nav/div/a[2]").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[1]/ul/li[1]").click()
        time.sleep(0.5)

    def test_text_home_title_displayed(self):
        self.assertEqual(u"Уроки школьной программы", self.driver.find_element_by_css_selector("h1.home-title").text)

    def test_text_home_desc_displayed(self):
        self.assertEqual(u"Видео, конспекты, тесты, тренажеры",
                         self.driver.find_element_by_css_selector("p.home-title_small").text)

    def test_button_subjects(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Предметы"))

    def test_button_grades(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Классы"))

    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.home-search"))

    def test_button_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.home-search__button"))

    def test_button_back_main_page(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.subjects__grades-nav-back"))

    def test_button_matematika(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Математика"))

    def test_button_OKM(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Окружающий мир"))

    def test_button_russian_language(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Русский язык"))

    def test_button_reading(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Чтение"))
