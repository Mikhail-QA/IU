from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class Test_1_2_7_0(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1270(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("hexcal@mail.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_name("commit").click()
        time.sleep(20)
        driver.find_element_by_css_selector(u"body > div.b-page__footer-down > div > header > div:nth-child(3) > div > div.b-menu-user > a").click()
        try:
            self.assertEqual(u"Видеоуроки школьной программы, конспекты, тесты, тренажеры", driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"Класcы", driver.find_element_by_css_selector("span.b-menu__title").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"Предметы", driver.find_element_by_xpath(
                "//body[@id='profileFavoritesPage']/div/div/header/div[2]/nav[2]/span").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertTrue(self.is_element_present(By.NAME, "q"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertTrue(self.is_element_present(By.ID, "flash-drive-widget"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)
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
    unittest.main()
