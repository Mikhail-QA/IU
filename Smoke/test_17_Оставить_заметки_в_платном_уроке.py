import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
from POM.page_paid_lesson import Notes


class WriteNoteInPayLesson(StartInterneturok):
    def test_user_note_in_pay_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        user_steps = PaymNotYandexRu(driver)
        popup_steps = PopupSignIn(driver)
        notes_steps = Notes(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()
        self.driver.get(
            "https://fast-staging.interneturok.ru/physics/7-klass/rabota-moshnost-energija/energiya-zakon-sohraneniya-energii")

        notes_steps.open_notes()
        notes_steps.write_note()
        notes_steps.save_note()
        notes_steps.go_to_profile()
        self.assertIn("Hello", self.driver.find_element_by_css_selector("div.profile-content.show").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
