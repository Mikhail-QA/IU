import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataMail(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def enter_data_users(self):
        self.driver.find_element_by_id("mailbox__login").send_keys("autopayment@mail.ru")
        self.driver.find_element_by_id("mailbox__password").send_keys("Testng1991")
        self.driver.find_element_by_id("mailbox__auth__button").click()

    def go_site_mail(self):
        self.driver.get("https://mail.ru")

    def go_site_yandex(self):
        self.driver.get("https://passport.yandex.ru/")

    def click_send(self):
        self.driver.find_element_by_css_selector("b-datalist__item__pic").click()

    def login_in_accaunt_user_Vratchglavyandex_check_mail(self):
        self.driver.find_element_by_css_selector("a.new-hr-auth-Form_Button-enter").click()
        self.driver.find_element_by_name("login").send_keys("vratch.glav@yandex.ru")
        self.driver.find_element_by_name("passwd").send_keys("Testng1991")
        self.driver.find_element_by_css_selector("button.passport-Button").click()
        time.sleep(4)

    def login_in_accaunt_user_Paymnotyandex_check_mail(self):
        self.driver.find_element_by_css_selector("a.new-hr-auth-Form_Button-enter").click()
        self.driver.find_element_by_name("login").send_keys("paym.not@yandex.ru")
        self.driver.find_element_by_name("passwd").send_keys("Testng1991")
        self.driver.find_element_by_css_selector("button.passport-Button").click()
        time.sleep(3)

    def login_in_accaunt_user_Vratchglavyandex_delete_all_mail(self):
        wait = WebDriverWait(self.driver, 30)
        self.driver.find_element_by_css_selector("a.new-hr-auth-Form_Button-enter").click()
        self.driver.find_element_by_name("login").send_keys("vratch.glav@yandex.ru")
        self.driver.find_element_by_name("passwd").send_keys("Testng1991")
        self.driver.find_element_by_css_selector("button.passport-Button").click()
        self.driver.find_element_by_css_selector("span.checkbox_view").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-toolbar-item-title-delete"))).click()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        time.sleep(2)

    def login_in_accaunt_user_Paymnotyandex_delete_all_mail(self):
        wait = WebDriverWait(self.driver, 30)
        self.driver.find_element_by_css_selector("a.new-hr-auth-Form_Button-enter").click()
        self.driver.find_element_by_css_selector("span.passport-Domik-Link").click()
        self.driver.find_element_by_name("login").send_keys("paym.not@yandex.ru")
        self.driver.find_element_by_name("passwd").send_keys("Testng1991")
        self.driver.find_element_by_css_selector("button.passport-Button").click()
        self.driver.find_element_by_css_selector("span.checkbox_view").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-toolbar-item-title-delete"))).click()
        time.sleep(0.5)

    def open_mail_click_on_the_link_to_confirm_the_mail(self):
        self.driver.find_element_by_css_selector(
            u"span[title=\"Инструкция по подтверждению адреса электронной почты\"]").click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector("a.daria-goto-anchor > font").click()
        time.sleep(0.5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)

    def login_in_accaunt_user_testinterneturok_check_mail(self):
        self.driver.find_element_by_name("login").send_keys("test@interneturok.ru")
        self.driver.find_element_by_name("passwd").send_keys("xvmb-nfrb-q0sp")
        self.driver.find_element_by_css_selector("button.passport-Button").click()
        time.sleep(3)
        self.driver.get("https://mail.yandex.ru/?uid=1130000006443638&login=test#inbox")

    def delete_mail(self):
        WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_css_selector(
            "span._nb-checkbox-flag._nb-checkbox-normal-flag")).click()
        WebDriverWait(self.driver, 15).until(
            lambda driver: driver.find_element_by_css_selector(".ns-view-toolbar-button-delete")).click()

        # self.driver.find_element_by_css_selector("span._nb-checkbox-flag._nb-checkbox-normal-flag").click()
        # self.driver.find_element_by_css_selector(".ns-view-toolbar-button-delete").click()
        # time.sleep(2)
