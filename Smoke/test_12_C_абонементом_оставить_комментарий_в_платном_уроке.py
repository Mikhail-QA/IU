import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
from POM.page_paid_lesson import PagePaidLessonComment


class SendCommentInPayLesson(StartInterneturok):
    def test_user_write_comment_in_pay_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        user_steps = PaymNotYandexRu(driver)
        popup_steps = PopupSignIn(driver)
        user = PagePaidLessonComment(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()
        self.driver.get(
            "https://fast-staging.interneturok.ru/algebra/11-klass/bzadachi-iz-egeb/urok-17-vopros-3-vypolnyayte-proverku-v-uravneniyah-i-neravenstvah")

        user.click_link_comments()
        user.write_comment()
        user.post_comment()
        user.delete_comment()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
