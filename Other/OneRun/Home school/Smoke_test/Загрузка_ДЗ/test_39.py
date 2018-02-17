from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest, time


class Teacher(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.get("https://web-dev01.interneturok.ru/school_landing")
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_teacher_load_one_file(self):
        driver = self.driver
        driver.find_element_by_link_text("Вход").click()
        time.sleep(1)
        driver.find_element_by_link_text("Зарегистрироваться").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]") \
            .send_keys("2221l51axp1@mail.ru")
        driver.find_element_by_xpath(
            "(//input[@type='password'])[2]") \
            .send_keys("123456")
        driver.find_element_by_css_selector("#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > input").click()
        time.sleep(29)
        driver.get("https://web-dev01.interneturok.ru/school/subjects-subscribe")
        driver.find_element_by_class_name("payment-summary_action").click()
        time.sleep(1)
        driver.find_element_by_id("bank-card").send_keys("4444444444444448")
        driver.find_element_by_name("skr_month").send_keys("12")
        driver.find_element_by_name("skr_year").send_keys("19")
        driver.find_element_by_name("skr_cardCvc").send_keys("000")
        driver.find_element_by_class_name("payment-contract__pay-button").click()
        time.sleep(5)
        self.assertEqual(u"Платеж успешно завершен", driver.find_element_by_class_name("title_last_yes").text)
        driver.find_element_by_css_selector("body > div.page-layout.page-layout_type_two-column.page-layout_page_payment-success.i-bem.page-layout_js_inited > div > div > div:nth-child(3) > div.island__section.clearfix > a").click()
        time.sleep(2)
        self.assertTrue(self.is_element_present(By.XPATH, "//welcome-school-notification/div/div"))
        driver.get("https://web-dev01.interneturok.ru/school/lesson/15890/homework/57170")

        driver.find_element_by_xpath(
            "//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[3]/div[3]/homework-tab-footer/div/div/div[2]/div/div/button").click()
        driver.find_element_by_id("upload-homework").send_keys("C:\\selenium\\freaa.png")
        time.sleep(0.1)

        driver.find_element_by_xpath(
            "//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[4]/div[2]/homework-tab-footer/div/div/div[2]/div/div/button").click()

        driver.find_element_by_css_selector("div.new-modal_btn-wrap > button.btn.btn-success").click()
        self.assertEqual(u"Ваше решение успешно отправлено и ожидает проверки учителем.",
                         driver.find_element_by_css_selector(
                             "div.fading.in > div.tab-footer.tab-footer__homework > homework-tab-footer > div.ng-scope > div.row.ng-scope > div.ng-scope > div.col-sm-9.col-md-9 > h3.homework-header_successfully > span").text)

        #Проверка ДЗ учителем
        driver.delete_all_cookies()
        driver.get("https://web-dev01.interneturok.ru/school_landing")
        time.sleep(2)
        driver.get("https://web-dev01.interneturok.ru/school_landing")
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_class_name("auth__form-group__input") \
            .send_keys("teacher-test")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > div:nth-child(2) > input") \
            .send_keys("teacher-test")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > input").click()
        time.sleep(1)
        driver.find_element_by_css_selector("input.form-control").send_keys("2221l1axp1@mail.ru")
        driver.find_element_by_link_text("Показать").click()
        driver.find_element_by_css_selector("li.list-group-item:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(7) > a:nth-child(2)").click()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True





if __name__ == "__main__":
    unittest.main()