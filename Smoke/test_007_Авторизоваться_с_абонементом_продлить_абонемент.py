import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.pageprofile import PageProfile
from POM.user import PaymNotYandexRu

class Extend_subscription(StartInterneturok):
    def test_user_extend_abonement(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = PaymNotYandexRu(driver)
        profile_steps = PageProfile(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()

        profile_steps.go_to_my_profile()
        profile_steps.click_extend_subscription()
        profile_steps.popup_click_buy_subscription()
        profile_steps.enter_data_card()
        profile_steps.go_to_my_profile()
        driver.refresh()
        self.assertIn("Осталось:\n62 дня\nАвтопродление:\n\nВкл.\nПодробнее об абонементе Продлить абонемент",
                     driver.find_element_by_class_name("profile-abonement__body").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
