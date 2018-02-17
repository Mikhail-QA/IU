import unittest
from POM.setUp import StartYandexMail
from POM.data_mail import DataMail


class Check_the_mail(StartYandexMail):
    def test_mail(self):
        driver = self.driver
        main_steps = DataMail(driver)

        main_steps.login_in_accaunt_user_Paymnotyandex_check_mail()
        self.assertIn("Уважаемый ученик! Ваш абонемент на сайте InternetUrok.ru активирован. Абонемент активен 31 день",
                      driver.find_element_by_css_selector("BODY").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
