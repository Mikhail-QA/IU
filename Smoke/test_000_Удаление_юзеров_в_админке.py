import allure
import unittest
from POM.user import Admin
from POM.popup_authorization_and_registration import PopupSignIn
from POM.admin_delete_users import AdminDeleteUser
from POM.setUp import StartInterneturokAdmin


@allure.feature("Админка")
@allure.story("Удаляю пользователей в админке")
class RemovingUsersInAdminPanel(StartInterneturokAdmin):
    def test_removing_a_users(self):
        driver = self.driver
        steps_admin = Admin(driver)
        steps_login = PopupSignIn(driver)
        steps_delete = AdminDeleteUser(driver)
        with allure.step("Авторизуюсь админом и переходу в раздел пользователи"):
            steps_admin.enter_email(user_name="admin")
            steps_admin.enter_password(password="qwedsazxc")
            steps_login.click_button_login_in_admin_panel()
            steps_delete.go_to_admin()

        with allure.step("Удаляю пользователя vratch.glav@yandex.ru"):
            steps_delete.user_1(pupil_1="vratch.glav@yandex.ru")

        with allure.step("Удаляю пользователя paym.not@yandex.ru"):
            steps_delete.user_2(pupil_2="paym.not@yandex.ru")

        with allure.step("Удаляю пользователя payment.not@mail.ru"):
            steps_delete.user_3(pupil_3="payment.not@mail.ru")
        with allure.step("Удаляю пользователя iuuser@yopmail.com"):
            steps_delete.user_4(pupil_4="iuuser@yopmail.com")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
