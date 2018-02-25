from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import PaidLesson
from POM.url_lesson import URLPaidLesson


class ClickButtonBuyTicketInPayLesson(StartInterneturokClassMethod):

    def test_click_button_buy_ticket_in_stub_video(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_video()
        step_user.click_button_buy_ticket_in_stubs()
        self.assertEquals(u"Зарегистрируйтесь", self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_buy_ticket_in_stub_trainers(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_trainers()
        step_user.click_button_buy_ticket_in_stubs()
        self.assertEquals(u"Зарегистрируйтесь", self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_buy_ticket_in_stub_questions(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_questions()
        step_user.click_button_buy_ticket_in_stubs()
        self.assertEquals(u"Зарегистрируйтесь", self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_buy_ticket_in_stub_test(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_test()
        step_user.click_button_buy_ticket_in_stubs()
        self.assertEquals(u"Зарегистрируйтесь", self.driver.find_element_by_css_selector("h5.popup-header__title").text)
