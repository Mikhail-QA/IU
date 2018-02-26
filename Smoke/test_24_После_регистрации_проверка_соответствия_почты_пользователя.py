import unittest
import allure
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupRegistration
from POM.setUp import StartInterneturok
from POM.user import IuUseryopmail
from POM.popup_authorization_and_registration import PopupSignIn


@allure.feature("Мой профиль")
@allure.story("После регистрации пользователь попадает в свою учётную запись")
class ReghAndCheckinMailUserToProfile(StartInterneturok):
    def test_user_reg_and_go_profile(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_auth = PopupSignIn(driver)
        popup_reg = PopupRegistration(driver)
        user_steps = IuUseryopmail(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Перейти в поп-ап Регистрации"):
            popup_auth.go_to_popup_registration()
        with allure.step("Ввожу email/password"):
            user_steps.reg_enter_email()
            user_steps.reg_enter_password()
        with allure.step("Нажать на кнопку Зарегистрироваться"):
            popup_reg.click_sign_up()
        with allure.step("Перейти в ЛК во вкладку /edit"):
            self.driver.get("https://fast-staging.interneturok.ru/profile/edit")
        with allure.step("В поле email отображается (почта-iuuser@yopmail.com) зарегистрировшего пользователя"):
            self.assertEqual(u"iuuser@yopmail.com",
                             self.driver.find_element_by_css_selector("input.profile-input").get_attribute("value"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
