import allure
from POM.setUp import StartInterneturokClassMethod
from POM.page_abonement import PageAbonement
from POM.page_abonement import URLAbonement


@allure.feature("Поп-апы для не авторизованного пользователя")
@allure.story("Проверяю на странице абонемент появления поп-апов при клике на кнопку Оплатить абонемент")
class ClickButtonBuyTicketOnPageAbonement(StartInterneturokClassMethod):

    def test_click_button_buy_ticket_in_header(self):
        driver = self.driver
        step_user = PageAbonement(driver)
        url_get = URLAbonement(driver)

        with allure.step("Перейти на страницу урока Абонемент"):
            url_get.go_page_abonement()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_header()
        with allure.step("Поп-ап Регистрации появился"):
            self.assertEqual(u"Зарегистрируйтесь",
                             self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_buy_ticket_in_footer(self):
        driver = self.driver
        step_user = PageAbonement(driver)
        url_get = URLAbonement(driver)

        with allure.step("Перейти на страницу урока Абонемент"):
            url_get.go_page_abonement()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_footer()
        with allure.step("Поп-ап Регистрации появился"):
            self.assertEqual(u"Зарегистрируйтесь",
                             self.driver.find_element_by_css_selector("h5.popup-header__title").text)
