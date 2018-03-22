"""
Проверить наличия элементов во вкладке ""Классы --> 1 класс""
URL: https://interneturok.ru/grades/1?_=1503573733002"	На странице отображаются: http://joxi.ru/EA41kdxTDXKbjr
"""

import allure
import time
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов в разделе Классы, 1 Класс")
class CheckAllElementsTheGradesOneSubject(StartInterneturokClassMethod):
    @allure.step("Нажать на кнопку Классы")
    def test_001_click_button_grades(self):
        self.driver.find_element_by_xpath("//main/nav/div/a[2]").click()
        time.sleep(0.5)
        with allure.step("В сетке классов перейти в 1 Класс"):
            self.driver.find_element_by_xpath("//div[1]/ul/li[1]").click()
            time.sleep(0.5)

    @allure.step("В заголовке отображается текст (Уроки школьной программы)")
    def test_text_home_title_displayed(self):
        self.assertEqual(u"Уроки школьной программы", self.driver.find_element_by_css_selector("h1.home-title").text)

    @allure.step("В заголовке отображается текст (Видео, конспекты, тесты, тренажеры)")
    def test_text_home_desc_displayed(self):
        self.assertEqual(u"Видео, конспекты, тесты, тренажеры",
                         self.driver.find_element_by_css_selector("p.home-title_small").text)

    @allure.step("На страницы отображается кнопка (Предметы)")
    def test_button_subjects(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Предметы"))

    @allure.step("На страницы отображается кнопка (Классы)")
    def test_button_grades(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Классы"))

    @allure.step("На страницы отображается полле ввода Поиск")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.home-search"))

    @allure.step("На страницы в элементе поиска отображается кнопка лупа (Поиск)")
    def test_button_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.home-search__button"))

    @allure.step("На страницы отображается кнопка (Все классы)")
    def test_button_back_main_page(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.subjects__grades-nav-back"))

    @allure.step("На страницы отображается Title класса (1 класс)")
    def test_title_the_subject(self):
        self.assertEqual(u"1 класс", self.driver.find_element_by_css_selector("span.subjects__grades-nav-current").text)

    @allure.step("На странице отображается кнопка листать Влево")
    def test_displayed_button_in_left(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div[2]/div/main/div[2]/div/div/div[1]/span[1]"))

    @allure.step("На странице отображается кнопка листать Вправо")
    def test_displayed_button_in_right(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.subjects__grades-nav-button-next"))

    @allure.step("На страницы отображается кнопка (Математика)")
    def test_button_matematika(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Математика"))

    @allure.step("На страницы отображается кнопка (Окружающий мир)")
    def test_button_OKM(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Окружающий мир"))

    @allure.step("На страницы отображается кнопка (Русский язык)")
    def test_button_russian_language(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Русский язык"))

    @allure.step("На страницы отображается кнопка (Чтение)")
    def test_button_reading(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Чтение"))
