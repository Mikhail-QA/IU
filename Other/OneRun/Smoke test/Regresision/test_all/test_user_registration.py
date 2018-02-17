from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
class UserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(40)
        self.base_url = "https://web-dev01.interneturok.ru/"


    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Войти").click()
        time.sleep(1)
        driver.find_element_by_link_text("Регистрация").click()
        time.sleep(1)
        self.assertEqual(u"Зарегистрируйтесь",
                         driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        driver.find_element_by_id("reg_user_email").clear()
        driver.find_element_by_id("reg_user_email").send_keys("2i2g5228i2@mail.ru")
        driver.find_element_by_css_selector(
            "#reg-form > div.dialog-form > div.dialog-form__control > #user_password").clear()
        driver.find_element_by_css_selector(
            "#reg-form > div.dialog-form > div.dialog-form__control > #user_password").send_keys("123456")
        driver.find_element_by_css_selector("#reg-form > div.modal-dialog__footer > input[name=\"commit\"]").click()
        self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)
        self.assertEqual(u"Проверить почту", driver.find_element_by_link_text(u"Проверить почту").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
