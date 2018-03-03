"""
Проверить наличия элементов на главной странице, во вкладке ""Классы""
URL:https://interneturok.ru/grades"	На странице отображаются: http://joxi.ru/52aykXDUGlZDx2
"""

import time
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod


class CheckAllElementsTheGrades(StartInterneturokClassMethod):
    def test_z_000_click_button_grades_z_(self):
        self.driver.find_element_by_xpath("//main/nav/div/a[2]").click()
        time.sleep(0.5)

    def test_z_001_text_home_title_displayed(self):
        self.assertEqual(u"Уроки школьной программы", self.driver.find_element_by_css_selector("h1.home-title").text)

    def test_z_002_text_home_desc_displayed(self):
        self.assertEqual(u"Видео, конспекты, тесты, тренажеры",
                         self.driver.find_element_by_css_selector("p.home-title_small").text)

    def test_z_003_button_subjects(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Предметы"))

    def test_z_004_button_grades(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Классы"))

    def test_z_005_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.home-search"))

    def test_z_006_button_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.home-search__button"))

    def test_z_007_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[1]"))

    def test_z_008_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[2]"))

    def test_z_009_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[3]"))

    def test_z_10_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[4]"))

    def test_z_11_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[5]"))

    def test_z_12_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[6]"))

    def test_z_13_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[7]"))

    def test_z_14_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[8]"))

    def test_z_15_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[9]"))

    def test_z_16_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[10]"))

    def test_z_17_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[11]"))

    def test_z_18_ege_grades_displayed_z_(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[12]"))

    def test_z_19_text_displayed_scientists_and_children(self):
        self.assertEqual(u"Ученые — детям",
                         self.driver.find_element_by_css_selector("h3.home-footer__title").text)

    def test_z_20_link_displayed_on_the_screen(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Интересные лекции для школьников"))

    def test_z_21_text_displayed_parents_and_teachers(self):
        self.assertEqual(u"Родителям и учителям",
                         self.driver.find_element_by_xpath("//div[2]/div/div[2]/div/h3").text)

    def test_z_22_link_displayed_the_screen(self):
        self.assertEqual(
            u"Полезные видеолекции: Детская психология, Здоровье ребёнка, Советы специалистов, Психология на Univertv.ru",
            self.driver.find_element_by_css_selector("#app > div.wrapper__column > div > main > div.home-footer > div > div.home-footer__item.col-12.col-md-7 > div > div.col > div > p").text)
