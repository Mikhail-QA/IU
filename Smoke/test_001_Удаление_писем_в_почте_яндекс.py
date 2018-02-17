import unittest
from POM.data_mail import DataMail
from POM.setUp import StartYandexMail

class Delete_mail_in_yandex(StartYandexMail):

    def test_delete(self):
        driver = self.driver
        steps_delete = DataMail(driver)

        steps_delete.login_in_accaunt_user_Vratchglavyandex_delete_all_mail()
        steps_delete.login_in_accaunt_user_Paymnotyandex_delete_all_mail()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
