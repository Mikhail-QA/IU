from selenium import webdriver
import unittest, time
# Заготовка 5 класс(учитель)
class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.get("https://web-dev01.interneturok.ru/school_landing")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_drag_and_drop_one_file(self):
        driver = self.driver
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_class_name("auth__form-group__input") \
            .send_keys("twotwo@mail.ru ")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > div:nth-child(2) > input") \
            .send_keys("123456")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > input").click()
        time.sleep(27)
        driver.get("https://web-dev01.interneturok.ru/school/lesson/7844/homework/40627")
        driver.find_element_by_xpath(
            "//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[3]/div[3]/homework-tab-footer/div/div/div[2]/div/div/button").click()
        self.assertEqual(u"Обзор", driver.find_element_by_xpath("//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[4]/div/div/button").text)
if __name__ == "__main__":
    unittest.main()