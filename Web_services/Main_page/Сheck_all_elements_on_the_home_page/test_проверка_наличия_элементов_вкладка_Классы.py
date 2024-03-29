"""
Проверить наличия элементов на главной странице, во вкладке ""Классы""
URL:https://interneturok.ru/grades"	На странице отображаются: http://joxi.ru/52aykXDUGlZDx2
"""

import allure
import time
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов в разделе Классы")
class CheckAllElementsTheGrades(StartInterneturokClassMethod):
    @allure.step("Нажать на кнопку Классы")
    def test_000_click_button_grades(self):
        self.driver.find_element_by_css_selector("div.switcher__wrap.row a:nth-child(2)").click()
        time.sleep(0.5)

    @allure.step("Элемент Логотип отображается")
    def test_logo_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo.header__logo"))

    @allure.step("Кнопка Войти отображается")
    def test_signIn_is_displayed(self):
        self.assertEqual(u"Войти", self.driver.find_element_by_css_selector("span.button.button_login").text)

    @allure.step("В заголовке отображается текст (Уроки школьной программы)")
    def test_text_home_title_displayed(self):
        self.assertEqual(u"Уроки школьной программы", self.driver.find_element_by_css_selector("h1.home-title").text)

    @allure.step("В заголовке отображается текст (Видео, конспекты, тесты, тренажеры)")
    def test_text_home_desc_displayed(self):
        self.assertEqual(u"Видео, конспекты, тесты, тренажеры",
                         self.driver.find_element_by_css_selector("p.home-title_small").text)

    @allure.step("Отображается кнопка (Предметы)")
    def test_button_subjects(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Предметы"))

    @allure.step("Отображается кнопка (Классы)")
    def test_button_grades(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Классы"))

    @allure.step("Отображается полле ввода Поиск")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.home-search"))

    @allure.step("На страницы в элементе поиска отображается кнопка лупа (Поиск)")
    def test_button_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.home-search__button"))

    @allure.step("Отображается кнопка (1 класс)")
    def test_1_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[1]"))

    @allure.step("Отображается кнопка (2 класс)")
    def test_2_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[2]"))

    @allure.step("Отображается кнопка (3 класс)")
    def test_3_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[3]"))

    @allure.step("Отображается кнопка (4 класс)")
    def test_4_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[4]"))

    @allure.step("Отображается кнопка (5 класс)")
    def test_5_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[5]"))

    @allure.step("Отображается кнопка (6 класс)")
    def test_6_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[6]"))

    @allure.step("Отображается кнопка (7 класс)")
    def test_7_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[7]"))

    @allure.step("Отображается кнопка (8 класс)")
    def test_8_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[8]"))

    @allure.step("Отображается кнопка (9 класс)")
    def test_9_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[9]"))

    @allure.step("Отображается кнопка (10 класс)")
    def test_10_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[10]"))

    @allure.step("Отображается кнопка (11 класс)")
    def test_11_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[11]"))

    @allure.step("Отображается кнопка (ЕГЭ Курс)")
    def test_ege_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[1]/ul/li[12]"))
