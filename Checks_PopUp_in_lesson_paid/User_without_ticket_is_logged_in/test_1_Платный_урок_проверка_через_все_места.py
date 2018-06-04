import allure
from POM.popup_authorization_and_registration import PopupSignIn
from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import PaidLesson, Notes, LessonFooter
from POM.url_lesson import URLPaidLesson
from POM.user import AutopaymentMailRu
from POM.main_page import MainPage
from POM.page_paid_lesson import PagePaidLessonQuestion
from POM.pageprofile import PageProfile


@allure.feature("Поп-апы для авторизованного пользователя без абонемента")
@allure.story("Авторизованный П проверить в платном уроке появления поп-апов во всех местах кроме заглушки")
class UserAuthCheckAppearancePopUpInAllPlaces(StartInterneturokClassMethod):

    def test_000_click_button_play_in_stub_video(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        get_url = URLPaidLesson(driver)
        data_user = AutopaymentMailRu(driver)
        open_popup = MainPage(driver)
        click_enter = PopupSignIn(driver)

        with allure.step("Нажать на кнопку Войти"):
            open_popup.go_to_sgnIn()
        with allure.step("В поп-апе авторизации ввести email/password"):
            data_user.enter_email()
            data_user.enter_password()
        with allure.step("В поп-апе авторизации Нажать на кнопку Войти"):
            click_enter.click_button_login()
        with allure.step("Перейти на страницу урока"):
            get_url.go_chemistry_8_grade_video()
        with allure.step("В превью видеоурока нажать на кнопку Плей"):
            step_user.click_button_play_video()
        with allure.step("Поп-ап Оплаты появился"):
            assert (self.driver.find_element_by_css_selector("div.popup.popup-payment"))

    def test_click_button_comment_in_tab_ask_question(self):
        driver = self.driver
        step_user = PagePaidLessonQuestion(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока во вкладку Вопросы к уроку"):
            url_get.go_chemistry_8_grade_questions()
        with allure.step("Нажать на кнопку Комментировать"):
            step_user.click_button_comment()
        with allure.step("Часть большого поп-ап Отображается popup-payment__price"):
            assert (self.driver.find_element_by_css_selector("div.popup-payment__price"))
        with allure.step("Часть большого поп-ап Отображается popup__text_intro"):
            self.assertIn(u"По абонементу доступны:",
                          driver.find_element_by_xpath("//div/div[2]/h3[1]").text)

    def test_click_button_save_in_note(self):
        driver = self.driver
        step_user = Notes(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_algebra_8_grade_test()
        with allure.step("Нажать на кнопку Заметки"):
            step_user.open_notes()
        with allure.step("Нажать на кнопку Сохранить"):
            step_user.save_note()
        with allure.step("Часть большого поп-ап Отображается popup-payment__price"):
            assert (self.driver.find_element_by_css_selector("div.popup-payment__price"))
        with allure.step("Часть большого поп-ап Отображается popup__text_intro"):
            self.assertIn(u"По абонементу доступны:",
                          driver.find_element_by_xpath("//div/div[2]/h3[1]").text)

    def test_click_input_field_in_note(self):
        driver = self.driver
        step_user = Notes(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_algebra_8_grade_test()
        with allure.step("Нажать на кнопку Заметки"):
            step_user.open_notes()
        with allure.step("Кликнуть мышкой в поле ввода текста"):
            step_user.click_textarea()
        with allure.step("Часть большого поп-ап Отображается popup-payment__price"):
            assert (self.driver.find_element_by_css_selector("div.popup-payment__price"))
        with allure.step("Часть большого поп-ап Отображается popup__text_intro"):
            self.assertIn(u"По абонементу доступны:",
                          driver.find_element_by_xpath("//div/div[2]/h3[1]").text)

    def test_click_button_favourites(self):
        driver = self.driver
        step_user = LessonFooter(driver)
        url_get = URLPaidLesson(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_physics_7_grade_trainers()
        with allure.step("В подвале сайта нажать на кнопку В Избранное"):
            step_user.click_button_favourites()
        with allure.step("Часть большого поп-ап Отображается popup-payment__price"):
            assert (self.driver.find_element_by_css_selector("div.popup-payment__price"))
        with allure.step("Часть большого поп-ап Отображается popup__text_intro"):
            self.assertIn(u"По абонементу доступны:",
                          driver.find_element_by_xpath("//div/div[2]/h3[1]").text)

    def test_click_button_pay_ticket(self):
        driver = self.driver
        url_get = PageProfile(driver)

        with allure.step("Перейти на страницу урока"):
            url_get.go_to_my_profile()
        with allure.step("В ЛК в виджете Абонемент нажать на кнопку (Оплатить абонемент)"):
            url_get.click_button_buy_subscription()
        with allure.step("Часть большого поп-ап Отображается popup-payment__price"):
            assert (self.driver.find_element_by_css_selector("div.popup-payment__price"))
        with allure.step("Часть большого поп-ап Отображается popup__text_intro"):
            self.assertIn(u"По абонементу доступны:",
                          driver.find_element_by_xpath("//div/div[2]/h3[1]").text)
