from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time

class TestCheckButtonMyProfileForTheAuthenticatedUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_check_button_my_profile_for_the_authenticated_user(self):
        driver = self.driver
        driver.get("https://web-dev01.interneturok.ru/")
        driver.maximize_window()
        self.assertEqual(u"Войти", driver.find_element_by_link_text(u"Войти").text)
        driver.find_element_by_link_text(u"Войти").click()
        self.assertEqual("", driver.find_element_by_name("commit").text)
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("hexcal@mail.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("123456")
        driver.find_element_by_name("commit").click()
        time.sleep(20)
        try:
            self.assertEqual(u"Мой профиль", driver.find_element_by_link_text(u"Мой профиль").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        element_to_hover_over = driver.find_element_by_link_text("Мой профиль")
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()

        self.assertEqual(u"Личный кабинет", driver.find_element_by_link_text(u"Личный кабинет").text)
        driver.find_element_by_link_text(u"Личный кабинет").click()
        self.assertEqual(u"Личная информация", driver.find_element_by_link_text(u"Личная информация").text)
        driver.implicitly_wait(2)

        element_to_hover_over = driver.find_element_by_link_text("Мой профиль")
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()

        self.assertEqual(u"Обновления", driver.find_element_by_link_text(u"Обновления").text)
        driver.find_element_by_link_text(u"Обновления").click()
        self.assertEqual(u"Комментарии", driver.find_element_by_link_text(u"Комментарии").text)
        driver.implicitly_wait(2)

        element_to_hover_over = driver.find_element_by_link_text("Мой профиль")
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()

        self.assertEqual(u"Вопросы к уроку", driver.find_element_by_link_text(u"Вопросы к уроку").text)
        driver.find_element_by_link_text(u"Вопросы к уроку").click()
        self.assertEqual(u"Вопросы к уроку", driver.find_element_by_link_text(u"Вопросы к уроку").text)

        element_to_hover_over = driver.find_element_by_link_text("Мой профиль")
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()

        self.assertEqual(u"Выйти", driver.find_element_by_link_text(u"Выйти").text)
        driver.find_element_by_link_text(u"Выйти").click()
        self.assertEqual(u"Войти", driver.find_element_by_link_text(u"Войти").text)

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
