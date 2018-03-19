import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
from POM.url_lesson import URLPaidLesson
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@allure.feature("Платный Видеоурок")
@allure.story("Авторизоваться с абонементом, проверить в платном уроке отсутствия заглушки видеоурока")
class CheckWithSubscriptionVideoInPayLesson(StartInterneturok):
    def test_no_stub_in_pay_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = PaymNotYandexRu(driver)
        get_url = URLPaidLesson(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email/password"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок"):
            get_url.go_algebra_8_grade_video()
        with allure.step("Проверить отсуствия заглушки видеоурока"):
            self.assertFalse(self.is_element_present(By.CLASS_NAME, "video-blocker__body"))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
