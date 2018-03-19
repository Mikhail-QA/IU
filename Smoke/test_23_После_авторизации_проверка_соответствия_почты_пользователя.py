import unittest
import allure
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.setUp import StartInterneturok
from POM.user import AutopaymentMailRu
from POM.pageprofile import PageProfile


@allure.feature("Мой профиль")
@allure.story("После авторизации пользователь попадает в свою учётную запись")
class AuthAndCheckinMailUserToProfile(StartInterneturok):
    def test_user_auth_and_go_profile(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = AutopaymentMailRu(driver)
        get_url = PageProfile(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email/password"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти в ЛК во вкладку /edit"):
            get_url.go_to_my_profile_edit()
        with allure.step("В поле email отображается (почта-autopayment@mail.ru) зарегистрировшего пользователя"):
            self.assertEqual(u"autopayment@mail.ru",
                             self.driver.find_element_by_css_selector("input.profile-input").get_attribute("value"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
