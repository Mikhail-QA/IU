import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminDeleteUser(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to_admin(self):
        self.driver.get("https://staging-admin.interneturok.ru/users")

    def user_1(self, pupil_1):
        self.driver.find_element_by_id("search_name").clear()
        self.driver.find_element_by_id("search_name").send_keys(pupil_1)
        self.driver.find_element_by_css_selector("input.btn").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("div.btn-group").click()
        time.sleep(1)
        self.driver.find_element_by_link_text(u"Удалить").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(6)

    def user_2(self, pupil_2):
        self.driver.find_element_by_id("search_name").clear()
        self.driver.find_element_by_id("search_name").send_keys(pupil_2)
        self.driver.find_element_by_css_selector("input.btn").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("div.btn-group").click()
        time.sleep(1)
        self.driver.find_element_by_link_text(u"Удалить").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(6)

    def user_3(self, pupil_3):
        self.driver.find_element_by_id("search_name").clear()
        self.driver.find_element_by_id("search_name").send_keys(pupil_3)
        self.driver.find_element_by_css_selector("input.btn").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("div.btn-group").click()
        time.sleep(1)
        self.driver.find_element_by_link_text(u"Удалить").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(6)

    def user_4(self, pupil_4):
        self.driver.find_element_by_id("search_name").clear()
        self.driver.find_element_by_id("search_name").send_keys(pupil_4)
        self.driver.find_element_by_css_selector("input.btn").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("div.btn-group").click()
        time.sleep(1)
        self.driver.find_element_by_link_text(u"Удалить").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(6)