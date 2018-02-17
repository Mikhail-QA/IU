from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

# devocka.polo@mail.ru

class Mail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://mail.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Reg_Auth(self):
        driver = self.driver
        driver.get(self.base_url + "/?from=logout")
        driver.maximize_window()
        driver.find_element_by_id("mailbox__login").send_keys("devocka.polo@mail.ru")
        driver.find_element_by_id("mailbox__password").send_keys("Testng1991")
        driver.find_element_by_id("mailbox__auth__button").click()
        time.sleep(1)
        driver.get("https://web-dev01.interneturok.ru/")
        driver.delete_all_cookies()
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_link_text(u"Регистрация").click()
        driver.find_element_by_css_selector(".b-omniauth__item_icon_mm").click()
        # driver.find_element_by_id("accept").click()
        driver.save_screenshot('screen_Mail.png')
        self.assertEqual(u"Регистрация", driver.find_element_by_css_selector("h3").text)
        self.assertEqual("devocka polo", driver.find_element_by_css_selector("p.b-oauth-user__name").text)
        self.assertEqual("devocka.polo@mail.ru", driver.find_element_by_css_selector("p.b-oauth-user__email").text)
        self.assertEqual(u"Вы впервые на Home school или у вас уже есть аккаунт ?", driver.find_element_by_css_selector("p.center").text)
        self.assertEqual(u"Я новый пользователь", driver.find_element_by_link_text(u"Я новый пользователь").text)
        self.assertEqual(u"У меня уже есть аккаунт", driver.find_element_by_link_text(u"У меня уже есть аккаунт").text)
        driver.find_element_by_link_text(u"Я новый пользователь").click()
        self.assertEqual(
            u"Для завершения регистрации введите ваш e-mail. На указанный\nвами e-mail будет отправлено письмо с ссылкой для подтверждения.",
            driver.find_element_by_css_selector("p.center").text)
        self.assertEqual(u"Действующий e-mail", driver.find_element_by_css_selector("label").text)
        try:
            self.assertEqual("devocka.polo@mail.ru", driver.find_element_by_id("user_email").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_name("commit").click()
        self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)
        self.assertEqual(u"Проверить почту", driver.find_element_by_link_text(u"Проверить почту").text)

        driver.get("https://web-dev01.interneturok.ru/signout")
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_mm").click()
        self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
