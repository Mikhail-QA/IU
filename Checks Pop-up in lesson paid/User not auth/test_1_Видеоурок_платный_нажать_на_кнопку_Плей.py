from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import PaidLesson
from POM.url_lesson import URLPaidLesson


class ClickButtonPlayInVideo(StartInterneturokClassMethod):

    def test_open_popup_in_payment_subject(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        get_url = URLPaidLesson(driver)

        get_url.go_algebra_8_grade_video()
        step_user.click_button_play_video()
        self.assertEquals(u"Зарегистрируйтесь",
                          self.driver.find_element_by_css_selector("h5.popup-header__title").text)
