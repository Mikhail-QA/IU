import unittest
from POM.setUp import StartYandexMail
from selenium.common.exceptions import NoSuchElementException
from POM.data_mail import DataMail
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
from selenium.webdriver.common.by import By


class LoginAndConfirmTheMail(StartYandexMail):
    def test_confirm_the_mail(self):
        driver = self.driver
        steps_mail = DataMail(driver)
        steps_main = MainPage(driver)
        steps_user = PaymNotYandexRu(driver)
        steps_popup = PopupSignIn(driver)

        steps_mail.login_in_accaunt_user_Paymnotyandex_check_mail()
        steps_mail.open_mail_click_on_the_link_to_confirm_the_mail()

        steps_main.go_to_internetUrok()
        steps_main.go_to_sgnIn()

        steps_user.enter_email()
        steps_user.enter_password()
        steps_popup.click_button_login()
        self.assertEqual(u"Адрес электронной почты успешно подтвержден",
                         driver.find_element_by_css_selector("p.top-banner__text").text)
        self.assertFalse(self.is_element_present(By.CSS_SELECTOR, "div.top-banner__buttons"))

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
