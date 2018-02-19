import allure
import unittest
from POM.data_mail import DataMail
from POM.setUp import StartYandexMail

@allure.feature("Почтовые уведомления")
@allure.story("Удаляю письма в почте пользоватлей")
class DeleteMailsInYandex(StartYandexMail):

    def test_removing_a_mails(self):
        driver = self.driver
        steps_delete = DataMail(driver)
        with allure.step("Удаляю письма у пользователя vratch.glav@yandex.ru"):
            steps_delete.login_in_accaunt_user_Vratchglavyandex_delete_all_mail()

        with allure.step("Удаляю письма у пользователя paym.not@yandex.ru"):
            steps_delete.login_in_accaunt_user_Paymnotyandex_delete_all_mail()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
