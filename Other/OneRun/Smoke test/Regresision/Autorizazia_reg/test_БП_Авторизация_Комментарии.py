from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

class test6(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/biology/11-klass/evolyucionnoe-uchenie/razvitie-evolyutsionnyh-vzglyadov-v-dodarvinovskiy-period")
        driver.maximize_window()
        driver.find_element_by_id("comments-counter").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#new_comment > div.b-comment-form__actions > input[name=\"commit\"]").click()
        time.sleep(1)
        self.assertEqual(u"Войдите в профиль", driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        driver.find_element_by_xpath("//body[@id='lessonPage']/div[5]/table/tbody/tr/td/div/div/div/div/a").click()
        time.sleep(1)
        driver.find_element_by_id("comment_text").click()
        self.assertEqual(u"Войдите в профиль", driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        driver.find_element_by_id("user_email").click()
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("tets2017-04-20@mail.ru")
        driver.find_element_by_id("user_password").click()
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_css_selector("div.modal-dialog__footer > input[name=\"commit\"]").click()
        time.sleep(19)
        self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)
        self.assertEqual(u"Видеоурок: Развитие эволюционных взглядов в додарвиновский период по предмету биология за 11 класс.", driver.title)
    
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
