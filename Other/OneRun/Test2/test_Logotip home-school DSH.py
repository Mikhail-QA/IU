# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestLogotipHomeSchol(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_logotip_home_schol(self):
        driver = self.driver
        driver.get("https://web-dev01.interneturok.ru/")
        self.assertEqual(
            u"Видеоуроки по предметам школьной программы. Бесплатно и без рекламы. Уроки содержат тесты, тренажёры и конспекты",
            driver.title)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Home school: проверяем домашнее задание за 1 час"))
        driver.find_element_by_link_text(u"Home school: проверяем домашнее задание за 1 час").click()
        self.assertEqual(u"Home school Home school", driver.title)
        driver.back()
        self.assertEqual(u"Подготовка к ЕГЭ", driver.find_element_by_link_text(u"Подготовка к ЕГЭ").text)
        driver.find_element_by_link_text(u"Подготовка к ЕГЭ").click()
        self.assertEqual(u"Подготовка к ЕГЭ по математике и физике", driver.title)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
