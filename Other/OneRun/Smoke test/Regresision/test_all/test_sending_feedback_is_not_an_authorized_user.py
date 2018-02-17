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
        self.assertEqual(u"Войти", driver.find_element_by_link_text(u"Войти").text)
        driver.find_element_by_css_selector("span.b-button-review__trigger-form").click()
        self.assertEqual(u"Спасибо, что решили написать!",
                         driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        self.assertEqual("", driver.find_element_by_id("user_feedback_sender").get_attribute("value"))
        self.assertEqual("", driver.find_element_by_id("user_feedback_email").get_attribute("value"))
        self.assertEqual("", driver.find_element_by_id("user_feedback_content").get_attribute("value"))
        self.assertEqual("", driver.find_element_by_id("user_feedback_from").get_attribute("value"))
        driver.find_element_by_id("user_feedback_sender").clear()
        driver.find_element_by_id("user_feedback_sender").send_keys(u"Миша")
        driver.find_element_by_id("user_feedback_email").clear()
        driver.find_element_by_id("user_feedback_email").send_keys("Hexcal@mail.ru")
        driver.find_element_by_id("user_feedback_content").clear()
        driver.find_element_by_id("user_feedback_content").send_keys(u"Всё хорошо")
        driver.find_element_by_id("user_feedback_from").clear()
        driver.find_element_by_id("user_feedback_from").send_keys(u"背靠燕山")
        driver.find_element_by_name("commit").click()
        time.sleep(3)
        self.assertEqual(u"Сообщение", driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        self.assertEqual(u"Закрыть", driver.find_element_by_link_text(u"Закрыть").text)
        driver.find_element_by_link_text(u"Закрыть").click()
        self.assertEqual(u"Видеоуроки школьной программы, конспекты, тесты, тренажеры", driver.title)
        driver.get("https://mail.yandex.ru/")
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector("#nb-1 > span > input").clear()
        driver.find_element_by_css_selector("#nb-1 > span > input").send_keys("test@interneturok.ru")
        driver.find_element_by_css_selector("#nb-2 > span > input").clear()
        driver.find_element_by_css_selector("#nb-2 > span > input").send_keys("xvmb-nfrb-q0sp")
        driver.find_element_by_css_selector("body > div.b-page.b-page_ru > div.new-left > div.new-auth.js-new-auth > form > div:nth-child(6) > span > button").click()
        time.sleep(4)
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text,
                                 r"^[\s\S]*背靠燕山[\s\S]*$")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
