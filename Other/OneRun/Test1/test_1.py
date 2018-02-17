from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1(self):
        driver = self.driver
        driver.get(
            "https://web-dev01.interneturok.ru/physics/8-klass/teplovye-yavleniya/vnutrennyaya-energiya?seconds=0&chapter_id=104")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Войти"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.video-blocker"))
        try:
            self.assertRegexpMatches(driver.find_element_by_css_selector(".video-blocker__blocker__text").text,
                                     r"Этот видеоурок доступен по абонементу")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertRegexpMatches(driver.find_element_by_css_selector(".video-blocker__blocker__text").text,
                                     r"Подробнее об абонементе, платных и бесплатных уроках")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertRegexpMatches(driver.find_element_by_css_selector(".video-blocker__blocker__text").text,
                                     r"У вас уже есть абонемент?")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertRegexpMatches(driver.find_element_by_css_selector(".video-blocker__blocker__text").text,
                                     r"Войти")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertRegexpMatches(driver.find_element_by_css_selector(".video-blocker__button").text,
                                     r"100 руб. в месяц")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.video-blocker__play"))

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
