import allure
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.setUp import StartInterneturok
from POM.user import AutopaymentMailRu
from POM.url_lesson import URLPaidLesson


@allure.feature("Платный видеоурок")
@allure.story("Авторизоваться без абонемента, проверить в платном уроке отображение заглушки видеоурока")
class CheckNoSubscriptionVideoInPayLesson(StartInterneturok):
    def test_yes_stub_in_pay_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = AutopaymentMailRu(driver)
        get_url = URLPaidLesson(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email=autopayment@mail.ru/password=123456"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок= Химические элементы. Символы химических элементов"):
            get_url.go_chemistry_8_grade_video()
        with allure.step("Проверить присутствие заглушки видеоурока"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.video-blocker"))

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
