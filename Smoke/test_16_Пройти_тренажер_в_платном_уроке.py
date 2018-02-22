import allure
import time
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
from POM.paid_exercise import Exercise


@allure.feature("Тренажер")
@allure.story("Пройти Тренажер пользователем с абонементом в платном уроке")
class PassSimulatorInPayLesson(StartInterneturok):
    def test_simulator_passed_in_pay_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        user_steps = PaymNotYandexRu(driver)
        popup_steps = PopupSignIn(driver)
        steps_exercise = Exercise(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email/password"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок"):
            self.driver.get(
                "https://fast-staging.interneturok.ru/physics/7-klass/vzaimodejstvie-tel/plotnost/trainers")
        with allure.step("Нажать на кнопку Пройти"):
            steps_exercise.go_exercise()
        with allure.step("Начать отвечать на ответы в Тренажере"):
            steps_exercise.test()
        with allure.step("Начать отвечать на ответы в Тренажере"):
            steps_exercise.click_button_finish()
        with allure.step("Пройденный Тренажёр помечается как Пройден"):
            assert self.driver.find_element_by_css_selector("span.result-mark.good")
        with allure.step("После пройденного Тренажёра название кнопки Пройти поменялась на Повторить"):
            assert (u"Повторить", self.driver.find_element_by_xpath("//li/div[2]/span/a").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
