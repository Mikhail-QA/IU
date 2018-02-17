from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
class mobilePayFromBlock(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
    def test_mobilePay_from_block(self):
        driver = self.driver
        driver.get(self.base_url + "/users/sign_in")
        driver.maximize_window()
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("hexcal@mail.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_name("commit").click()
        driver.get("https://web-dev01.interneturok.ru/mobilepay")

        actions.click()