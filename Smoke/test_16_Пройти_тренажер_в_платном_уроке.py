import time
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
from POM.paid_exercise import Exercise


class PassSimulatorInPayLesson(StartInterneturok):
    def test_simulator_passed_in_pay_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        user_steps = PaymNotYandexRu(driver)
        popup_steps = PopupSignIn(driver)
        steps_exercise = Exercise(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()
        self.driver.get(
            "https://fast-staging.interneturok.ru/physics/7-klass/vzaimodejstvie-tel/plotnost/trainers")
        time.sleep(2)
        steps_exercise.go_exercise()
        steps_exercise.test()
        steps_exercise.click_button_finish()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
