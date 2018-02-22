import allure
import time
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.user import PaymNotYandexRu
from POM.popup_authorization_and_registration import PopupSignIn
from POM.freetest import FreeTest


@allure.feature("Тест")
@allure.story("Пройти Тест пользователем без абонементом в бесплатном уроке")
class PassTestInFreeLesson(StartInterneturok):
    def test_passed_in_free_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        user_steps = PaymNotYandexRu(driver)
        popup_steps = PopupSignIn(driver)
        steps_test = FreeTest(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email/password"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок"):
            driver.get(
                "https://fast-staging.interneturok.ru/biology/7-klass/zhivotnye-ploskie-chervi/lentochnye-chervi/testcases")

        # time.sleep(2)
        with allure.step("Нажать на кнопку Пройти"):
            steps_test.go_test()
        with allure.step("Отвечать на вопросы в тесте"):
            steps_test.start_test()
        with allure.step("В финальном поп-апе нажать на кнопку Завершить"):
            steps_test.click_button_finish()
        with allure.step("После пройденного Теста название кнопки Пройти поменялась на Повторить"):
            assert (u"Повторить", self.driver.find_element_by_xpath("//li/div[2]/span/a").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
