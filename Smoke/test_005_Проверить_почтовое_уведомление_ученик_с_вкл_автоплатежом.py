import unittest
from POM.data_mail import DataMail
from POM.setUp import StartYandexMail


class CheckTheMailUserYesAutoPayment(StartYandexMail):
    def test_check_mail_notification(self):
        driver = self.driver
        main_steps = DataMail(driver)

        main_steps.login_in_accaunt_user_Vratchglavyandex_check_mail()
        self.assertIn("Уважаемый ученик! Ваш абонемент на сайте InternetUrok.ru активирован. Абонемент активен 31 день",
                      driver.find_element_by_css_selector("BODY").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
