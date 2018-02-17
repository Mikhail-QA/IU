from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/chemistry/10-klass/bvvedenieb/predmet-organicheskoy-himii-rol-organicheskih-veschestv-v-zhizni-cheloveka?seconds=0&chapter_id=184")
        driver.maximize_window()
        driver.find_element_by_css_selector("#bookmark-lesson-link").click()
        self.assertEqual(u"Войдите в профиль",
                         driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("hexcal@mail.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_css_selector("div.modal-dialog__footer > input[name=\"commit\"]").click()
        self.assertFalse(self.is_element_present(By.CSS_SELECTOR, "div.popup__body-item"))
        self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)
        driver.find_element_by_css_selector("#bookmark-lesson-link").click()
        self.assertEqual(u"Сообщение", driver.find_element_by_class_name("modal-dialog__header__title").text)
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