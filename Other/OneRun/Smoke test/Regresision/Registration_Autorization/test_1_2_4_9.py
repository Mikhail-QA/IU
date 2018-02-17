#Проверка Авторизации кнопка Войти
from selenium import webdriver
import unittest


class TheAccountSingIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"

    def test_the_account_sing_in(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"Войти").click()
        self.assertEqual(u"Войдите в профиль",
                         driver.find_element_by_css_selector("h4.modal-dialog__header__title").text)
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("hexcal@mail.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_name("commit").click()
        self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
