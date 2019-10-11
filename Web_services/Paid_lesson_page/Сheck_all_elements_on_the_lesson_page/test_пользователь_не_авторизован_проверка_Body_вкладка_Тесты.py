import allure
from selenium.webdriver.common.by import By
from Web_services.URL import PaidLessonPage
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Страница урока Основные понятия (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов в Body во вкладке Тесты для не авторизованного пользователя")
class ChecksAllElementsInLessonPageTheBodyTabTestUserNotAuth(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 8 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = PaidLessonPage(StartInterneturokClassMethod)
        go_page.go_lesson_page_tab_test()

    @allure.step("На странице урока отображается название урока (Тригонометрические функции y = sin t, y = cos t)")
    def test_lesson_title(self):
        self.assertEqual("Тригонометрические функции y = sin t, y = cos t", self.driver.find_element_by_css_selector("h1.lesson-title").text)

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

    @allure.step("Во вкладке Тренажер отображается текст (Проверьте знания с помощью теста)")
    def test_title_text_test(self):
        self.assertEqual("Проверьте знания с помощью теста",
                         self.driver.find_element_by_css_selector("p.practices-desc").text)

    @allure.step("Во вкладке Тест отображается заглушка (Тренажеры доступны по абонементу)")
    def test_video_blocker(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.video-blocker"))
        with allure.step("В загулшке в левом углу отображается звезда (платный урок)"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.video-blocker__body-corner"))
        with allure.step("В заглушка присутствует текст (Тесты доступны по абонементу)"):
            self.assertEqual("Тесты доступны по абонементу",
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
        with allure.step("В заглушка отображается кнопка (Оплатить абонемент от 150 руб. в месяц)"):
            self.assertEqual("Оплатить абонемент\nот 150 руб. в месяц",
                             self.driver.find_element_by_css_selector("a.abonement__buy").text)

    @allure.step("Во вкладке Тесты отображается (Тест 1)")
    def test_button_trainers_one(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, ".practices-list > li:nth-child(1)"))
        with allure.step("В блоке тренажеров урока отображается текст (Тест 1)"):
            self.assertEqual("Тест 1", self.driver.find_element_by_css_selector(
                ".practices-list > li:nth-child(1) .practices-list__item-name").text)
        with allure.step("В блоке тренажеров урока отображается текст (Не пройден)"):
            self.assertEqual("Не пройден", self.driver.find_element_by_css_selector(
                ".practices-list > li:nth-child(1) .b-table-practices__result").text)
        with allure.step("В блоке тренажеров урока отображается кнопка (Пройти)"):
            self.assertEqual("Пройти", self.driver.find_element_by_css_selector(
                ".practices-list  > li:nth-child(1) > div.col-action > span > button").text)

    @allure.step("Во вкладке Тесты отображается (Тест 2)")
    def test_button_trainers_two(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, ".practices-list > li:nth-child(2)"))
        with allure.step("В блоке тренажеров урока отображается текст (Тест 2)"):
            self.assertEqual("Тест 2", self.driver.find_element_by_css_selector(
                ".practices-list > li:nth-child(2) .practices-list__item-name").text)
        with allure.step("В блоке тренажеров урока отображается текст (Не пройден)"):
            self.assertEqual("Не пройден", self.driver.find_element_by_css_selector(
                ".practices-list > li:nth-child(2) .b-table-practices__result").text)
        with allure.step("В блоке тренажеров урока отображается кнопка (Пройти)"):
            self.assertEqual("Пройти", self.driver.find_element_by_css_selector(
                ".practices-list  > li:nth-child(2) > div.col-action > span > button").text)

    @allure.step("В уроке в конце конспекта отображается ссылка (Информация об уроке)")
    def test_displayed_lesson_footer_button_info(self):
        self.assertEqual("Информация об уроке",
                         self.driver.find_element_by_id("info-link").text)
        with allure.step("В кнопке Информация об уроке присутствует иконка "):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.icon-lesson-info"))

    @allure.step("В уроке в конце конспекта отображается ссылка (Комментарии (11))")
    def test_displayed_lesson_footer_button_comment(self):
        self.assertEqual("Комментарии (11)",
                         self.driver.find_element_by_id("comments-link").text)
        with allure.step("В кнопке Комментарии (11) присутствует иконка "):
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
