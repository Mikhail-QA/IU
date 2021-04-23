import allure
import time
from POM.setUp import StartInterneturokClassMethod
from POM.page_abonement import PageAbonement
from POM.page_abonement import URLAbonement


@allure.feature("Поп-апы для не авторизованного пользователя")
@allure.story("Проверить на странице абонемент появления поп-апов при клике на кнопку Оплатить абонемент")
class ClickButtonBuyTicketOnPageAbonement(StartInterneturokClassMethod):

    def test_click_button_buy_ticket_in_header(self):
        driver = self.driver
        step_user = PageAbonement(driver)
        url_get = URLAbonement(driver)

        with allure.step("Перейти на страницу урока Абонемент"):
            url_get.go_page_class()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            url_get.click_link_abonement()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_header()
        with allure.step("П редиректнуло на страницу оплаты"):
            self.driver.switch_to_window(driver.window_handles[2])
            assert self.driver.current_url == 'https://staging.interneturok.ru/payment'

    def test_click_button_buy_ticket_in_footer(self):
        driver = self.driver
        step_user = PageAbonement(driver)
        url_get = URLAbonement(driver)

        with allure.step("Перейти на страницу урока Абонемент"):
            url_get.go_page_class()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            url_get.click_link_abonement()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_footer()
        with allure.step("П редиректнуло на страницу оплаты"):
            self.driver.switch_to_window(driver.window_handles[1])
            assert self.driver.current_url == 'https://staging.interneturok.ru/payment'
