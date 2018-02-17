from selenium import webdriver
import unittest, time

class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.get("https://web-dev01.interneturok.ru/school_landing")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_open_file_after_sending(self):
        driver = self.driver
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_class_name("auth__form-group__input") \
            .send_keys("cohatwow@yopmail.com")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > div:nth-child(2) > input") \
            .send_keys("123456")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > input").click()
        time.sleep(27)
        driver.get("https://web-dev01.interneturok.ru/school/lesson/8066/homework/28086")
        driver.find_element_by_css_selector("img.img-responsive").click()
        self.assertEqual(u"Cохранить на диск",
                         driver.find_element_by_css_selector("body > div.modal.fade.ng-isolate-scope.iu-fade.in > div > div > div > div.modal-footer.clearfix.ng-scope > div.modal-footer_col.modal-footer_col__l > a").text)


if __name__ == "__main__":
    unittest.main()