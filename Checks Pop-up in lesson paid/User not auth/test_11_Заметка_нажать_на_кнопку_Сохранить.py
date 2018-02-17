from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import Notes
from POM.url_lesson import URLPaidLesson


class ClickButtonPlayInVideo(StartInterneturokClassMethod):

    def test_open_popup_in_payment_subject(self):
        driver = self.driver
        step_user = Notes(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_questions()
        step_user.open_notes()
        step_user.save_note()
        self.assertEquals(u"Войдите в профиль", self.driver.find_element_by_css_selector("h5.popup-header__title").text)
