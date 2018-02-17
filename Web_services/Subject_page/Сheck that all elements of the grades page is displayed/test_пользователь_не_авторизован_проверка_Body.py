"""
Проверить наличия элементов на странице Алгебра 8 класс в Body
Пользователь не авторизован
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://joxi.ru/vAWbBDLHkK1YM2
"""

from selenium.webdriver.common.by import By
from Interneturok.web_services.app.SetUp import StartInterneturokClassMethod


class ChecksAllElementsTheBodyUserNotAuth(StartInterneturokClassMethod):
    def test_001_open_page(self):
        self.driver.get("https://staging.interneturok.ru/algebra/8-klass")

    def test_title_body(self):
        self.assertEqual(u"Алгебра", self.driver.find_element_by_css_selector("h1.subject-title").text)

    def test_number_grades(self):
        self.assertEqual(u"8 класс", self.driver.find_element_by_css_selector("span.subject-nav__grade").text)

    def test_lesson__notice_text(self):
        self.assertTrue(self.driver.find_element_by_css_selector("a.lesson-paid.ember-view"))

    # def test_lesson__noti2ce_text(self):
    #     self.assertIn("Для просмотра уроков необходим абонемент",
    #                   self.driver.find_element_by_css_selector("main.content.static").text)

    def test_tooltip_lesson(self):
        self.assertTrue(self.driver.find_element_by_css_selector("a.lesson-paid"))

    def test_switcher_link_left(self):
        self.assertTrue(self.driver.find_element_by_css_selector("a.subject-nav_prev"))

    def test_switcher_link_right(self):
        self.assertTrue(self.driver.find_element_by_css_selector("a.subject-nav_next"))

    def test_text_name_books(self):
        self.assertEqual(u"Смотреть уроки как в учебнике:",
                         self.driver.find_element_by_class_name("subject-book__title").text)

    def test_books_item(self):
        self.assertTrue(self.driver.find_element_by_xpath("//div[1]/div[2]/div/div/a[1]"))

    def test_books_item_two(self):
        self.assertTrue(self.driver.find_element_by_xpath("//div[1]/div[2]/div/div/a[2]"))

    def test_zagolovok_temi_yroka(self):
        self.assertEqual(u"Алгебраические дроби. Арифметические операции над алгебраическими дробями",
                         self.driver.find_element_by_xpath("//div/ul/li[1]/h4").text)

    def test_list__item(self):
        self.assertTrue(self.driver.find_element_by_class_name("subject-theme__sublist"))

    def test_ikonki_vkladok_urokov(self):
        self.assertTrue(self.driver.find_element_by_class_name("subject-theme__icons"))

    def test_levyai_list_yrokov(self):
        self.assertTrue(self.driver.find_element_by_css_selector("ul.nav.menu__list"))

    def test_button_review_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.review__close"))
