import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class PageProfile(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_buy_subscription(self):
        self.driver.find_element_by_css_selector("a.profile-abonement__button").click()
        time.sleep(0.5)

    def click_extend_subscription(self):
        self.driver.find_element_by_css_selector("a.profile-abonement__button").click()

    def choose_subscription_365_day(self):
        self.driver.find_element_by_xpath("//div/div/div[3]/div/label[2]/span").click()
        time.sleep(0.5)

    def popup_click_buy_subscription(self):
        self.driver.find_element_by_class_name("abonement__buy").click()

    def popup_click_enable_autopayment(self):
        self.driver.find_element_by_xpath("//div/div[3]/div[2]/div/div[1]/div[1]/label").click()

    def popup_click_include_autopayment(self):
        self.driver.find_element_by_xpath("//div/div[3]/div[2]/div/div[1]/div[1]/label").click()

    def click_button_off_autopayment(self):
        self.driver.find_element_by_css_selector("a.link_green.link_dotted").click()
        time.sleep(1)

    def click_in_popup1_off_autopayment(self):
        self.driver.find_element_by_id("autopay_off").click()
        time.sleep(1)

    def click_in_popup2_off_autopayment(self):
        self.driver.find_element_by_class_name("button_blue").click()
        time.sleep(1)

    def enter_data_card(self):
        self.driver.find_element_by_id("cardNumber").send_keys("4444444444444448")
        self.driver.find_element_by_name("skr_month").send_keys("12")
        self.driver.find_element_by_name("skr_year").send_keys("20")
        self.driver.find_element_by_name("skr_cardCvc").send_keys("000")
        self.driver.find_element_by_class_name("payment-contract__pay-button").click()
        time.sleep(1.5)

    def go_to_my_profile(self):
        self.driver.get("https://staging.interneturok.ru/profile")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, 'span.profile-abonement__title')))

    def go_to_my_profile_edit(self):
        self.driver.get("https://staging.interneturok.ru/profile/edit")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, 'span.profile-abonement__title')))
