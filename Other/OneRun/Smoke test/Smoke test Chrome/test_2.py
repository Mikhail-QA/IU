# looking MobilePay, step 1 and 2 form-block
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
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
        self.assertEqual(u"Оплата абонемента со счета мобильного телефона", driver.title)
        assert (driver.find_elements_by_class_name("mobilepay__form-block"))
        driver.implicitly_wait(30)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe").click())
        time.sleep(5)
        driver.switch_to_window("Оплата абонемента со счета мобильного телефона")
        # driver.send_keys(Keys.CONTROL+"w")
        driver.implicitly_wait(20)
        assert (driver.find_elements_by_class_name("mobilepay__form"))
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()