import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.setUp import StartInterneturok
from POM.user import AutopaymentMailRu


class User_no_abonement_check_plugs(StartInterneturok):
    def test_yes_plugs_in_free_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = AutopaymentMailRu(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()

        self.driver.get(
            "https://fast-staging.interneturok.ru/russian/9-klass/vvedenie/mezhdunarodnoe-znachenie-russkogo-yazyka")
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
