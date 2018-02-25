import allure
from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import PaidLesson
from POM.url_lesson import URLPaidLesson


@allure.feature("Поп-апы")
@allure.story("Не авторизованным П проверяю в платном уроке появления поп-апов при клике на кнопку Оплатить абонемент")
class ClickButtonBuyTicketInPayLesson(StartInterneturokClassMethod):

    def test_click_button_buy_ticket_in_stub_video(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкалдку Видеоурок"):
            url_get.go_algebra_8_grade_video()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_stubs()
        with allure.step("Поп-ап Регистрации появился"):
            self.assertEquals(u"Зарегистрируйтесь",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_buy_ticket_in_stub_trainers(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкалдку Тренажёры"):
            url_get.go_algebra_8_grade_trainers()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_stubs()
        with allure.step("Поп-ап Регистрации появился"):
            self.assertEquals(u"Зарегистрируйтесь",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_buy_ticket_in_stub_questions(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкалдку Вопросы к уроку"):
            url_get.go_algebra_8_grade_questions()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_stubs()
        with allure.step("Поп-ап Регистрации появился"):
            self.assertEquals(u"Зарегистрируйтесь",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_buy_ticket_in_stub_test(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкалдку Тесты"):
            url_get.go_algebra_8_grade_test()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            step_user.click_button_buy_ticket_in_stubs()
        with allure.step("Поп-ап Регистрации появился"):
            self.assertEquals(u"Зарегистрируйтесь",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)
