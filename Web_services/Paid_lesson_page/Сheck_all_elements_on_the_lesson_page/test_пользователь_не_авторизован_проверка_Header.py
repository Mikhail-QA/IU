import allure
from selenium.webdriver.common.by import By
from Web_services.URL import PaidLessonPage
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Страница урока Основные понятия (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов в Header для не авторизованного пользователя")
class ChecksAllElementsInLessonPageTheHeadersUserNotAuth(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 8 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = PaidLessonPage(StartInterneturokClassMethod)
        go_page.go_lesson_page()

    @allure.step("Элемент Логотип отображается")
    def test_logo_interneturok(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo.header__logo"))

    @allure.step("Кнопка возврата на страницу Предмет/Класс отображается (Алгебра,8)")
    def test_button_back_page_subject(self):
        self.assertEqual("Алгебра,11", self.driver.find_element_by_css_selector("a.header__back").text)

    @allure.step("Кнопка Предметы отображается")
    def test_button_subjects_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//header/div[1]/div[2]"))

    @allure.step("Кнопка Классы отображается")
    def test_button_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//header/div[1]/div[1]"))

    @allure.step("Элемент Поиск отображается")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.header-search__wraps"))

    @allure.step("Кнопка Флешка отображается")
    def test_button_flash(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "i.icon-flash"))

    @allure.step("Кнопка Войти отображается")
    def test_button_enter_is_displayed(self):
        self.assertEqual(u"Войти", self.driver.find_element_by_css_selector("div.header-menu-wrapper").text)
