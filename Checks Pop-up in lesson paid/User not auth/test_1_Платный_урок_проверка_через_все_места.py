from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import PaidLesson
from POM.url_lesson import URLPaidLesson
from POM.page_paid_lesson import Notes
from POM.page_paid_lesson import Favourites
from POM.page_paid_lesson import Value
from POM.page_paid_lesson import PagePaidLessonComment


class CheckAppearancePopUpInAllPlaces(StartInterneturokClassMethod):

    def test_click_button_play_in_stub_video(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        get_url = URLPaidLesson(driver)

        get_url.go_algebra_8_grade_video()
        step_user.click_button_play_video()
        self.assertEquals(u"Зарегистрируйтесь",
                          self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_comment_in_tab_ask_question(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_questions()
        step_user.click_button_comments()
        self.assertEquals(u"Зарегистрируйтесь", self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_save_in_note(self):
        driver = self.driver
        step_user = Notes(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_questions()
        step_user.open_notes()
        step_user.save_note()
        self.assertEquals(u"Войдите в профиль", self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_input_field_in_note(self):
        driver = self.driver
        step_user = Notes(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_questions()
        step_user.open_notes()
        step_user.click_textarea()
        self.assertEquals(u"Войдите в профиль", self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_favourites(self):
        driver = self.driver
        step_user = Favourites(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_questions()
        step_user.click_button_favourites()
        self.assertEquals(u"Войдите в профиль", self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_value_lesson(self):
        driver = self.driver
        step_user = Value(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_questions()
        step_user.click_button_value_lesson()
        self.assertEquals(u"Войдите в профиль", self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_send_in_tab_comment(self):
        driver = self.driver
        step_user = PagePaidLessonComment(driver)
        url_get = URLPaidLesson(driver)

        url_get.go_algebra_8_grade_questions()
        step_user.click_link_comments()
        step_user.click_button_send()
        self.assertEquals(u"Войдите в профиль", self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_input_field_in_comment(self):
        driver = self.driver
        url_get = URLPaidLesson(driver)
        step_user = PagePaidLessonComment(driver)
        click_comment = PaidLesson(driver)

        url_get.go_algebra_8_grade_test()
        step_user.click_link_comments()
        click_comment.click_button_comments()
        self.assertEquals(u"Зарегистрируйтесь", self.driver.find_element_by_css_selector("h5.popup-header__title").text)
