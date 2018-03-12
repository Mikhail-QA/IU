"""
Проверить наличия элементов на странице Алгебра 8 класс в Body
Пользователь не авторизован
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://joxi.ru/vAWbBDLHkK1YM2
"""

import allure
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod
from Web_services.Subject_page.URL import UrlLesson


@allure.feature("Страница Предмет-Класс (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов в Body для не авторизованного пользователя")
class ChecksAllElementsTheBodyUserNotAuth(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 8 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = UrlLesson(StartInterneturokClassMethod)
        go_page.go_algebra_8_grade()

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

    @allure.step("Над учебниками отображается текст (Смотреть уроки как в учебнике:)")
    def test_text_name_books(self):
        self.assertEqual(u"Смотреть уроки как в учебнике:",
                         self.driver.find_element_by_class_name("subject-book__title").text)

    @allure.step("На странице отображается книга (Алгебра 8 класс (Мордкович А.Г.))")
    def test_books_item_one(self):
        self.assertTrue(self.driver.find_element_by_xpath("//div[1]/div[2]/div/div/a[1]"))

    @allure.step("На странице отображается книга (Алгебра 8 класс (Макарычев Ю.Н.))")
    def test_books_item_two(self):
        self.assertTrue(self.driver.find_element_by_xpath("//div[1]/div[2]/div/div/a[2]"))

    @allure.step(
        "Первый блок уроков имеет заголовок (Алгебраические дроби. Арифметические операции над алгебраическими дробями) ")
    def test_zagolovok_temi_yroka(self):
        self.assertEqual(u"Алгебраические дроби. Арифметические операции над алгебраическими дробями",
                         self.driver.find_element_by_xpath("//div/ul/li[1]/h4").text)

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
