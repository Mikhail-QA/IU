import allure
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import PaidLesson
from POM.url_lesson import URLPaidLesson
from POM.user import AutopaymentMailRu


@allure.feature("Поп-апы для авторизованного пользователя без абонемента")
@allure.story("Авторизованный П проверить в платном уроке появления поп-апов при клике на кнопку Оплатить абонемент")
class UserAuthClickButtonBuyTicketInPayLesson(StartInterneturokClassMethod):

    def test_000_click_button_buy_ticket_in_stub_video(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)
        data_user = AutopaymentMailRu(driver)
        open_popup = MainPage(driver)
        click_enter = PopupSignIn(driver)

        with allure.step("Нажать на кнопку Войти"):
            open_popup.go_to_sgnIn()
        with allure.step("В поп-апе авторизации ввести email/password"):
            data_user.enter_email()
            data_user.enter_password()
        with allure.step("В поп-апе авторизации Нажать на кнопку Войти"):
            click_enter.click_button_login()
        with allure.step("Перейти на страницу урока во вкалдку Видеоурок"):
            url_get.go_chemistry_8_grade_video()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_stubs()
        with allure.step("П редиректнуло на страницу оплаты"):
            self.driver.switch_to_window(driver.window_handles[1])
            assert self.driver.current_url == 'https://staging.interneturok.ru/payment'

    def test_click_button_buy_ticket_in_stub_trainers(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкалдку Тренажёры"):
            url_get.go_physics_7_grade_trainers()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_stubs()
        with allure.step("П редиректнуло на страницу оплаты"):
            self.driver.switch_to_window(driver.window_handles[4])
            assert self.driver.current_url == 'https://staging.interneturok.ru/payment'

    def test_click_button_buy_ticket_in_stub_test(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкалдку Тесты"):
            url_get.go_algebra_8_grade_test()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_stubs()
        with allure.step("П редиректнуло на страницу оплаты"):
            self.driver.switch_to_window(driver.window_handles[3])
            assert self.driver.current_url == 'https://staging.interneturok.ru/payment'

    def test_click_button_buy_ticket_in_stub_questions(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкалдку Вопросы к уроку"):
            url_get.go_chemistry_8_grade_questions()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_stubs()
        with allure.step("П редиректнуло на страницу оплаты"):
            self.driver.switch_to_window(driver.window_handles[2])
            assert self.driver.current_url == 'https://staging.interneturok.ru/payment'
