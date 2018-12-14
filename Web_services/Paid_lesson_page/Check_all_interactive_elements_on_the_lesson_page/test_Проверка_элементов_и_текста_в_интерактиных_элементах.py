import time
import allure
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod
from Web_services.URL import PaidLessonPage
from POM.page_paid_lesson import Notes, LessonFooter, PagePaidLessonComment


@allure.feature("Страница урока Тригонометрические функции y = sin t, y = cos t (Алгебра 11 класс)")
@allure.story("Проверка наличия элементов и текста в интерактивных элементах ")
class ChecksAllInteractiveElementsOnLessonPage(StartInterneturokClassMethod):
    @allure.step("Проверка текста и элементов в открытой Заметки")
    def test_000_check_note(self):
        StartInterneturokClassMethod = self.driver
        get_page_lesson = PaidLessonPage(StartInterneturokClassMethod)
        open_notes = Notes(StartInterneturokClassMethod)

        get_page_lesson.go_lesson_page_tab_trainers()
        open_notes.open_notes()
        with allure.step("Отображается открытый блок Заметки"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.lesson-note-wrapper"))
        with allure.step("В полле вода текста отображается сообщение (Сохраняйте любой текст из...)"):
            self.assertEqual(
                "Сохраняйте любой текст из конспекта или записывайте собственные мысли и выводы прямо здесь.",
                self.driver.find_element_by_css_selector("textarea.lesson-note-widget__mobile-input").get_attribute(
                    "placeholder"))
        with allure.step("В заметки отображается кнопка Сохранить"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR,
                                                    "div.lesson-note-widget__mobile.lesson-note-widget__text.show > form > button"))

    @allure.step("Проверка текста и элементов в Информация об уроке")
    def test_001_check_info_lesson(self):
        StartInterneturokClassMethod = self.driver
        open_lesson_info = LessonFooter(StartInterneturokClassMethod)

        open_lesson_info.click_button_info_on_lesson()
        with allure.step("Отображается открытый блоке (Информация об уроке)"):
            self.assertTrue(self.is_element_present(By.ID, "info"))
        with allure.step("В блоке (Информация об уроке) отображается текст (Год съемки: 2011)"):
            self.assertEqual("Год съемки: 2011\nУчитель:  Тарасов Валентин Алексеевич",
                             self.driver.find_element_by_id("info").text)
        with allure.step("В открытом блоке отображается кнопка закрыть (Крестик)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#info > a"))

    @allure.step("Проверка текста и элементов в комментариях")
    def test_002_check_comments(self):
        StartInterneturokClassMethod = self.driver
        open_comment = PagePaidLessonComment(StartInterneturokClassMethod)

        time.sleep(0.5)
        open_comment.click_link_comments()
        with allure.step("Отображается открытый блок (Комментарии)"):
            self.assertTrue(self.is_element_present(By.ID, "comments"))
        with allure.step("В блоке (Комментарии) отображается текст (Комментарии к уроку)"):
            self.assertEqual("Комментарии к уроку",
                             self.driver.find_element_by_css_selector("span.comments__title").text)
        with allure.step("В открытом блоке отображается кнопка закрыть (Крестик)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#comments > a"))
        with allure.step("В блоке комментарии отображается комментарий"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.comment"))
        with allure.step("В списке комментариев отображается кнопка (Показать ещё комментарии)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.comment__more"))
        with allure.step("В конце списка комментариев отображается полле вода текста"):
            self.assertTrue(self.is_element_present(By.NAME, "text"))
        with allure.step("В конце списка комментариев отображается Кнопка (Отправить)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.comment__button"))
        self.driver.find_element_by_css_selector("#comments > a").click()

    @allure.step("Проверка текста и элементов в блоке Поделиться")
    def test_003_check_share(self):
        StartInterneturokClassMethod = self.driver
        open_tab_share = LessonFooter(StartInterneturokClassMethod)

        time.sleep(1)
        open_tab_share.click_button_share()
        time.sleep(1)
        with allure.step("Отображается открытый блок (Поделиться)"):
            self.assertTrue(self.is_element_present(By.ID, "share"))
        with allure.step("В открытом блоке отображается кнопка закрыть (Крестик)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#share > a"))

        with allure.step("В открытом блоке отображается иконка соцсети (ВК)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-social_vk"))
            with allure.step("В соцсети ВК отображается текст (Вконтакте)"):
                self.assertEqual("Вконтакте", self.driver.find_element_by_css_selector(
                    ".ember-view > div > a:nth-child(1) > span.lesson-tooltip__icon-text").text)
        with allure.step("В открытом блоке отображается иконка соцсети (Одноклассники)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-social_od"))
            with allure.step("В соцсети ОД отображается текст (Одноклассники)"):
                self.assertEqual("Одноклассники", self.driver.find_element_by_css_selector(
                    ".ember-view > div > a:nth-child(2) > span.lesson-tooltip__icon-text").text)
        with allure.step("В открытом блоке отображается иконка соцсети (Мой Мир)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-social_mm"))
            with allure.step("В соцсети Мой Мир отображается текст (Мой Мир)"):
                self.assertEqual("Мой Мир", self.driver.find_element_by_css_selector(
                    ".ember-view > div > a:nth-child(3) > span.lesson-tooltip__icon-text").text)
        with allure.step("В открытом блоке отображается иконка соцсети (Facebook)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-social_fb"))
            with allure.step("В соцсети Facebook отображается текст (Facebook)"):
                self.assertEqual("Facebook", self.driver.find_element_by_css_selector(
                    ".ember-view > div > a:nth-child(4) > span.lesson-tooltip__icon-text").text)
        with allure.step("В открытом блоке отображается иконка соцсети (Livejournal)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-social_lj"))
            with allure.step("В соцсети Livejournal отображается текст (Livejournal)"):
                self.assertEqual("Livejournal", self.driver.find_element_by_css_selector(
                    ".ember-view > div > a:nth-child(5) > span.lesson-tooltip__icon-text").text)
        with allure.step("В открытом блоке отображается иконка соцсети (Твиттер)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-social_tw"))
            with allure.step("В соцсети Твиттер отображается текст (Твиттер)"):
                self.assertEqual("Твиттер", self.driver.find_element_by_css_selector(
                    ".ember-view > div > a:nth-child(6) > span.lesson-tooltip__icon-text").text)
        with allure.step("В открытом блоке отображается текст и ссылка на урок (Ссылка на урок:)"):
            self.assertEqual("Ссылка на урок:", self.driver.find_element_by_css_selector(
                "#share > div:nth-child(3) > div.lesson-tooltip__frame-header > span").text)

        with allure.step("В открытом блоке отображается текст и ссылка на урок (Код для вставки на сайт:"):
            self.assertEqual(
                "Код для вставки на сайт:\nКопируя приведенный ниже HTML-код, вы тем самым принимаете Условия использования",
                self.driver.find_element_by_css_selector(
                    "#share > div:nth-child(4) > div.lesson-tooltip__frame-header").text)
