import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupRegistration
from POM.user import PaymNotYandexRu
from POM.pageprofile import PageProfile


class Registration_and_buy_a_subscription(StartInterneturok):
    def test_no_auto_payment(self):
        driver = self.driver
        steps_main_page = MainPage(driver)
        steps_popup = PopupRegistration(driver)
        steps_user = PaymNotYandexRu(driver)
        steps_in_profile = PageProfile(driver)

        steps_main_page.go_to_sgnIn()

        steps_popup.go_to_popup_registration()

        steps_user.reg_enter_email()
        steps_user.reg_enter_password()
        steps_popup.click_sign_up()

        steps_in_profile.go_to_my_profile()
        steps_in_profile.click_button_buy_subscription()
        steps_in_profile.popup_click_enable_autopayment()
        steps_in_profile.popup_click_buy_subscription()
        steps_in_profile.enter_data_card()
        steps_in_profile.go_to_my_profile()
        driver.refresh()
        self.assertIn("Осталось:\n31 день\nАвтопродление:\nВыкл.\nПодробнее об абонементе Продлить абонемент",
                      driver.find_element_by_class_name("profile-abonement__body").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
