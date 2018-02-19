import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.page_free_lesson import PageFreeLessonQuestion
from POM.cycles import Cycles


class Ask_question_in_free_lesson(StartInterneturok):
    def test_user_ask_question(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = AutopaymentMailRu(driver)
        delete_steps = Cycles(driver)
        user = PageFreeLessonQuestion(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()
        self.driver.get(
            "https://staging.interneturok.ru/biology/11-klass/evolyucionnoe-uchenie/razvitie-evolyutsionnyh-vzglyadov-v-dodarvinovskiy-period/questions")

        delete_steps.delete_all_question()

        user.ask_question()
        user.post_question()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
