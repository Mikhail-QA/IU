import unittest
from selenium.common.exceptions import NoSuchElementException
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
"""
Пример цикла авторизации и поиска слово "Привет" и если не находит нужно выйти из учетки
и опять авторизоваться и опять искать слово "Привет"
"""
class Extend_subscription(StartInterneturok):
    def test_user_extend_abonement(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = PaymNotYandexRu(driver)

        main_steps.go_to_sgnIn()

        user_steps.enter_email()
        user_steps.enter_password()
        popup_steps.click_button_login()

        for el in range(2):
            try:
                self.driver.find_element_by_link_text("Привет")
                print('Ok. Found on %s iteration' % el)
                break
            except NoSuchElementException:
                driver.get("https://web-dev01.interneturok.ru/signout")
                main_steps.go_to_sgnIn()

                user_steps.enter_email()
                user_steps.enter_password()
                popup_steps.click_button_login()
        raise NoSuchElementException
