from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest
import time

class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.get("https://web-dev01.interneturok.ru/school_landing")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()


    def test_not_clickable_button_load_hom(self):
        driver = self.driver
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_class_name("auth__form-group__input").send_keys("iuroki@yopmail.com")

        driver.find_element_by_css_selector(
        "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > div:nth-child(2) > input")\
        .send_keys("123456")

        driver.find_element_by_css_selector(
        "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > input").click()

        time.sleep(27)
        driver.get("https://web-dev01.interneturok.ru/school/lesson/10928/homework/40519")
        driver.find_element_by_xpath(
        "//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[3]/div[3]/homework-tab-footer/div/div/div[2]/div/div/button")\
        .click()

        self.assertEqual("Ваше решение",
        driver.find_element_by_css_selector("li.list-group-item.active > div.item__link--brd").text)

        self.assertTrue(self.is_element_present(By.CLASS_NAME, "disabled"))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

if __name__ == "__main__":
    unittest.main()