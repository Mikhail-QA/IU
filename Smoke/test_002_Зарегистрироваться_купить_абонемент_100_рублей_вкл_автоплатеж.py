import unittest
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupRegistration
from POM.user import VratchGlavYandexRu
from POM.pageprofile import PageProfile
from POM.setUp import StartInterneturok


class CreateAccountAndBuyTicket100YesAutoPayment(StartInterneturok):
    def test_buy_ticket_per_100_rubles(self):
        driver = self.driver
        steps_main = MainPage(driver)
        steps_user = VratchGlavYandexRu(driver)
        steps_popup = PopupRegistration(driver)
        steps_in_profile = PageProfile(driver)

        steps_main.go_to_sgnIn()
        steps_popup.go_to_popup_registration()
        steps_user.reg_enter_email()
        steps_user.reg_enter_password()
        steps_popup.click_sign_up()
        steps_in_profile.go_to_my_profile()
        steps_in_profile.click_button_buy_subscription()
        steps_in_profile.popup_click_buy_subscription()
        steps_in_profile.enter_data_card()
        steps_in_profile.go_to_my_profile()
        driver.refresh()
        self.assertIn("Осталось:\n31 день\nАвтопродление:\n\nВкл.\nПодробнее об абонементе Продлить абонемент",
                      driver.find_element_by_class_name("profile-abonement__body").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
