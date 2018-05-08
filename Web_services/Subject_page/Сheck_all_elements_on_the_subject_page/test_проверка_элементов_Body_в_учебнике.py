"""
Проверить наличия элементов на странице Алгебра 8 класс в Body в учебнике "Алгебра 8 класс (Мордкович А.Г.)"
На странице отображаются: http://joxi.ru/vAWbBDLHkK1YM2
"""

import allure
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod
from Web_services.URL import SubjectPage
from POM.page_paid_subject_grades import PaidLessonAlgebra8


@allure.feature("Страница Предмет-Класс в открытом учебнике (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов в Body в учебнике (Алгебра 8 класс (Мордкович А.Г.)")
class ChecksAllElementsInSubjectPageTheBodyInOpenBook(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 8 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = SubjectPage(StartInterneturokClassMethod)
        open_book = PaidLessonAlgebra8(StartInterneturokClassMethod)
        go_page.go_algebra_8_grade()
        open_book.click_button_open_book()

    @allure.step("Отображается заголовок (Алгебра)")
    def test_title_body(self):
        self.assertEqual(u"Алгебра", self.driver.find_element_by_css_selector("h1.subject-title").text)

    @allure.step("Отображается заголовок (8 класс)")
    def test_number_grades(self):
        self.assertEqual(u"8 класс", self.driver.find_element_by_css_selector("span.subject-nav__grade").text)

    @allure.step("Отображается иконка (Звезда платный урок)")
    def test_abonement_widget_displayed(self):
        self.assertTrue(self.driver.find_element_by_css_selector("a.lesson-paid"))

    @allure.step("Отображается кнопка перехода на 7 класс")
    def test_switcher_link_left(self):
        self.assertTrue(self.driver.find_element_by_css_selector("a.subject-nav_prev"))

    @allure.step("Отображается кнопка перехода на 9 класс")
    def test_switcher_link_right(self):
        self.assertTrue(self.driver.find_element_by_css_selector("a.subject-nav_next"))

    @allure.step("Над учебниками отображается текст (Алгебра 8 класс (Мордкович А.Г.))")
    def test_text_name_books(self):
        self.assertEqual(u"Алгебра 8 класс (Мордкович А.Г.)",
                         self.driver.find_element_by_css_selector("span.subject-book__title").text)

    @allure.step("На странице отображается книга (Алгебра 8 класс (Мордкович А.Г.))")
    def test_books_item_one(self):
        self.assertTrue(
            self.driver.find_element_by_css_selector(
                ".subject-book__body-inner:nth-child(1) .subject-book:nth-child(1)"))

    @allure.step("На странице отображается книга (Алгебра 8 класс (Колмогоров А.Н.))")
    def test_books_item_two(self):
        self.assertTrue(
            self.driver.find_element_by_css_selector(
                ".subject-book__body-inner:nth-child(1) .subject-book:nth-child(2)"))

    @allure.step("В открытом учебнике отображается кнопка (Закрыть учебник)")
    def test_switcher_link_right(self):
        self.assertEqual("Закрыть учебник",
                         self.driver.find_element_by_css_selector("span.subject-book__close-text").text)

    @allure.step("В открытом учебнике напротив кнопки Закрыть учебник отображается (крестик)")
    def test_switcher_link_right(self):
        self.assertTrue(self.driver.find_element_by_css_selector("span.subject-book__close-icon"))

    @allure.step(
        "Первый блок уроков имеет заголовок (Глава 1. АЛГЕБРАИЧЕСКИЕ ДРОБИ) ")
    def test_zagolovok_temi_yroka(self):
        self.assertEqual(u"Глава 1. АЛГЕБРАИЧЕСКИЕ ДРОБИ", self.driver.find_element_by_xpath("//div/ul/li[1]/h4").text)

    @allure.step("Отображается список уроков")
    def test_list__item(self):
        self.assertTrue(self.driver.find_element_by_class_name("subject-theme__sublist"))

    @allure.step("Отображается вкладки урока")
    def test_icon_tab_grades(self):
        self.assertTrue(self.driver.find_element_by_class_name("subject-theme__icons"))

    @allure.step("Отображается вкладка урока (Видеоурок)")
    def test_mini_icon_video_displayed(self):
        self.assertTrue(self.driver.find_element_by_class_name("icon-video"))

    @allure.step("Отображается вкладка урока (Текстовый урок)")
    def test_mini_icon_text_displayed(self):
        self.assertTrue(self.driver.find_element_by_class_name("icon-text"))

    @allure.step("Отображается вкладка урока (Тренажеры)")
    def test_mini_icon_trainers_displayed(self):
        self.assertTrue(self.driver.find_element_by_class_name("icon-trainers"))

    @allure.step("Отображается вкладка урока (Тесты)")
    def test_mini_icon_test_displayed(self):
        self.assertTrue(self.driver.find_element_by_class_name("icon-test"))

    @allure.step("Отображается список тем урока")
    def test_levyai_list_yrokov(self):
        self.assertTrue(self.driver.find_element_by_css_selector("ul.nav.menu__list"))

    @allure.step("Отображается кнопка (Оставить отзыв)")
    def test_button_review_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.review__close"))
