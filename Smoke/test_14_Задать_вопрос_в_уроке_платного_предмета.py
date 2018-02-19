import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.user import PaymNotYandexRu
from POM.popup_authorization_and_registration import PopupSignIn
from POM.page_paid_lesson import PagePaidLessonQuestion
from POM.cycles import Cycles


class Ask_question_in_paid_lesson(StartInterneturok):
    def test_user_ask_question(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = PaymNotYandexRu(driver)
        user = PagePaidLessonQuestion(driver)
        delete_steps = Cycles(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()
        self.driver.get(
            "https://fast-staging.interneturok.ru/russian/9-klass/slozhnopodchinyonnye-predlozheniya/pravopisanie-predlozheniy-s-soyuzom-kak/questions")
        delete_steps.delete_all_question()

        user.ask_question()
        user.post_question()
        self.assertEqual(u"Привет Rich", self.driver.find_element_by_css_selector("p.comment__text").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
