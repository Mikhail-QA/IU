from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class test_1_2_7_1(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1271(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("klobus@mail.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_name("commit").click()
        time.sleep(25)
        driver.find_element_by_css_selector(u".b-button-login").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"Личная информация").click()
        time.sleep(2)
        self.assertEqual(u"Личная информация", driver.find_element_by_css_selector("ul.left > li.current > a").text)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.setting-button"))
        self.assertTrue(self.is_element_present(By.ID, "profile_image"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.name-field"))
        self.assertEqual("klobus@mail.ru", driver.find_element_by_css_selector("span.option-field").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='edit_profile_form']/div[2]/div[2]/span"))
        self.assertEqual(u"Имя", driver.find_element_by_xpath("//form[@id='edit_profile_form']/div[2]/div[2]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='edit_profile_form']/div[2]/div[3]/span"))
        self.assertEqual(u"Возраст", driver.find_element_by_xpath("//form[@id='edit_profile_form']/div[2]/div[3]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='edit_profile_form']/div[2]/div[4]/span"))
        self.assertEqual(u"Страна", driver.find_element_by_xpath("//form[@id='edit_profile_form']/div[2]/div[4]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='edit_profile_form']/div[2]/div[5]/span"))
        self.assertEqual(u"Город", driver.find_element_by_xpath("//form[@id='edit_profile_form']/div[2]/div[5]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='edit_profile_form']/div[2]/div[6]/span"))
        self.assertEqual(u"Ученик",
                         driver.find_element_by_xpath("//form[@id='edit_profile_form']/div[2]/div[6]/span[2]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='edit_profile_form']/div[2]/div[7]/span"))
        self.assertEqual(u"Школа", driver.find_element_by_xpath("//form[@id='edit_profile_form']/div[2]/div[7]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='edit_profile_form']/div[2]/div[8]/span"))
        self.assertEqual(u"Родитель",
                         driver.find_element_by_xpath("//form[@id='edit_profile_form']/div[2]/div[8]").text)
        self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='edit_profile_form']/div[2]/div[9]/span"))
        self.assertEqual(u"Учитель", driver.find_element_by_xpath("//form[@id='edit_profile_form']/div[2]/div[9]").text)

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
