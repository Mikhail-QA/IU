"""
Проверить наличия элементов на странице Алгебра 8 класс в  Header вкладка Классы
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://prntscr.com/gev0sx
"""
import time
from Web_services.app.SetUp import StartInterneturokClassMethod
from selenium.webdriver import ActionChains


class CheckAllElementInGrade(StartInterneturokClassMethod):
    def test_001_go_page(self):
        self.driver.get("https://fast-staging.interneturok.ru/algebra/8-klass")
        time.sleep(2)
        element_to_hover_over = self.driver.find_element_by_xpath("//header/div[1]/div[1]")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(2)

    def test_001_grade(self):
        self.assertIn(u"1 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_002_grade(self):
        self.assertIn(u"2 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_003_grade(self):
        self.assertIn(u"3 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_004_grade(self):
        self.assertIn(u"4 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_005_grade(self):
        self.assertIn(u"5 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_006_grade(self):
        self.assertIn(u"6 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_007_grade(self):
        self.assertIn(u"7 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_008_grade(self):
        self.assertIn(u"8 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_009_grade(self):
        self.assertIn(u"9 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_10_grade(self):
        self.assertIn(u"10 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_11_grade(self):
        self.assertIn(u"11 класс", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)

    def test_ege_grade(self):
        self.assertIn(u"ЕГЭ", self.driver.find_element_by_xpath("//header/div[1]/div[1]").text)
