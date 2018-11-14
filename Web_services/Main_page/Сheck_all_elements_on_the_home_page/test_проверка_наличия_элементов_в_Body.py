"""
Проверить наличия элементов на главной странице в Body
URL: https://interneturok.ru/"
"""
import allure
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod


@allure.feature("Главная страница")
@allure.story("Проверка наличия элементов и текста на главной страницы в элементе main.content.static")
class ChecksAllElementsThePageInBody(StartInterneturokClassMethod):
    @allure.step("В заголовке отображается текст (Уроки школьной программы)")
    def test_text_home_title_displayed(self):
        self.assertEqual(u"Уроки школьной программы",
                         self.driver.find_element_by_css_selector("h1.home-title").text)

    @allure.step("В заголовке отображается текст (Видео, конспекты, тесты, тренажеры)")
    def test_text_home_desc_displayed(self):
        self.assertEqual(u"Видео, конспекты, тесты, тренажеры",
                         self.driver.find_element_by_css_selector("p.home-title_small").text)

    @allure.step("На главной страницы отображается кнопка (Предметы)")
    def test_button_subjects(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Предметы"))

    @allure.step("На главной страницы отображается кнопка (Классы)")
    def test_button_grades(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Классы"))

    @allure.step("На главной страницы отображается полле ввода Поиск")
    def test_field_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.home-search"))

    @allure.step("На главной страницы в элементе поиска отображается кнопка лупа (Поиск)")
    def test_button_search(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.home-search__button"))

    @allure.step("На главной страницы отображается кнопка (Алгебра)")
    def test_button_displayed_algebra(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Алгебра"))

    @allure.step("На главной страницы отображается кнопка (Геометрия)")
    def test_button_displayed_geometry(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Геометрия"))

    @allure.step("На главной страницы отображается кнопка (Математика)")
    def test_button_displayed_mathematics(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Математика"))

    @allure.step("На главной страницы отображается кнопка (Информатика)")
    def test_button_displayed_computer_science(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Информатика"))

    @allure.step("На главной страницы отображается кнопка (Обществознание)")
    def test_button_displayed_social_studies(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Обществознание"))

    @allure.step("На главной страницы отображается кнопка (ОБЖ)")
    def test_button_displayed_health_basics(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"ОБЖ"))

    @allure.step("На главной страницы отображается кнопка (Физика)")
    def test_button_displayed_physics(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Физика"))

    @allure.step("На главной страницы отображается кнопка (Химия)")
    def test_button_displayed_chemistry(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Химия"))

    @allure.step("На главной страницы отображается кнопка (Биология)")
    def test_button_displayed_biology(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Биология"))

    @allure.step("На главной страницы отображается кнопка (География)")
    def test_button_displayed_geography(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"География"))

    @allure.step("На главной страницы отображается кнопка (Природоведение)")
    def test_button_displayed_nature_study(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Природоведение"))

    @allure.step("На главной страницы отображается кнопка (Окружающий мир)")
    def test_button_displayed_environmental_study(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Окружающий мир"))

    @allure.step("На главной страницы отображается кнопка (Русский язык)")
    def test_button_displayed_russian(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Русский язык"))

    @allure.step("На главной страницы отображается кнопка (Литература)")
    def test_button_displayed_literature(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Литература"))

    @allure.step("На главной страницы отображается кнопка (История России)")
    def test_button_displayed_history_of_russia(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u""))

    @allure.step("На главной страницы отображается кнопка (Всеобщая история)")
    def test_button_displayed_world_history(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Всеобщая история"))

    @allure.step("На главной страницы отображается кнопка (Английский язык)")
    def test_button_displayed_england(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Английский язык"))

    @allure.step("На главной страницы отображается кнопка (Чтение)")
    def test_button_displayed_reading(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Чтение"))

    @allure.step("На главной страницы отображается кнопка (Школьная литература. Читаем вместе)")
    def test_button_displayed_idea_1(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Школьная литература. Читаем вместе"))

    @allure.step("На главной страницы отображается кнопка (Математика за 20 уроков)")
    def test_button_displayed_idea_2(self):
        self.assertEqual(u"Математика за 20 уроков",
                         self.driver.find_element_by_css_selector(
                             ".subjects__menu:nth-child(2) .subjects__col:nth-child(1) a:nth-child(2)").text)

    @allure.step("На главной страницы отображается кнопка (Основные понятия истории)")
    def test_button_displayed_idea_3(self):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Основные понятия истории"))

    @allure.step("На главной страницы отображается кнопка (Основы рационального поведения)")
    def test_button_displayed_idea_4(self):
        self.assertEqual(u"Основы рационального поведения",
                         self.driver.find_element_by_css_selector(
                             ".subjects__menu:nth-child(2) .subjects__col:nth-child(3) a:nth-child(1)").text)

    @allure.step("На главной страницы отображается кнопка (Обществознание. Разбираемся вместе)")
    def test_button_displayed_idea_5(self):
        self.assertEqual(u"Обществознание. Разбираемся вместе",
                         self.driver.find_element_by_css_selector(
                             ".subjects__menu:nth-child(2) .subjects__col:nth-child(2) a:nth-child(1)").text)

    @allure.step("На главной страницы отображается кнопка (Дискуссии и обсуждения)")
    def test_button_displayed_idea_6(self):
        self.assertEqual(u"Дискуссии и обсуждения",
                         self.driver.find_element_by_css_selector(
                             ".subjects__menu:nth-child(2) .subjects__col:nth-child(3) a:nth-child(2)").text)

    # @allure.step("На страницы отображается блок (Ученые — детям)")
    # def test_text_displayed_scientists_and_children(self):
    #     self.assertEqual(u"Ученые — детям",
    #                      self.driver.find_element_by_css_selector("h3.home-footer__title").text)
    #
    #     with allure.step("В блоке (Ученые — детям) раздел называется (Дополнительные видеоуроки:)"):
    #         self.assertEqual(u"Дополнительные видеоуроки:",
    #                          self.driver.find_element_by_xpath("//span[@class='home-footer__subtitle']").text)
    #     with allure.step("В блоке (Ученые — детям) отображается ссылка (Астрономия)"):
    #         self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Астрономия"))
    #     with allure.step("В блоке (Ученые — детям) отображается ссылка (Физика)"):
    #         self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Физика"))
    #     with allure.step("В блоке (Ученые — детям) отображается ссылка (Математика)"):
    #         self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Математика"))
    #
    # @allure.step("На страницы отображается блок (Родителям и учителям)")
    # def test_text_displayed_parents_and_teachers(self):
    #     self.assertEqual(u"Родителям и учителям",
    #                      self.driver.find_element_by_xpath("//div[2]/div/div[2]/div/h3").text)
    #     with allure.step("В блоке (Родителям и учителям) раздел называется (Полезные видеолекции:)"):
    #         self.assertEqual(u"Полезные видеолекции:",
    #                          self.driver.find_element_by_css_selector(
    #                              ".home-footer__item:nth-child(2) .home-footer__subtitle").text)
    #     with allure.step("В блоке (Родителям и учителям) отображается ссылка (Детская психология)"):
    #         self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Детская психология"))
    #     with allure.step("В блоке (Родителям и учителям) отображается ссылка (Здоровье ребенка)"):
    #         self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Здоровье ребенка"))
    #     with allure.step("В блоке (Родителям и учителям) отображается ссылка (Советы специалистов)"):
    #         self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Советы специалистов"))
    #     with allure.step("В блоке (Родителям и учителям) отображается ссылка (Психология на Univertv.ru)"):
    #         self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Психология на Univertv.ru"))

    @allure.step("На главной страницы отображается кнопка Оставить отзыв")
    def test_button_review_displayed(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.review__close"))
