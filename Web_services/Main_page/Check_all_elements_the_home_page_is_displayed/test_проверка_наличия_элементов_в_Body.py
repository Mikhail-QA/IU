"""
Проверить наличия элементов на главной странице в Body
URL: https://interneturok.ru/"
"""
import allure
from selenium.webdriver.common.by import By
from Web_services.app.SetUp import StartInterneturokClassMethod


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов и текста на главной страницы в элементе main.content.static")
class ChecksAllElementsThePageInBody(StartInterneturokClassMethod):
    with allure.step("В заголовке отображается текст (Уроки школьной программы)"):
        def test_text_home_title_displayed(self):
            self.assertEqual(u"Уроки школьной программы",
                             self.driver.find_element_by_css_selector("h1.home-title").text)
    with allure.step("В заголовке отображается текст (Видео, конспекты, тесты, тренажеры)"):
        def test_text_home_desc_displayed(self):
            self.assertEqual(u"Видео, конспекты, тесты, тренажеры",
                             self.driver.find_element_by_css_selector("p.home-title_small").text)
    with allure.step("На главной страницы отображается кнопка (Предметы)"):
        def test_button_subjects(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Предметы"))

    with allure.step("На главной страницы отображается кнопка (Классы)"):
        def test_button_grades(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Классы"))

    with allure.step("На главной страницы отображается полле ввода Поиск"):
        def test_field_search(self):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.home-search"))

    with allure.step("На главной страницы в элементе поиска отображается кнопка лупа (Поиск)"):
        def test_button_search(self):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.home-search__button"))

    with allure.step("На главной страницы отображается кнопка (Алгебра)"):
        def test_button_displayed_algebra(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Алгебра"))

    with allure.step("На главной страницы отображается кнопка (Геометрия)"):
        def test_button_displayed_geometry(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Геометрия"))

    with allure.step("На главной страницы отображается кнопка (Математика)"):
        def test_button_displayed_mathematics(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Математика"))

    with allure.step("На главной страницы отображается кнопка (Информатика)"):
        def test_button_displayed_computer_science(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Информатика"))

    with allure.step("На главной страницы отображается кнопка (Обществознание)"):
        def test_button_displayed_social_studies(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Обществознание"))

    with allure.step("На главной страницы отображается кнопка (ОБЖ)"):
        def test_button_displayed_health_basics(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"ОБЖ"))

    with allure.step("На главной страницы отображается кнопка (Физика)"):
        def test_button_displayed_physics(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Физика"))

    with allure.step("На главной страницы отображается кнопка (Химия)"):
        def test_button_displayed_chemistry(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Химия"))

    with allure.step("На главной страницы отображается кнопка (Биология)"):
        def test_button_displayed_biology(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Биология"))

    with allure.step("На главной страницы отображается кнопка (География)"):
        def test_button_displayed_geography(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"География"))

    with allure.step("На главной страницы отображается кнопка (Природоведение)"):
        def test_button_displayed_nature_study(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Природоведение"))

    with allure.step("На главной страницы отображается кнопка (Окружающий мир)"):
        def test_button_displayed_environmental_study(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Окружающий мир"))

    with allure.step("На главной страницы отображается кнопка (Русский язык)"):
        def test_button_displayed_russian(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Русский язык"))

    with allure.step("На главной страницы отображается кнопка (Литература)"):
        def test_button_displayed_literature(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Литература"))

    with allure.step("На главной страницы отображается кнопка (История России)"):
        def test_button_displayed_history_of_russia(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u""))

    with allure.step("На главной страницы отображается кнопка (Всеобщая история)"):
        def test_button_displayed_world_history(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Всеобщая история"))

    with allure.step("На главной страницы отображается кнопка (Английский язык)"):
        def test_button_displayed_england(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Английский язык"))

    with allure.step("На главной страницы отображается кнопка (Чтение)"):
        def test_button_displayed_reading(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Чтение"))

    with allure.step("На главной страницы отображается кнопка (Идеи и смыслы)"):
        def test_notification_displayed_ideas_and_meanings(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Идеи и смыслы"))

    with allure.step("На главной страницы отображается текст (Ученые — детям)"):
        def test_text_displayed_scientists_and_children(self):
            self.assertEqual(u"Ученые — детям",
                             self.driver.find_element_by_css_selector("h3.home-footer__title").text)

    with allure.step(
            "На главной страницы в блоке Ученые — детям отображается текст (Интересные лекции для школьников)"):
        def test_link_displayed_on_the_screen(self):
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Интересные лекции для школьников"))

    with allure.step("На главной страницы отображается текст (Родителям и учителям)"):
        def test_text_displayed_parents_and_teachers(self):
            self.assertEqual(u"Родителям и учителям",
                             self.driver.find_element_by_xpath("//div[2]/div/div[2]/div/div[2]/div/h3").text)

    with allure.step(
            "На главной страницы в блоке Родителям и учителям отображается текст (Полезные видеолекции: Детская психология, Здоровье ребёнка, Советы специалистов, Психология на Univertv.ru)"):
        def test_link_displayed_the_screen(self):
            self.assertEqual(
                u"Полезные видеолекции: Детская психология, Здоровье ребёнка, Советы специалистов, Психология на Univertv.ru",
                self.driver.find_element_by_css_selector(
                    "div.home-footer > div > div.home-footer__item.col-12.col-md-7 > div > div.col > div > p").text)

    with allure.step("На главной страницы отображается кнопка Оставить отзыв"):
        def test_button_review_displayed(self):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.review__close"))
