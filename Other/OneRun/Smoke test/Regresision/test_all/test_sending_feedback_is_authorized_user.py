from selenium import webdriver
import unittest
import time

class SendingFeedbackIsNotAnAuthorizedUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"

    def test_sending_feedback_is_not_an_authorized_user(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("hexcal@mail.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_name("commit").click()
        time.sleep(20)
        driver.find_element_by_css_selector("span.b-button-review__trigger-form").click()
        self.assertEqual(u"ทดสอบนะจ๊ะ", driver.find_element_by_id("user_feedback_sender").get_attribute("value"))
        self.assertEqual("hexcal@mail.ru", driver.find_element_by_id("user_feedback_email").get_attribute("value"))
        driver.find_element_by_id("user_feedback_content").clear()
        driver.find_element_by_id("user_feedback_content").send_keys(u"Всё хорошо")
        driver.find_element_by_id("user_feedback_from").click()
        driver.find_element_by_id("user_feedback_from").clear()
        driver.find_element_by_id("user_feedback_from").send_keys("الظواهر الملحوظة")
        driver.find_element_by_name("commit").click()
        time.sleep(4)
        self.assertEqual(u"Сообщение", driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        driver.find_element_by_link_text(u"Закрыть").click()
        self.assertEqual(u"Видеоуроки школьной программы, конспекты, тесты, тренажеры", driver.title)
        # get yandex.ru
        driver.get("https://mail.yandex.ru/")
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector("#nb-1 > span > input").clear()
        driver.find_element_by_css_selector("#nb-1 > span > input").send_keys("test@interneturok.ru")
        driver.find_element_by_css_selector("#nb-2 > span > input").clear()
        driver.find_element_by_css_selector("#nb-2 > span > input").send_keys("xvmb-nfrb-q0sp")
        driver.find_element_by_css_selector("body > div.b-page.b-page_ru > div.new-left > div.new-auth.js-new-auth > form > div:nth-child(6) > span > button").click()
        time.sleep(4)
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text,
                                 r"^[\s\S]*الظواهر الملحوظة[\s\S]*$")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
