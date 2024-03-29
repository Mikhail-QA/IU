import allure
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.setUp import StartInterneturokClassMethod
from POM.page_abonement import PageAbonement
from POM.page_abonement import URLAbonement
from POM.user import AutopaymentMailRu


@allure.feature("Поп-апы для авторизованного пользователя без абонемента")
@allure.story("Проверить на странице Абонемент появления поп-апов при клике на кнопку Оплатить абонемент")
class UserAuthClickButtonBuyTicketOnPageAbonement(StartInterneturokClassMethod):

    def test_000_click_button_buy_ticket_in_header(self):
        driver = self.driver
        step_user = PageAbonement(driver)
        url_get = URLAbonement(driver)
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
        with allure.step("Перейти на страницу урока Абонемент"):
            url_get.go_page_class()
        with allure.step("Нажать на ссылку Оплатить абонемент"):
            url_get.click_link_abonement()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_header()
        with allure.step("П редиректнуло на страницу оплаты"):
            self.driver.switch_to_window(driver.window_handles[1])
            assert self.driver.current_url == 'https://staging.interneturok.ru/payment'

    def test_click_button_buy_ticket_in_footer(self):
        driver = self.driver
        step_user = PageAbonement(driver)
        url_get = URLAbonement(driver)

        with allure.step("Перейти на страницу урока Абонемент"):
            url_get.go_page_class()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            url_get.click_link_abonement()
        with allure.step("В первой кнопке нажать Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_footer()
        with allure.step("П редиректнуло на страницу оплаты"):
            self.driver.switch_to_window(driver.window_handles[2])
            assert self.driver.current_url == 'https://staging.interneturok.ru/payment'
