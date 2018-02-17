from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

class test4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/biology/11-klass/evolyucionnoe-uchenie/teoriya-darvina/questions")
        driver.maximize_window()
        # driver.find_element_by_link_text(u"Вопросы к уроку").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.b-comment-answer__author"))
        driver.find_element_by_link_text(u"Комментировать").click()
        self.assertEqual(u"Зарегистрируйтесь", driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        driver.find_element_by_id("reg_user_email").click()
        driver.find_element_by_id("reg_user_email").clear()
        driver.find_element_by_id("reg_user_email").send_keys("xcz123l@mail.ru")
        driver.find_element_by_css_selector("#reg-form > div.dialog-form > div.dialog-form__control > #user_password").click()
        driver.find_element_by_css_selector("#reg-form > div.dialog-form > div.dialog-form__control > #user_password").clear()
        driver.find_element_by_css_selector("#reg-form > div.dialog-form > div.dialog-form__control > #user_password").send_keys("123456")
        driver.find_element_by_css_selector("#reg-form > div.modal-dialog__footer > input[name=\"commit\"]").click()
        time.sleep(1)
        self.assertFalse(self.is_element_present(By.CSS_SELECTOR, "#reg-form > div.dialog-form > div.dialog-form__control > div.dialog-form__control__warning"))
        self.assertEqual(u"Вопросы к уроку к теме Теория Дарвина по Биология 11 класс онлайн", driver.title)
        self.assertEqual(u"Проверить почту", driver.find_element_by_link_text(u"Проверить почту").text)
        driver.find_element_by_link_text(u"Комментировать").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//span[@id='async-questions']/dd/div/div[3]/div[4]/div[2]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e: return False
    #     return True
    
    # def is_alert_present(self):
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException as e: return False
    #     return True
    
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
