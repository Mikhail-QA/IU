import unittest
import allure
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@allure.issue("https://jira.interneturok.ru/browse/IU-1457")
@allure.testcase(
    "https://docs.google.com/spreadsheets/d/1LlkQ5QLbi6kdjFQF3kgf8Xxd8R8zN041Pk19yKL3APc/edit#gid=941258384")
@allure.severity("blocker")
@allure.feature("Поп-ап оплаты")
@allure.story("Ввод суммы для конвертации, получение результата, проверка того, что использовалась    введенная нами сумма")
class TestPopup(unittest.TestCase):
    @allure.step("1: Запускаю драйвер")
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://web-dev01.interneturok.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_check_popup_registration(self):
        driver = self.driver
        with allure.step("2: Перейти на урок"):
            driver.get(
                "https://web-dev01.interneturok.ru/physics/8-klass/teplovye-yavleniya/vnutrennyaya-energiya?seconds=0&chapter_id=104")
        with allure.step("3: нажать на пноку Оплатить абонемент"):
            driver.find_element_by_css_selector("a.blocker__button").click()
        with allure.step("4: проверяю открылся ли поп-ап"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, ".modal-dialog__wrap"))
        with allure.step("5: Нажать на кнопку закрыть поп-ап"):
            driver.find_element_by_css_selector(".m-close").click()


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
