import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class StartInterneturok(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.driver.get("https://fast-staging.interneturok.ru")
        time.sleep(2)
        self.verificationErrors = []


class StartYandexMail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.driver.get("https://mail.yandex.ru/")
        self.verificationErrors = []


class StartInterneturokAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.driver.get("https://staging-api.interneturok.ru/users/sign_in")
        self.verificationErrors = []


class StartInterneturokClassMethod(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        cls.driver.get("https://fast-staging.interneturok.ru/")
        time.sleep(2)
        cls.verificationErrors = []

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
