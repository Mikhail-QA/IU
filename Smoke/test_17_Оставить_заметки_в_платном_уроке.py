import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
from POM.page_paid_lesson import Notes
from POM.url_lesson import URLPaidLesson


@allure.feature("Заметка")
@allure.story("Оставить заметку пользователем с абонементом в платом уроке")
class WriteNoteInPayLesson(StartInterneturok):
    def test_user_note_in_pay_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        user_steps = PaymNotYandexRu(driver)
        popup_steps = PopupSignIn(driver)
        notes_steps = Notes(driver)
        get_url = URLPaidLesson(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email=paym.not@yandex.ru/password=123456"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок =Химические элементы. Символы химических элементов"):
            get_url.go_chemistry_8_grade_video()
        with allure.step("На странице урока нажать на виджет Заметка"):
            notes_steps.open_notes()
        with allure.step("В поле ввода ввести текст Hello"):
            notes_steps.write_note()
        with allure.step("Нажать на кнопку Сохранить"):
            notes_steps.save_note()
        with allure.step("Перейти в ЛК во вкладку Заметка"):
            notes_steps.go_to_profile()
        with allure.step("В ЛК отображается сохранённая Заметка"):
            self.assertEquals("Hello", self.driver.find_element_by_css_selector("p.profile-content__note").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
