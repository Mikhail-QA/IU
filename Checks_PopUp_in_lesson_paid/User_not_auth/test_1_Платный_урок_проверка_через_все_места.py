import allure
from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import PaidLesson
from POM.url_lesson import URLPaidLesson
from POM.page_paid_lesson import Notes
from POM.page_paid_lesson import LessonFooter
from POM.page_paid_lesson import Value
from POM.page_paid_lesson import PagePaidLessonComment
from POM.page_paid_lesson import PagePaidLessonQuestion


@allure.feature("Поп-апы для не авторизованного пользователя")
@allure.story("Не авторизованным П проверяю в платном уроке появления поп-апов во всех местах кроме заглушки")
class CheckAppearancePopUpInAllPlaces(StartInterneturokClassMethod):

    def test_click_button_play_in_stub_video(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        get_url = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкалдку Видеоурок"):
            get_url.go_chemistry_8_grade_video()
        with allure.step("Нажать на кнопку Плей"):
            step_user.click_button_play_video()
        with allure.step("Поп-ап Регистрации Появился"):
            self.assertEquals(u"Зарегистрируйтесь",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_comment_in_tab_ask_question(self):
        driver = self.driver
        step_user = PagePaidLessonQuestion(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкалдку Вопросы к уроку"):
            url_get.go_algebra_8_grade_questions()
        with allure.step("Нажать на кнопку Комментировать"):
            step_user.click_button_comment()
        with allure.step("Поп-ап Регистрации появился"):
            self.assertEquals(u"Зарегистрируйтесь",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_save_in_note(self):
        driver = self.driver
        step_user = Notes(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_algebra_8_grade_test()
        with allure.step("Нажать на кнопку Заметки"):
            step_user.open_notes()
        with allure.step("Нажать на кнопку Сохранить"):
            step_user.save_note()
        with allure.step("Поп-ап Авторизации появился"):
            self.assertEquals(u"Войдите в профиль",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_input_field_in_note(self):
        driver = self.driver
        step_user = Notes(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_algebra_8_grade_test()
        with allure.step("Нажать на кнопку Заметки"):
            step_user.open_notes()
        with allure.step("Кликнуть мышкой в поле ввода текста"):
            step_user.click_textarea()
        with allure.step("Поп-ап Авторизации появился"):
            self.assertEquals(u"Войдите в профиль",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_favourites(self):
        driver = self.driver
        step_user = LessonFooter(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_algebra_8_grade_questions()
        with allure.step("В подвале сайта нажать на кнопку В Избранное"):
            step_user.click_button_favourites()
        with allure.step("Поп-ап Авторизации появился"):
            self.assertEquals(u"Войдите в профиль",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_value_lesson(self):
        driver = self.driver
        step_user = Value(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_algebra_8_grade_questions()
        with allure.step("В подвале сайта нажать на кнопку Оценить урок"):
            step_user.click_button_value_lesson()
        with allure.step("Поп-ап Авторизации появился"):
            self.assertEquals(u"Войдите в профиль",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_send_in_tab_comment(self):
        driver = self.driver
        step_user = PagePaidLessonComment(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_algebra_8_grade_questions()
        with allure.step("Нажать на кнопку Комментарии"):
            step_user.click_link_comments()
        with allure.step("Нажать на кнопку Отправить"):
            step_user.click_button_send()
        with allure.step("Поп-ап Авторизации появился"):
            self.assertEquals(u"Войдите в профиль",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_input_field_in_comment(self):
        driver = self.driver
        url_get = URLPaidLesson(driver)
        step_user = PagePaidLessonComment(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_algebra_8_grade_test()
        with allure.step("Нажать на кнопку Комментарии"):
            step_user.click_link_comments()
        with allure.step("Кликнуть мышкой в полле вода текста"):
            step_user.click_field_textarea()
        with allure.step("Поп-ап Авторизации появился"):
            self.assertEquals(u"Войдите в профиль",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)

    def test_click_button_comment_in_tab_comments(self):
        driver = self.driver
        url_get = URLPaidLesson(driver)
        step_user = PagePaidLessonComment(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_algebra_8_grade_test()
        with allure.step("Нажать на кнопку Комментарии"):
            step_user.click_link_comments()
        with allure.step("Нажать на кнопку Комментировать"):
            step_user.click_button_comment()
        with allure.step("Поп-ап Регистрации появился"):
            self.assertEquals(u"Зарегистрируйтесь",
                              self.driver.find_element_by_css_selector("h5.popup-header__title").text)
