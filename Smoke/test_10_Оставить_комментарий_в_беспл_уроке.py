import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.page_free_lesson import PageFreeLessonComment
from POM.cycles import Cycles


class Send_commnen_in_free_lesson(StartInterneturok):
    def test_user_write_comment(self):
        driver = self.driver
        steps_page = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = AutopaymentMailRu(driver)
        user = PageFreeLessonComment(driver)
        delete_steps = Cycles(driver)

        steps_page.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()
        self.driver.get(
            "https://staging.interneturok.ru/biology/11-klass/evolyucionnoe-uchenie/obzor-evolyutsionnyh-predstavleniy")

        user.click_button_comments()
        delete_steps.delete_old_comments()
        user.wtire_comment()
        user.post_comment()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
