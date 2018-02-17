from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class test_1_2_7_3(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1273(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("klobus@mail.ru")
        driver.find_element_by_id("user_password").click()
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_name("commit").click()
        time.sleep(24)
        driver.find_element_by_css_selector(u".b-button-login").click()
        driver.find_element_by_link_text(u"Личная информация").click()
        driver.find_element_by_link_text(u"Социальные профили").click()
        self.assertEqual(
            u"""С вашей учетной записью не связано ни одного профиля социальных сетей.
Связь с социальными профилями позволяет входить на сайт Home school в один клик по логотипу социальной сети, без указания логина и пароля""",
            driver.find_element_by_css_selector(".no-networks-text").text)
        self.assertEqual(u"Добавить профиль", driver.find_element_by_css_selector("p.network-connection-caption").text)
        self.assertTrue(
            self.is_element_present(By.XPATH, "//a[contains(@href, '/auth/interneturok?provider=facebook')]"))
        self.assertTrue(
            self.is_element_present(By.XPATH, "//a[contains(@href, '/auth/interneturok?provider=vkontakte')]"))
        self.assertTrue(self.is_element_present(By.XPATH, "//a[contains(@href, '/auth/interneturok?provider=yandex')]"))
        self.assertTrue(
            self.is_element_present(By.XPATH, "//a[contains(@href, '/auth/interneturok?provider=twitter')]"))
        self.assertTrue(
            self.is_element_present(By.XPATH, "//a[contains(@href, '/auth/interneturok?provider=odnoklassniki')]"))
        self.assertTrue(self.is_element_present(By.XPATH, "//a[contains(@href, '/auth/interneturok?provider=mailru')]"))
        self.assertTrue(
            self.is_element_present(By.XPATH, "//a[contains(@href, '/auth/interneturok?provider=google_oauth2')]"))
        self.assertEqual(
            u"""Эта страница предназначена для управления профилями социальных сетей,
связанными с вашей учетной записью на сайте Home school.""",
            driver.find_element_by_css_selector("p.social-networks-management-footer").text)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
