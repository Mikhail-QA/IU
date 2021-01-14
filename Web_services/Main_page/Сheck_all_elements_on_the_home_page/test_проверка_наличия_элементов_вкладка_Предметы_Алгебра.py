"""
Проверить наличия элементов, во вкладке ""Предметы --> Алгебра""
URL:https://interneturok.ru/subjects"	На странице отображаются: http://joxi.ru/p2715ZyT0LEvZr
"""

import allure
import time
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов в разделе Предмет (Алгебра)")
class CheckAllElementsTheSubject(StartInterneturokClassMethod):
    def test_000_go_old_main_page(self):
        self.driver.get('https://staging.interneturok.ru/subject/algebra')
        self.driver.find_element_by_css_selector('span.subjects__grades-nav-back-text').click()
        time.sleep(2)

    @allure.step("Нажать на Предмет Алгебра")
    def test_001_click_button_Algebra(self):
        self.driver.find_element_by_xpath("//div/div/div[1]/ul/li[1]/a").click()
        time.sleep(1)

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

    @allure.step("На главной страницы отображается полле ввода Поиск")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.home-search"))

    @allure.step("На главной страницы в элементе поиска отображается кнопка лупа (Поиск)")
    def test_button_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.home-search__button"))

    @allure.step("На страницы отображается кнопка (Все предметы)")
    def test_button_back_main_page(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.subjects__grades-nav-back"))

    @allure.step("На странице отображается кнопка листать Влево")
    def test_button_in_left_displayed(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "<"))

    @allure.step("На страницы отображается Title предмета (Алгебра)")
    def test_text_displayed(self):
        self.assertEqual(u"Алгебра", self.driver.find_element_by_css_selector("span.subjects__grades-nav-current").text)

    @allure.step("На странице отображается кнопка листать Вправо")
    def test_button_in_right_displayed(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, ">"))

    @allure.step("На страницы отображается кнопка (7 класс)")
    def test_button_7_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[1]/a"))

    @allure.step("На страницы отображается кнопка (8 класс)")
    def test_button_8_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[2]/a"))

    @allure.step("На страницы отображается кнопка (9 класс)")
    def test_button_9_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[3]/a"))

    @allure.step("На страницы отображается кнопка (10 класс)")
    def test_button_10_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[4]/a"))

    @allure.step("На страницы отображается кнопка (11 класс)")
    def test_button_11_algebra(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[5]/a"))

    @allure.step("На страницы отображается кнопка (ЕГЭ курс)")
    def test_button_ege(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//div/div/div[1]/ul/li[6]/a"))
