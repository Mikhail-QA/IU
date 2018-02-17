import time
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.pageprofile import PageProfile
from POM.user import VratchGlavYandexRu


class Disable_autopayment(StartInterneturok):
    def test_off_autopayment(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = VratchGlavYandexRu(driver)
        profile_steps = PageProfile(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()

        profile_steps.go_to_my_profile()
        time.sleep(1)
        profile_steps.click_button_off_autopayment()
        time.sleep(1.5)
        profile_steps.click_in_popup1_off_autopayment()
        profile_steps.click_in_popup2_off_autopayment()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
