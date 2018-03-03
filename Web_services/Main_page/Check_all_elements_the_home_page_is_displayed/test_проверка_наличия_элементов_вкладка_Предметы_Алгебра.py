"""
Проверить наличия элементов, во вкладке ""Предметы --> Алгебра""
URL:https://interneturok.ru/subjects"	На странице отображаются: http://joxi.ru/p2715ZyT0LEvZr
"""

import time
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod


class CheckAllElementsTheGrades(StartInterneturokClassMethod):
    def test_001_click_button_Algebra(self):
        self.driver.find_element_by_xpath("//div/div/div[1]/ul/li[1]/a").click()
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

    def test_button_in_left_displayed(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "<"))

    def test_text_displayed(self):
        self.assertEqual(u"Алгебра", self.driver.find_element_by_css_selector("span.subjects__grades-nav-current").text)

    def test_button_in_right_displayed(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, ">"))

    def test_button_7_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[1]/a"))

    def test_button_8_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[2]/a"))

    def test_button_9_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[3]/a"))

    def test_button_10_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[4]/a"))

    def test_button_11_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[5]/a"))

    def test_button_ege(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[6]/a"))

