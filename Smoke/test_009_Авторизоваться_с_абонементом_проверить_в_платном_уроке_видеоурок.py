import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class User_with_abonement_check_no_plugs(StartInterneturok):
    def test_no_plugs_in_paid_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = PaymNotYandexRu(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()
        self.driver.get(
            "https://fast-staging.interneturok.ru/physics/11-klass/bmagnitnoe-poleb/magnitnoe-pole-ego-svoystva")
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
