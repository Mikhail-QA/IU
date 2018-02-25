from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import PagePaidLessonComment
from POM.page_paid_lesson import PaidLesson
from POM.url_lesson import URLPaidLesson


class ClickButtonPlayInVideo(StartInterneturokClassMethod):

    def test_open_popup_in_payment_subject(self):
        driver = self.driver
        url_get = URLPaidLesson(driver)
        step_user = PagePaidLessonComment(driver)
        click_comment = PaidLesson(driver)

        url_get.go_algebra_8_grade_test()
        step_user.click_link_comments()
        click_comment.click_button_comment()
        self.assertEquals(u"Зарегистрируйтесь", self.driver.find_element_by_css_selector("h5.popup-header__title").text)
