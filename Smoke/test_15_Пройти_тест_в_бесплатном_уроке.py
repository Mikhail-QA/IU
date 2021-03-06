import allure
import unittest
import pytest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.user import PaymNotYandexRu
from POM.popup_authorization_and_registration import PopupSignIn
from POM.freetest import FreeTest
from POM.url_lesson import URLFreeLesson


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Тест")
@allure.story("Пройти Тест пользователем без абонементом в бесплатном уроке")
class PassTestInFreeLesson(StartInterneturok):
    def test_passed_in_free_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        user_steps = PaymNotYandexRu(driver)
        popup_steps = PopupSignIn(driver)
        steps_test = FreeTest(driver)
        get_url = URLFreeLesson(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email=paym.not@yandex.ru/password=123456"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок =Ленточные черви"):
            get_url.go_biology_7_grade_test()
        with allure.step("Нажать на кнопку Пройти"):
            steps_test.go_test()
        with allure.step("Отвечать на вопросы в тесте"):
            steps_test.start_test()
        with allure.step("В финальном поп-апе нажать на кнопку Завершить"):
            steps_test.click_button_finish()
        with allure.step("После пройденного Теста название кнопки Пройти поменялась на Повторить"):
            self.assertEquals(u"Повторить", self.driver.find_element_by_xpath("//li/div[2]/span/a").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
