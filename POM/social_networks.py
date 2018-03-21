import time


class SocialVk(object):
    def __init__(self, driver):
        self.driver = driver

    def auth_user_vk(self):
        self.driver.get("https://vk.com/")
        self.driver.find_element_by_id("index_email").send_keys("+79852635831")
        self.driver.find_element_by_id("index_pass").send_keys("Testng1991")
        self.driver.find_element_by_id("index_login_button").click()
        time.sleep(1)

    def click_button_new_user(self):
        self.driver.find_element_by_css_selector("body > div > div.actions > a:nth-child(1)").click()

    def click_button_reg(self):
        self.driver.find_element_by_name("commit").click()
        time.sleep(2)
