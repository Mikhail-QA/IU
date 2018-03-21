import allure
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.main_page import MainPage
from Web_services.URL import Paid_lesson_page


@allure.feature("Страница урока Основные понятия (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов в Header для авторизованного пользователя")
class ChecksAllElementsInLessonPageTheHeadersUserAuth(StartInterneturokClassMethod):
    @allure.step("Авторизоваться пользователем")
    def test_000_logged_user(self):
        StartInterneturokClassMethod = self.driver
        steps_main = MainPage(StartInterneturokClassMethod)
        steps_user = AutopaymentMailRu(StartInterneturokClassMethod)
        steps_popup = PopupSignIn(StartInterneturokClassMethod)
        go_page = Paid_lesson_page(StartInterneturokClassMethod)
        steps_main.go_to_sgnIn()
        steps_user.enter_email()
        steps_user.enter_password()
        steps_popup.click_button_login()
        go_page.go_lesson_page()

    @allure.step("Элемент Логотип отображается")
    def test_logo_is_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.logo.header__logo"))

    @allure.step("Кнопка возврата на страницу Предмет/Класс отображается (Алгебра,8)")
    def test_button_back_page_subject(self):
        self.assertEqual("Алгебра,8", self.driver.find_element_by_css_selector("a.header__back").text)

    @allure.step("Кнопка Предметы отображается")
    def test_button_subjects_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//header/div[1]/div[2]"))

    @allure.step("Кнопка Классы отображается")
    def test_button_grades_displayed(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//header/div[1]/div[1]"))

    @allure.step("Элемент Поиск отображается")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.NAME, "query"))

    @allure.step("Кнопка Флешка отображается")
    def test_flash_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon.icon-flash"))

    @allure.step("Кнопка Мой профиль отображается")
    def test_button_signIn_is_displayed(self):
        self.assertEqual(u"Мой профиль", self.driver.find_element_by_css_selector("div.header__menu_profile").text)
