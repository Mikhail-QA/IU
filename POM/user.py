# authorization user not abonement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutopaymentMailRu(object):
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, user_name="autopayment@mail.ru"):
        self.driver.find_element_by_xpath("//div/label[1]/input").send_keys(user_name)

    def enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//div/label[2]/input").send_keys(password)


# registration user buy subscription
class PaymentnotMailRu(object):
    def __init__(self, driver):
        self.driver = driver

    def reg_enter_email(self, user_name="payment.not@mail.ru"):
        self.driver.find_element_by_xpath("//div/label[1]/input").send_keys(user_name)

    def reg_enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//div/label[2]/input").send_keys(password)


# registration user with abonement
class PaymNotYandexRu(object):
    def __init__(self, driver):
        self.driver = driver

    def reg_enter_email(self, user_name="paym.not@yandex.ru"):
        self.driver.find_element_by_xpath("//div/label[1]/input").send_keys(user_name)

    def reg_enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//div/label[2]/input").send_keys(password)

    def enter_email(self, user_name="paym.not@yandex.ru"):
        self.driver.find_element_by_xpath("//div/label[1]/input").send_keys(user_name)

    def enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//div/label[2]/input").send_keys(password)


# registration user with abonement
class VratchGlavYandexRu(object):
    def __init__(self, driver):
        self.driver = driver

    def reg_enter_email(self, user_name="vratch.glav@yandex.ru"):
        self.driver.find_element_by_xpath("//div/label[1]/input").send_keys(user_name)

    def reg_enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//div/label[2]/input").send_keys(password)

    def enter_email(self, user_name="vratch.glav@yandex.ru"):
        self.driver.find_element_by_xpath("//div/label[1]/input").send_keys(user_name)

    def enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//div/label[2]/input").send_keys(password)


# authorization admin user
class Admin(object):
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, user_name):
        # wait = WebDriverWait(self.driver, 30)
        # wait.until(EC.element_to_be_clickable((By.ID, "user_email"))).send_keys(user_name)
        self.driver.find_element_by_name("user[email]").clear()
        self.driver.find_element_by_name("user[email]").send_keys("%s" % user_name)

    def enter_password(self, password):
        self.driver.find_element_by_id("user_password").clear()
        self.driver.find_element_by_id("user_password").send_keys("%s" % password)
