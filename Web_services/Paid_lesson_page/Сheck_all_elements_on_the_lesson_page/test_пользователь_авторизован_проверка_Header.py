import allure
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.main_page import MainPage
from Web_services.URL import PaidLessonPage


@allure.feature("Страница урока Основные понятия (Алгебра 11 класс)")
@allure.story("Проверка наличия элементов в Header для авторизованного пользователя")
class ChecksAllElementsInLessonPageTheHeadersUserAuth(StartInterneturokClassMethod):
    @allure.step("Авторизоваться пользователем")
    def test_000_logged_user(self):
        StartInterneturokClassMethod = self.driver
        steps_main = MainPage(StartInterneturokClassMethod)
        steps_user = AutopaymentMailRu(StartInterneturokClassMethod)
        steps_popup = PopupSignIn(StartInterneturokClassMethod)
        go_page = PaidLessonPage(StartInterneturokClassMethod)
        steps_main.go_to_sgnIn()
        steps_user.enter_email()
        steps_user.enter_password()
        steps_popup.click_button_login()
        go_page.go_lesson_page()

    @allure.step("Элемент Логотип отображается")
    def test_logo_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo.header__logo"))

    @allure.step("Кнопка возврата на страницу Предмет/Класс отображается (Алгебра,11)")
    def test_button_back_page_subject(self):
        self.assertEqual("Алгебра, 11 класс",
                         self.driver.find_element_by_css_selector("a.breadcrumbs__link.ember-view").text)

    @allure.step("Кнопка Предметы отображается")
    def test_button_subjects_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.header-menu-grades"))

    @allure.step("Кнопка Классы отображается")
    def test_button_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.header-menu-subjects"))

    @allure.step("Элемент Поиск отображается")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    @allure.step("Кнопка Мой профиль отображается")
    def test_button_signIn_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.header-userinfo"))

    @allure.step("Кнопка меню-бургер отображается")
    def test_button_signIn_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.ember-basic-dropdown"))
