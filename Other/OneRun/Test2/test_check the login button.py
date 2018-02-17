
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class button(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get("https://web-dev01.interneturok.ru/")
        driver.maximize_window()
        self.assertEqual(
            u"Видеоуроки школьной программы, конспекты, тесты, тренажеры",
            driver.title)
        driver.find_element_by_link_text(u"Войти").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "h4.modal-dialog__header__title"))
        try:
            self.assertEqual(u"Войти", driver.find_element_by_name("commit").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

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
    suite = unittest.TestLoader().loadTestsFromTestCase(button)
    unittest.TextTestRunner(verbosity=2)
