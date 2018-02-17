# Проверка авторизации через паспорт https://dev01-passport.interneturok.ru/register
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class Test_1_2_4_0(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://dev01-passport.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1240(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.maximize_window()
        self.assertEqual(u"Вход - Home school", driver.title)
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("hexcal@mail.ru")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_name("commit").click()
        self.assertEqual(u"©  2010-2017 ООО «Интерда»", driver.find_element_by_css_selector("footer.footer > p").text)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Выход"))
        self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"Logo\"]").text)

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
