import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class StartInterneturok(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.driver.get("https://staging.interneturok.ru")
        time.sleep(3)
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
        self.driver.get("https://staging-admin.interneturok.ru/accounts/sign_in")
        self.verificationErrors = []


class StartInterneturokAdminClassMethod(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        cls.driver.get("https://staging-admin.interneturok.ru/accounts/sign_in")
        cls.verificationErrors = []

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()


class StartInterneturokClassMethod(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        cls.driver.get("https://staging.interneturok.ru/")
        time.sleep(3)
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
