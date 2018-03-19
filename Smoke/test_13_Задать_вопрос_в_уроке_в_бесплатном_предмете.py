import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.page_free_lesson import PageFreeLessonQuestion
from POM.cycles import Cycles
from POM.url_lesson import URLFreeLesson


@allure.feature("Вопрос к уроку")
@allure.story("Публикация вопроса пользователем без абонементом в бесплатном уроке")
class AskQuestionInFreeLesson(StartInterneturok):
    def test_user_ask_question_in_free_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = AutopaymentMailRu(driver)
        delete_steps = Cycles(driver)
        user = PageFreeLessonQuestion(driver)
        get_url = URLFreeLesson(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email/password"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок"):
            get_url.go_biology_11_grade_questions()
        with allure.step("Удалить существующие вопросы в списке"):
            delete_steps.delete_all_question()
        with allure.step("Ввести текст в поле ввода Привет Yonga"):
            user.ask_question()
        with allure.step("Нажать на кнопку Отправить"):
            user.post_question()
        with allure.step("Проверяю отображение опубликованного в списке Вопроса"):
            # assert (self.driver.find_element_by_css_selector("p.comment__text"))
            self.assertEquals(u"Привет Yonga", self.driver.find_element_by_css_selector("p.comment__text").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
