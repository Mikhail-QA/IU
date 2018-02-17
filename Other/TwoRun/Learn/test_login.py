import unittest
from selenium import webdriver
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu


class auth_popup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://web-dev01.interneturok.ru/users/sign_in?tab=authTab")

    def test_validate_data(self):
        driver = self.driver
        session = PaymNotYandexRu(driver)
        popup = PopupSignIn(driver)
        driver.execute_script("window.open()")
        session.enter_email()
        session.enter_password()
        popup.click_button_login()
        driver.get_cookies()
        self.assertTrue(driver.find_element_by_link_text("Мой профиль"))
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
