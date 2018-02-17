"""
Проверить наличия элементов на странице Алгебра 8 класс в Header вкладка Предметы
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://prntscr.com/gev0y8
"""
import time
from Interneturok.web_services.app.SetUp import StartInterneturokClassMethod
from selenium.webdriver import ActionChains


class CheckAllElementInGrade(StartInterneturokClassMethod):
    def test_001_go_page(self):
        self.driver.get("https://staging.interneturok.ru/algebra/8-klass")
        time.sleep(2)
        element_to_hover_over = self.driver.find_element_by_xpath("//header/div[1]/div[2]")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(2)

    def test_algebra_subject(self):
        self.assertIn(u"Алгебра", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_geometrya_subject(self):
        self.assertIn(u"Геометрия", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_matematika_subject(self):
        self.assertIn(u"Математика", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_informatika_subject(self):
        self.assertIn(u"Информатика", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_objestvo_subject(self):
        self.assertIn(u"Обществознание", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_OBJ_subject(self):
        self.assertIn(u"ОБЖ", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_fizika_subject(self):
        self.assertIn(u"Физика", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_himiya_subject(self):
        self.assertIn(u"Химия", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_biologi_subject(self):
        self.assertIn(u"Биология", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_geografiya_subject(self):
        self.assertIn(u"География", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_prirodavedenie_subject(self):
        self.assertIn(u"Природоведение", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_okryjauchiymir_subject(self):
        self.assertIn(u"Окружающий мир", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_russian_language_subject(self):
        self.assertIn(u"Русский язык", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_literatura_subject(self):
        self.assertIn(u"Литература", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_istoriya_russia_subject(self):
        self.assertIn(u"История России", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_vseobchayaistoriya_subject(self):
        self.assertIn(u"Всеобщая история", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_english_language_subject(self):
        self.assertIn(u"Английский язык", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_chtenie_subject(self):
        self.assertIn(u"Чтение", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    def test_icon_payment(self):
        self.assertTrue(self.driver.find_element_by_css_selector("li.subjects__tab-payment"))