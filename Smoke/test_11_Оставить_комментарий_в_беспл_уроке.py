import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.page_free_lesson import PageFreeLessonComment
from POM.url_lesson import URLFreeLesson


@allure.feature("Комментарий")
@allure.story("Публикация комментария пользователем без абонемента в бесплатном уроке")
class SendCommentInFreeLesson(StartInterneturok):
    def test_user_write_comment_in_free_lesson(self):
        driver = self.driver
        steps_page = MainPage(driver)
        popup_steps = PopupSignIn(driver)
        user_steps = AutopaymentMailRu(driver)
        user = PageFreeLessonComment(driver)
        get_url = URLFreeLesson(driver)
        with allure.step("Нажать на кнопку Войти"):
            steps_page.go_to_sgnIn()
        with allure.step("Ввожу email/password"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок"):
            get_url.go_biology_11_grade()
        with allure.step("На странице урока нажать на кнопку Комментарии"):
            user.click_button_comments()
        with allure.step("Ввести текст в поле ввода Привет Yonga"):
            user.wtire_comment()
        with allure.step("Нажать на кнопку Отправить"):
            user.post_comment()
        with allure.step("Проверяю отображение опубликованного в списке комментария"):
            self.assertEquals(u"Привет Yonga", self.driver.find_element_by_xpath("//div/div[2]/p").text)
        with allure.step("Удалить опубликованный комментарий"):
            user.delete_comment()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
