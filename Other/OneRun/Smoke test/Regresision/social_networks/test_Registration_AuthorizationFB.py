from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

# facebook.test.10@mail.ru

class Facebook(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verificationErrors = [False]

    def test_Reg_Auth(self):
        driver = self.driver
        driver.get ("https://www.facebook.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

        driver.find_element_by_id("email").send_keys("facebook.test.10@mail.ru")
        driver.find_element_by_id("pass").send_keys("test1991")
        driver.find_element_by_id("u_0_q").click()
        time.sleep(1)

        driver.get("https://web-dev01.interneturok.ru/")
        driver.delete_all_cookies()
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_link_text(u"Регистрация").click()
        driver.find_element_by_css_selector("a.b-omniauth__item_icon_fb").click()
        driver.save_screenshot('screen_FB.png')

        self.assertEqual(u"Регистрация", driver.find_element_by_css_selector("h3").text)
        self.assertEqual("Vlad Olysevich", driver.find_element_by_css_selector("p.b-oauth-user__name").text)
        self.assertEqual("facebook.test.10@mail.ru", driver.find_element_by_css_selector("p.b-oauth-user__email").text)
        self.assertEqual(u"Вы впервые на Home school или у вас уже есть аккаунт ?", driver.find_element_by_css_selector("p.center").text)
        self.assertEqual(u"Я новый пользователь", driver.find_element_by_link_text(u"Я новый пользователь").text)
        self.assertEqual(u"У меня уже есть аккаунт", driver.find_element_by_link_text(u"У меня уже есть аккаунт").text)
        driver.find_element_by_link_text(u"Я новый пользователь").click()
        self.assertEqual(
            u"Для завершения регистрации введите ваш e-mail. На указанный\nвами e-mail будет отправлено письмо с ссылкой для подтверждения.",
            driver.find_element_by_css_selector("p.center").text)
        self.assertEqual(u"Действующий e-mail", driver.find_element_by_css_selector("label").text)
        try:
            self.assertEqual("facebook.test.10@mail.ru", driver.find_element_by_id("user_email").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_name("commit").click()
        self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)
        self.assertEqual(u"Проверить почту", driver.find_element_by_link_text(u"Проверить почту").text)

# Test autorization
        driver.get("https://web-dev01.interneturok.ru/signout")
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_css_selector("a.b-omniauth__item_icon_fb").click()
        self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()
