from selenium import webdriver
import unittest, time
#Заготовка 10 класс(учитель)- Геометрия, 10 класс, 2016-2017. Урок "Кракен"

class Student(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
        self.driver.get("https://web-dev01.interneturok.ru/school_landing")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_the_deadline_is_limited(self):
        driver = self.driver
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_class_name("auth__form-group__input") \
            .send_keys("cohatwo@yopmail.com")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > div:nth-child(2) > input") \
            .send_keys("123456")
        driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(7) > input").click()
        time.sleep(27)
        driver.get("https://web-dev01.interneturok.ru/school/lesson/15889/homework/57169")
        self.assertEqual(u"Срок сдачи ДЗ: 16 июня 23:59 (МСК)",
                         driver.find_element_by_css_selector("strong.ng-binding.ng-scope").text)
        driver.find_element_by_xpath(
            "//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[3]/div[3]/homework-tab-footer/div/div/div[2]/div/div/button").click()
        driver.find_element_by_id("upload-homework").send_keys("C:\\selenium\\freaa.png")
        driver.find_element_by_xpath(
            "//div[@id='lesson-content']/div/div/div/div/div/div/div/div/div[4]/div[2]/homework-tab-footer/div/div/div[2]/div/div/button").click()
        self.assertEqual(u"Вы уверены, что загрузили все файлы?",
                         driver.find_element_by_class_name("new-modal_header").text)
        driver.find_element_by_css_selector("div.new-modal_btn-wrap > button.btn.btn-success").click()
        self.assertEqual(u"Ваше решение успешно отправлено и ожидает проверки учителем.",
                         driver.find_element_by_css_selector(
                             "div.fading.in > div.tab-footer.tab-footer__homework > homework-tab-footer > div.ng-scope > div.row.ng-scope > div.ng-scope > div.col-sm-9.col-md-9 > h3.homework-header_successfully > span").text)
        driver.refresh()
        # Проверяю загрузилась ли картинка
        assert driver.find_element_by_css_selector("img.img-responsive")

if __name__ == "__main__":
    unittest.main()
