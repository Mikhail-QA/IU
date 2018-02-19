import unittest
from POM.setUp import StartInterneturok
from POM.main_page import PopupFeedback
from POM.data_mail import DataMail


class WriteReview(StartInterneturok):
    def test_the_review_came_the_mail(self):
        driver = self.driver
        steps_feedback = PopupFeedback(driver)
        steps_mail = DataMail(driver)

        steps_feedback.open_popup()
        steps_feedback.enter_name()
        steps_feedback.enter_email()
        steps_feedback.enter_text()
        steps_feedback.click_button_send()
        steps_feedback.click_in_button_name_close()
        steps_mail.go_site_yandex()
        steps_mail.login_in_accaunt_user_testinterneturok_check_mail()
        self.assertIn("背靠燕山",
                      driver.find_element_by_class_name("mail-MessageSnippet-Item_firstline").text)
        steps_mail.delete_mail()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
