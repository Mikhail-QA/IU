#Проверка работы кнопки Закрыть
from selenium import webdriver
import unittest


class Test_1_2_4_8(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"

    def test_1248(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_xpath("//td/div/div/div/div/a").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
