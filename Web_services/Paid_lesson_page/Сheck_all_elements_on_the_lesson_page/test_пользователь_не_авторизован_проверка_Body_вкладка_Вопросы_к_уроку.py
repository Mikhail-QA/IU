import allure
from selenium.webdriver.common.by import By
from Web_services.URL import PaidLessonPage
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Страница урока Тригонометрические функции y = sin t, y = cos t (Алгебра 11 класс)")
@allure.story("Проверка наличия элементов в Body во вкладке Вопросы к уроку для не авторизованного пользователя")
class ChecksAllElementsInLessonPageTheBodyTabQuestionsUserNotAuth(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 11 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = PaidLessonPage(StartInterneturokClassMethod)
        go_page.go_lesson_page_tab_question()

    @allure.step("На странице урока отображается название урока (Тригонометрические функции y = sin t, y = cos t)")
    def test_lesson_title(self):
        self.assertEqual("Тригонометрические функции y = sin t, y = cos t",
                         self.driver.find_element_by_css_selector("h1.lesson-title").text)

    @allure.step("На странице урока отображается кнопка перейти на предыдущий урок (Кнопка влево)")
    def test_lesson_arrow_left(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.lesson-arrow_left"))

    @allure.step("На странице урока отображается кнопка перейти на следующий урок (Кнопка вправо)")
    def test_lesson_arrow_right(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.lesson-arrow_right"))

    @allure.step("На странице урока отображается Вкладки урока (Видеоурок, Текстовый урок и т.д)")
    def test_lesson_controls_body(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ul.lesson-controls__body"))

    @allure.step("На странице урока отображается вкладка (Видеоурок)")
    def test_button_video(self):
        self.assertEqual("Видеоурок", self.driver.find_element_by_css_selector("li.lc-video").text)
        with allure.step("Во вкладке Видеоурок отображается иконка"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.lesson-controls__icon_vid"))

    @allure.step("На странице урока отображается вкладка (Тестовый урок)")
    def test_button_text_lesson(self):
        self.assertEqual("Текстовый урок", self.driver.find_element_by_css_selector("li.lc-txt").text)
        with allure.step("Во вкладке Текстовый урок отображается иконка"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.lesson-controls__icon_vid"))

    @allure.step("На странице урока отображается вкладка (Тренажеры)")
    def test_button_training(self):
        self.assertEqual("Тренажеры", self.driver.find_element_by_css_selector(
            ".lesson-controls__body:nth-child(1) .lesson-controls__wrap:nth-child(3)").text)
        with allure.step("Во вкладке Тренажеры отображается иконка"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.lesson-controls__icon_training"))

    @allure.step("На странице урока отображается вкладка (Тесты)")
    def test_button_test(self):
        self.assertEqual("Тесты", self.driver.find_element_by_css_selector("li.lc-test").text)
        with allure.step("Во вкладке Тесты отображается иконка"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.lesson-controls__icon_test"))

    @allure.step("На странице урока отображается вкладка (Вопросы к уроку)")
    def test_button_questions(self):
        self.assertEqual("Вопросы к уроку", self.driver.find_element_by_css_selector("li.lc-questions").text)
        with allure.step("Во вкладке Вопросы к уроку отображается иконка"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.lesson-controls__icon_questions"))

    @allure.step("На странице урока отображается кнопка (Заметки)")
    def test_button_note(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.lesson-note-widget"))

    @allure.step("Во вкладке Вопросы к уроку отображается заглушка (Чтобы задать вопрос учителю, оплатите абонемент)")
    def test_video_blocker(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.video-blocker"))
        with allure.step("В загулшке в левом углу отображается звезда (платный урок)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.video-blocker__body-corner"))
        with allure.step("В заглушка присутствует текст (Чтобы задать вопрос учителю, оплатите абонемент)"):
            self.assertEqual("Чтобы задать вопрос учителю, оплатите абонемент",
                             self.driver.find_element_by_css_selector("h5.video-blocker__content_text-title").text)
        with allure.step("В заглушка присутствует ссылка (Подробнее об абонементе, платных и бесплатных уроках)"):
            self.assertEqual("Подробнее об абонементе, платных и бесплатных уроках",
                             self.driver.find_element_by_css_selector("a.video-blocker__content_text-link.link").text)
        with allure.step("В заглушка присутствует текст (У вас уже есть абонемент?)"):
            self.assertEqual("У вас уже есть абонемент? Войти",
                             self.driver.find_element_by_css_selector("p.has-abonement").text)
        with allure.step("В заглушка отображается ссылка (Войти)"):
            self.assertEqual("Войти",
                             self.driver.find_element_by_xpath("//div[2]/div/div[1]/p/a").text)
        with allure.step("В заглушка отображается кнопка (Оплатить абонемент от 75 руб. в месяц)"):
            self.assertEqual("Оплатить абонемент\nот 75 руб. в месяц",
                             self.driver.find_element_by_css_selector("a.abonement__buy").text)

    @allure.step("Во вкладке Вопросы к уроку отображается список вопросков от П (div.questions-wrapper)")
    def test_question_wrapper(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.questions-wrapper"))
        with allure.step("Во вкладке Вопросы к уроку отображается вопрос П в нём присутствует (аватарка П)"):
            self.assertEqual(
                "https://static-interneturok.cdnvideo.ru/avatar/big_9127a396759437995c897fd8abe816cf.png",
                self.driver.find_element_by_css_selector(
                    "img.comment__user-image").get_attribute("src"))
        with allure.step("Во списке вопросов у П под аватаркой отображается роль (Ученик)"):
            self.assertEqual("Ученик", self.driver.find_element_by_css_selector("div.comment__col").text)
        with allure.step("Во вопросе отображается имя П (ทดสอบนะจ๊ะ)"):
            self.assertEqual("ทดสอบนะจ๊ะ",
                             self.driver.find_element_by_css_selector("span.comment__username").text)
        with allure.step(
                "Во вопросе отображается текст вопроса (Потчему в примере 11 после сокращения Y оставшееся 2 - от 7 не +?)"):
            self.assertEqual(
                "помогите пожалуйста! я много смотрела видиоуроки, но их нет в статистике!! как можно их дабавить туда!",
                self.driver.find_element_by_css_selector("p.comment__text").text)
        with allure.step("Во вопросе отображается дата опубликования вопроса (21.09.2017)"):
            self.assertEqual("07.05.2018", self.driver.find_element_by_css_selector("span.comment__date").text)
        with allure.step("Во вопросе отображается кнопка (Комментировать)"):
            self.assertEqual("Комментировать", self.driver.find_element_by_css_selector("span.comment__action").text)

    @allure.step("Вопрос который прокомментировали более 3 раз отображается кнопка (Показть еще ответы)")
    def test_displayed_button_comment_more(self):
        self.assertEqual("Показать еще ответы", self.driver.find_element_by_css_selector(
            ".ember-view> div.comments-more.comment_subcomment > a").text)

    @allure.step("В конце списка вопросов отображается кнопка (Показть еще вопросы)")
    def test_displayed_button_comment_more_all(self):
        self.assertEqual("Показать еще вопросы", self.driver.find_element_by_css_selector(
            "div.questions-wrapper > div.comments-more > a").text)

    @allure.step("В уроке в конце конспекта отображается ссылка (Информация об уроке)")
    def test_displayed_lesson_footer_button_info(self):
        self.assertEqual("Информация об уроке",
                         self.driver.find_element_by_id("info-link").text)
        with allure.step("В кнопке Информация об уроке присутствует иконка "):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon-lesson-info"))

    @allure.step("В уроке в конце конспекта отображается ссылка (Комментарии (7))")
    def test_displayed_lesson_footer_button_comment(self):
        self.assertEqual("Комментарии (7)",
                         self.driver.find_element_by_id("comments-link").text)
        with allure.step("В кнопке Комментарии (7) присутствует иконка "):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon-lesson-comments"))

    @allure.step("В уроке в конце конспекта отображается ссылка (Поделиться)")
    def test_displayed_lesson_footer_button_share(self):
        self.assertEqual("Поделиться",
                         self.driver.find_element_by_id("share-link").text)
        with allure.step("В кнопке Поделиться присутствует иконка "):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon-lesson-share"))

    @allure.step("В уроке в конце конспекта отображается ссылка (В избранное)")
    def test_displayed_lesson_footer_button_lesson_add(self):
        self.assertEqual("В избранное",
                         self.driver.find_element_by_css_selector(
                             ".lesson-footer >div:nth-child(1) .ember-view:nth-child(4) > a.lesson-icons__group").text)
        with allure.step("В кнопке В избранное присутствует иконка "):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon-lesson-add"))

    @allure.step("В уроке в конце конспекта отображается ссылка (Нашли ошибку?)")
    def test_displayed_lesson_footer_button_lesson_report(self):
        self.assertEqual("Нашли ошибку?",
                         self.driver.find_element_by_css_selector("a.lesson-icons__group.ember-view").text)
        with allure.step("В кнопке Нашли ошибку? присутствует иконка "):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon-lesson-report"))

    @allure.step("В уроке в конце конспекта отображается текст  (Оценить урок:)")
    def test_displayed_lesson_footer_button_rating(self):
        self.assertEqual("Оценить урок:",
                         self.driver.find_element_by_css_selector("div.rating").text)
        with allure.step("В уроке в конце конспекта отображается звёзд для оценки урока (5 звезда)"):
            self.assertEqual("star5",
                             self.driver.find_element_by_css_selector(
                                 ".lesson-footer__row div >label:nth-child(3)").get_attribute("for"))
        with allure.step("В уроке в конце конспекта отображается звёзд для оценки урока (4 звезда)"):
            self.assertEqual("star4",
                             self.driver.find_element_by_css_selector(
                                 ".lesson-footer__row div >label:nth-child(5)").get_attribute("for"))
        with allure.step("В уроке в конце конспекта отображается звёзд для оценки урока (3 звезда)"):
            self.assertEqual("star3",
                             self.driver.find_element_by_css_selector(
                                 ".lesson-footer__row div >label:nth-child(7)").get_attribute("for"))
        with allure.step("В уроке в конце конспекта отображается звёзд для оценки урока (3 звезда)"):
            self.assertEqual("star3",
                             self.driver.find_element_by_css_selector(
                                 ".lesson-footer__row div >label:nth-child(7)").get_attribute("for"))

        with allure.step("В уроке в конце конспекта отображается звёзд для оценки урока (2 звезда)"):
            self.assertEqual("star2",
                             self.driver.find_element_by_css_selector(
                                 ".lesson-footer__row div >label:nth-child(9)").get_attribute("for"))

        with allure.step("В уроке в конце конспекта отображается звёзд для оценки урока (1 звезда)"):
            self.assertEqual("star1",
                             self.driver.find_element_by_css_selector(
                                 ".lesson-footer__row div >label:nth-child(11)").get_attribute("for"))

    @allure.step("В уроке в конце конспекта отображается блок оценки урока (Вконтакте:)")
    def test_displayed_lesson_footer_button_social_vk(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.social__vk"))
        with allure.step("В кнопке Вконтаке отображается кнопка Лайкнуть"):
            self.assertTrue(self.is_element_present(By.ID, "vk_like"))

    @allure.step("В уроке в конце конспекта отображается блок оценки урока (Facebook)")
    def test_displayed_lesson_footer_button_social_facebook(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.social__fb"))

    @allure.step("В уроке в конце конспекта отображается блок оценки урока (Одноклассники)")
    def test_displayed_lesson_footer_button_social_od(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.social__ok"))
