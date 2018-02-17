from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest, time
# заготовка 2 класс(учитель)

class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.get("https://web-dev01.interneturok.ru/school_landing")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_not_clickable_button_load_homework(self):
        driver = self.driver
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_class_name("auth__form-group__input")\
            .send_keys("coha@Mail.ru")
        driver.find_element_by_css_selector("#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > div:nth-child(2) > input")\
            .send_keys("123456")
        driver.find_element_by_css_selector("#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > input").click()
        time.sleep(27)
        driver.get("https://web-dev01.interneturok.ru/school/lesson/10928/homework/40519")
        driver.find_element_by_xpath("//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[3]/div[3]/homework-tab-footer/div/div/div[2]/div/div/button").click()
        time.sleep(2)
        driver.find_element_by_id("upload-homework").send_keys("C:\\selenium\\freaa.png")
        time.sleep(0.1)
        self.assertTrue(self.is_element_present(By.CLASS_NAME, "ng-scope"))
        driver.find_element_by_xpath("//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[4]/div[2]/homework-tab-footer/div/div/div[2]/div/div/button").click()
        self.assertEqual(u"Вы уверены, что загрузили все файлы?", driver.find_element_by_class_name("new-modal_header").text)
        driver.find_element_by_css_selector("div.new-modal_btn-wrap > button.btn.btn-success").click()
        self.assertEqual(u"Ваше решение успешно отправлено и ожидает проверки учителем.",
                         driver.find_element_by_css_selector("div.fading.in > div.tab-footer.tab-footer__homework > homework-tab-footer > div.ng-scope > div.row.ng-scope > div.ng-scope > div.col-sm-9.col-md-9 > h3.homework-header_successfully > span").text)
        driver.refresh()
        # Проверяю загрузилась ли картинка
        assert driver.find_element_by_css_selector("img.img-responsive")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

if __name__ == "__main__":
    unittest.main()