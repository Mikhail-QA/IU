"""
Проверить наличия элементов на странице Алгебра 8 класс в  Header вкладка Классы
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://prntscr.com/gev0sx
"""
import allure
import time
from Web_services.URL import SubjectPage
from Web_services.app.SetUp import StartInterneturokClassMethod
from selenium.webdriver import ActionChains


@allure.feature("Страница Предмет-Класс (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов в открытой кнопке Классы")
class CheckAllElementInGrade(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 8 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = SubjectPage(StartInterneturokClassMethod)
        go_page.go_algebra_8_grade()

    @allure.step("Навести мышку на кнопку Классы")
    def test_1_hover_mouse_button_grades(self):
        time.sleep(2)
        element_to_hover_over = self.driver.find_element_by_xpath("//header/div[1]/div[1]")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(2)

    @allure.step("В списке отображается 1 класс")
    def test_grade_1(self):
        self.assertIn(u"1 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 2 класс")
    def test_grade_2(self):
        self.assertIn(u"2 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 3 класс")
    def test_grade_3(self):
        self.assertIn(u"3 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 4 класс")
    def test_grade_4(self):
        self.assertIn(u"4 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 5 класс")
    def test_grade_5(self):
        self.assertIn(u"5 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 6 класс")
    def test_grade_6(self):
        self.assertIn(u"6 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 7 класс")
    def test_grade_7(self):
        self.assertIn(u"7 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 8 класс")
    def test_grade_8(self):
        self.assertIn(u"8 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 9 класс")
    def test_grade_9(self):
        self.assertIn(u"9 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 10 класс")
    def test_grade_10(self):
        self.assertIn(u"10 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается 11 класс")
    def test_grade_11(self):
        self.assertIn(u"11 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    @allure.step("В списке отображается кнопка ЕГЭ")
    def test_ege_grade(self):
        self.assertIn(u"ЕГЭ", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)
