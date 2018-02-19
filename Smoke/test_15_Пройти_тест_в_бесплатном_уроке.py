import time
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.user import PaymNotYandexRu
from POM.popup_authorization_and_registration import PopupSignIn
from POM.freetest import FreeTest


class PassTestInFreeLesson(StartInterneturok):
    def test_passed_in_free_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        user_steps = PaymNotYandexRu(driver)
        popup_steps = PopupSignIn(driver)
        steps_test = FreeTest(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()
        driver.get(
            "https://fast-staging.interneturok.ru/biology/7-klass/zhivotnye-ploskie-chervi/lentochnye-chervi/testcases")
        time.sleep(2)
        steps_test.go_test()
        steps_test.start_test()
        steps_test.click_button_finish()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()