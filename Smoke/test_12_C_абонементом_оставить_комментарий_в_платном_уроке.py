import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import PaymNotYandexRu
from POM.page_paid_lesson import PagePaidLessonComment


@allure.feature("Комментарий")
@allure.story("Публикация комментария пользователем с абонементом в платном уроке")
class SendCommentInPayLesson(StartInterneturok):
    def test_user_write_comment_in_pay_lesson(self):
        driver = self.driver
        main_steps = MainPage(driver)
        user_steps = PaymNotYandexRu(driver)
        popup_steps = PopupSignIn(driver)
        user = PagePaidLessonComment(driver)
        with allure.step("Нажать на кнопку Войти"):
            main_steps.go_to_sgnIn()
        with allure.step("Ввожу email/password"):
            user_steps.enter_email()
            user_steps.enter_password()
        with allure.step("Нажать на кнопку Авторизоваться"):
            popup_steps.click_button_login()
        with allure.step("Перейти на урок"):
            self.driver.get(
                "https://fast-staging.interneturok.ru/algebra/11-klass/bzadachi-iz-egeb/urok-17-vopros-3-vypolnyayte-proverku-v-uravneniyah-i-neravenstvah")
        with allure.step("На странице урока нажать на кнопку Комментарии"):
            user.click_link_comments()
        with allure.step("Ввести текст в поле ввода Привет Rich"):
            user.write_comment()
        with allure.step("Нажать на кнопку Отправить"):
            user.post_comment()
        with allure.step("Проверяю отображение опубликованного в списке комментария"):
            self.assertEquals(u"Привет Rich", self.driver.find_element_by_css_selector("p.comment__text").text)
        with allure.step("Удалить опубликованный комментарий"):
            user.delete_comment()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
