from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class test_1_2_7_2(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1272(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_link_text(u"Регистрация").click()
        time.sleep(1)
        driver.find_element_by_id("reg_user_email").clear()
        driver.find_element_by_id("reg_user_email").send_keys("turbo222@mail.ru")
        driver.find_element_by_css_selector(
            "#reg-form > div.dialog-form > div.dialog-form__control > #user_password").clear()
        driver.find_element_by_css_selector(
            "#reg-form > div.dialog-form > div.dialog-form__control > #user_password").send_keys("123456")
        driver.find_element_by_css_selector("#reg-form > div.modal-dialog__footer > input[name=\"commit\"]").click()
        time.sleep(17)
        driver.find_element_by_css_selector(u".b-button-login").click()
        driver.find_element_by_link_text(u"Личная информация").click()
        driver.find_element_by_css_selector("a.setting-button").click()
        driver.find_element_by_id("user_fullname").clear()
        driver.find_element_by_id("user_fullname").send_keys(u"Михаил")
        driver.find_element_by_id("user_birthday").click()
        driver.find_element_by_css_selector("select.ui-datepicker-year").send_keys("1991")
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_id("user_country").clear()
        driver.find_element_by_id("user_country").send_keys(u"Россия")
        driver.find_element_by_id("user_city").clear()
        driver.find_element_by_id("user_city").send_keys(u"СПБ")
        driver.find_element_by_id("user_school").clear()
        driver.find_element_by_id("user_school").send_keys(u"№31")
        driver.find_element_by_css_selector("a.setting-button.save").click()
        time.sleep(1)
        self.assertEqual("turbo222@mail.ru", driver.find_element_by_css_selector("span.option-field").text)
        self.assertEqual(u"Михаил", driver.find_element_by_xpath(
            "//form[@id='edit_profile_form']/div[2]/div[2]/span[2]/span").text)
        self.assertEqual("80", driver.find_element_by_xpath(
            "//form[@id='edit_profile_form']/div[2]/div[3]/span[2]/span").text)
        self.assertEqual(u"Россия", driver.find_element_by_xpath(
            "//form[@id='edit_profile_form']/div[2]/div[4]/span[2]/span").text)
        self.assertEqual(u"СПБ", driver.find_element_by_xpath(
            "//form[@id='edit_profile_form']/div[2]/div[5]/span[2]/span").text)
        self.assertEqual(u"Ученик",
                         driver.find_element_by_xpath("//form[@id='edit_profile_form']/div[2]/div[6]/span[2]").text)
        self.assertEqual(u"№31", driver.find_element_by_xpath(
            "//form[@id='edit_profile_form']/div[2]/div[7]/span[2]/span").text)

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
