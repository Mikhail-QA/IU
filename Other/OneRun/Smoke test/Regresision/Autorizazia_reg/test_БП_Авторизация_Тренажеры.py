from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

class test8(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/informatika/9-klass/bmultimedijnaya-informaciya-vidy-kompyuternoj-grafikib/vvedenie-obrabotka-multimediynoy-informatsii?seconds=0&chapter_id=755")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Тренажеры").click()
        driver.find_element_by_link_text(u"Пройти").click()
        self.assertEqual(u"Войдите в профиль", driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("tets2017-04-20@mail.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_css_selector("div.modal-dialog__footer > input[name=\"commit\"]").click()
        self.assertEqual(u"Тренажеры к теме Введение. Обработка мультимедийной информации по Информатика 9 класс онлайн", driver.title)
        driver.find_element_by_xpath("//body[@id='lessonPage']/div[5]/table/tbody/tr/td/div/div/div/a").click()
        self.assertEqual(u"Тренажёр к уроку: Введение. Обработка мультимедийной информации",
                         driver.find_element_by_css_selector("#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__title-pane > div").text)
        driver.find_element_by_css_selector("a.b-button.arcticmodal-close-confirm").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
