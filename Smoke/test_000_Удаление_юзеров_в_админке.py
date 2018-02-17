import unittest
from POM.user import Admin
from POM.popup_authorization_and_registration import PopupSignIn
from POM.admin_delete_users import DeleteUser
from POM.setUp import StartInterneturokAdmin


class DeleteUsers(StartInterneturokAdmin):
    def test_delete(self):
        driver = self.driver
        steps_admin = Admin(driver)
        steps_login = PopupSignIn(driver)
        steps_delete = DeleteUser(driver)

        steps_admin.enter_email(user_name="admin")
        steps_admin.enter_password(password="qwedsazxc")

        steps_login.click_button_login_in_admin_panel()
        steps_delete.go_to_admin()

        steps_delete.user_1(pupil_1="vratch.glav@yandex.ru")
        steps_delete.user_2(pupil_2="paym.not@yandex.ru")
        steps_delete.user_3(pupil_3="payment.not@mail.ru")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
