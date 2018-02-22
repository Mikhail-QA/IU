import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import PopupFeedback
from POM.data_mail import DataMail


@allure.feature("Оставить отзыв")
@allure.story("Пользовательм оставить отзыв и убедиться приходу отзыва на почту Менеджера ИУ")
class WriteReview(StartInterneturok):
    def test_the_review_came_the_mail(self):
        driver = self.driver
        steps_feedback = PopupFeedback(driver)
        steps_mail = DataMail(driver)
        with allure.step("Нажить на кнопку Оставить отзыв"):
            steps_feedback.open_popup()
        with allure.step("В поп-апе ввести имя"):
            steps_feedback.enter_name()
        with allure.step("В поп-апе ввести email"):
            steps_feedback.enter_email()
        with allure.step("В поп-апе ввести текст отзыва"):
            steps_feedback.enter_text()
        with allure.step("Нажать на кнопку Отправить"):
            steps_feedback.click_button_send()
        with allure.step("В поп-апе ""Спасибо за отзыв"" нажать на кнопку закрыть"):
            steps_feedback.click_in_button_name_close()
        with allure.step("Перейти на сайт Yandex-почты"):
            steps_mail.go_site_yandex()
        with allure.step("В почте Yandex авторизоваться Менеджером ИУ"):
            steps_mail.login_in_accaunt_user_testinterneturok_check_mail()
        with allure.step("В списке пришедних писем присутствует письмо от пользователя"):
            self.assertIn("背靠燕山",
                          driver.find_element_by_class_name("mail-MessageSnippet-Item_firstline").text)
        with allure.step("Удалить первое пиьсмо из списка в Yandex-почте"):
            steps_mail.delete_mail()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
