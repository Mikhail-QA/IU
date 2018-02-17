#Проверка работы чекбокса Запомнить меня
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class Test_1_2_4_6(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1246(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Войти").click()
        self.assertEqual("", driver.find_element_by_css_selector("span.b-input-checkbox__fake").text)
        driver.find_element_by_css_selector("span.b-input-checkbox__fake").click()
        self.assertEqual("", driver.find_element_by_css_selector("span.b-input-checkbox__fake-mark").text)
        driver.find_element_by_css_selector("span.b-input-checkbox__fake-mark").click()

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
