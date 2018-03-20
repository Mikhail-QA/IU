"""
Проверить наличия элементов на странице Алгебра 8 класс в Header вкладка Предметы
URL: https://web-dev01.interneturok.ru/algebra/8-klass"
На странице отображаются: http://prntscr.com/gev0y8
"""
import allure
import time
from Web_services.URL import SubjectPage
from Web_services.app.SetUp import StartInterneturokClassMethod
from selenium.webdriver import ActionChains


@allure.feature("Страница Предмет-Класс (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов в открытой кнопке Предметы")
class CheckAllElementInSubject(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 8 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = SubjectPage(StartInterneturokClassMethod)
        go_page.go_algebra_8_grade()

    @allure.step("Навести мышку на кнопку Предметы")
    def test_001_hover_mouse_button_grades(self):
        time.sleep(2)
        element_to_hover_over = self.driver.find_element_by_xpath("//header/div[1]/div[2]")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(2)

    @allure.step("В списке отображается предмет (Алгебра)")
    def test_algebra_subject(self):
        self.assertIn(u"Алгебра", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Геометрия)")
    def test_geometrya_subject(self):
        self.assertIn(u"Геометрия", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Математика)")
    def test_matematika_subject(self):
        self.assertIn(u"Математика", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Информатика)")
    def test_informatika_subject(self):
        self.assertIn(u"Информатика", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Обществознание)")
    def test_objestvo_subject(self):
        self.assertIn(u"Обществознание", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (ОБЖ)")
    def test_OBJ_subject(self):
        self.assertIn(u"ОБЖ", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Физика)")
    def test_fizika_subject(self):
        self.assertIn(u"Физика", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Химия)")
    def test_himiya_subject(self):
        self.assertIn(u"Химия", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Биология)")
    def test_biologi_subject(self):
        self.assertIn(u"Биология", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (География)")
    def test_geografiya_subject(self):
        self.assertIn(u"География", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Природоведение)")
    def test_prirodavedenie_subject(self):
        self.assertIn(u"Природоведение", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Окружающий мир)")
    def test_okryjauchiymir_subject(self):
        self.assertIn(u"Окружающий мир", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Русский язык)")
    def test_russian_language_subject(self):
        self.assertIn(u"Русский язык", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Литература)")
    def test_literatura_subject(self):
        self.assertIn(u"Литература", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (История России)")
    def test_istoriya_russia_subject(self):
        self.assertIn(u"История России", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Всеобщая история)")
    def test_vseobchayaistoriya_subject(self):
        self.assertIn(u"Всеобщая история", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Английский язык)")
    def test_english_language_subject(self):
        self.assertIn(u"Английский язык", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)

    @allure.step("В списке отображается предмет (Чтение)")
    def test_chtenie_subject(self):
        self.assertIn(u"Чтение", self.driver.find_element_by_xpath("//header/div[1]/div[2]").text)
