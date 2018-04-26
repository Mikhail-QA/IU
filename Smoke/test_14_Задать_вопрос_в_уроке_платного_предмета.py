import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.user import PaymNotYandexRu
from POM.popup_authorization_and_registration import PopupSignIn
from POM.page_paid_lesson import PagePaidLessonQuestion
from POM.cycles import Cycles
from POM.url_lesson import URLPaidLesson


@allure.feature("Вопрос к уроку")
@allure.story("Публикация вопроса пользователем с абонементом в платном уроке")
class AskQuestionInPayLesson(StartInterneturok):
    def test_user_ask_question_In_pay_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = PaymNotYandexRu(driver)
        user = PagePaidLessonQuestion(driver)
        get_url = URLPaidLesson(driver)
        delete_steps = Cycles(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email=paym.not@yandex.ru/password=123456"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок =Химические элементы. Символы химических элементов"):
            get_url.go_chemistry_8_grade_questions()
        with allure.step("Удалить существующие вопросы в списке"):
            delete_steps.delete_all_question()
        with allure.step("Ввести текст в поле ввода Привет Rich"):
            user.ask_question()
        with allure.step("Нажать на кнопку Отправить"):
            user.post_question()
        with allure.step("Проверяю отображение опубликованного в списке Вопроса"):
            # self.assertEqual(u"Привет Rich", self.driver.find_element_by_css_selector("p.comment__text").text)
            self.assertEquals(u"Привет Rich", self.driver.find_element_by_css_selector("p.comment__text").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
