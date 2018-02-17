from selenium import webdriver
import unittest, time
#Заготовка 10 класс(учитель)

class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.get("https://web-dev01.interneturok.ru/school_landing")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_close_windows_push_button_no(self):
        driver = self.driver
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_class_name("auth__form-group__input") \
            .send_keys("asdkjcxzjkwq@mail.ru")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > div:nth-child(2) > input") \
            .send_keys("123456")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > input").click()
        time.sleep(27)
        driver.get("https://web-dev01.interneturok.ru/school/lesson/10098/homework/35432")
        driver.find_element_by_xpath(
            "//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[3]/div[3]/homework-tab-footer/div/div/div[2]/div/div/button").click()
        driver.find_element_by_id("upload-homework").send_keys("C:\\selenium\\freaa.png")
        driver.find_element_by_xpath(
            "//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[4]/div[2]/homework-tab-footer/div/div/div[2]/div/div/button").click()
        self.assertEqual(u"Вы уверены, что загрузили все файлы?",
                         driver.find_element_by_class_name("new-modal_header").text)
        driver.find_element_by_css_selector("div.new-modal_btn-wrap > button.btn.btn-silver").click()
        self.assertEqual(u"Отправить решение",
                         driver.find_element_by_css_selector("#lesson-content > div > div > div > div > div > div > div > div > div.fading.in > div.tab-footer.tab-footer__homework > homework-tab-footer > div > div > div:nth-child(2) > div > div > button").text)
        driver.refresh()
        self.assertEqual(u"Загрузить решение",
                         driver.find_element_by_css_selector("#lesson-content > div > div > div > div > div > div > div > div > div.fading.in > div.tab-footer.tab-footer__homework.ng-scope > homework-tab-footer > div > div > div:nth-child(2) > div > div > button").text)


if __name__ == "__main__":
    unittest.main()