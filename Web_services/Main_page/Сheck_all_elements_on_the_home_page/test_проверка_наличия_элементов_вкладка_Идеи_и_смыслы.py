"""
Проверить наличия элементов во вкладке Идеии и смыслы
URL: https://interneturok.ru/"	На странице отображаются: http://joxi.ru/E2pLd3xcBvY912
"""

import allure
import time
import pytest
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов в разделе Идеи и смыслы")
@pytest.mark.skip(reason="Убрали Блок Идем и Смыслы")
class CheckIdea(StartInterneturokClassMethod):

    @allure.step("Перейти на страницу Идеи и смыслы")
    def test_1_a_open_block_idea(self):
        self.driver.get("https://fast-staging.interneturok.ru/idei-i-smysly")
        time.sleep(0.5)

    @allure.step("Элемент Логотип отображается")
    def test_logo_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo.header__logo"))

    @allure.step("Элемент Флешка отображается")
    def test_flash_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "i.icon-flash"))

    @allure.step("Кнопка Войти отображается")
    def test_signIn_is_displayed(self):
        self.assertEqual(u"Войти", self.driver.find_element_by_css_selector("span.button.button_login").text)

    @allure.step("В заголовке отображается текст (Уроки школьной программы)")
    def test_text_home_title_displayed(self):
        self.assertEqual(u"Уроки школьной программы",
                         self.driver.find_element_by_css_selector("h1.home-title").text)

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

    @allure.step("Отображается кнопка (Все предметы)")
    def test_button_back_main_page(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.subjects__grades-nav-back-text"))

    @allure.step("Отображается заголовок с текстом (Идеи и смыслы)")
    def test_notification_displayed_ideas_and_meanings(self):
        self.assertEqual(u"Идеи и смыслы",
                         self.driver.find_element_by_css_selector("span.subjects__grades-nav-current").text)

    @allure.step("На главной страницы отображается полле ввода Поиск")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.home-search"))

    @allure.step("На главной страницы в элементе поиска отображается кнопка лупа (Поиск)")
    def test_button_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.home-search__button"))

    @allure.step("Отображается кнопка (Математика за 20 уроков Общие идеи)")
    def test_board_grades1(self):
        self.assertEqual(u"Математика за 20 уроков\nОбщие идеи",
                         self.driver.find_element_by_xpath("//div/main//div/ul/li[1]").text)

    @allure.step("Отображается кнопка (Основы рационального поведения Инструменты размышления)")
    def test_board_grades2(self):
        self.assertEqual(u"Основы рационального поведения\nИнструменты размышления", self.driver.find_element_by_xpath(
            "//a[contains(@href, '/idei-i-smysly/osnovy-ratsionalnogo-povedeniya')]").text)

    @allure.step("Отображается кнопка (Дискуссии и обсуждения Литература, ...)")
    def test_board_grades3(self):
        self.assertEqual(u"Дискуссии и обсуждения\nЛитература, ...", self.driver.find_element_by_xpath(
            "//a[contains(@href, '/idei-i-smysly/diskussii-i-obsuzhdeniya')]").text)

    @allure.step("Отображается кнопка (Полезные интервью)")
    def test_board_grades4(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Полезные интервью"))

    @allure.step("Отображается кнопка (Основные понятия истории)")
    def test_board_grades5(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Основные понятия истории"))

    @allure.step("Отображается кнопка (Опыт внимательного чтения)")
    def test_board_grades6(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Опыт внимательного чтения"))
