"""
1. Мета-теги / Title, Keywords, Description должны присутствовать и не должны быть пустыми + соответствовать страницы на которой находится П
Главная
Класс-Предмет
Страница урока
любая статичная страница. Например https://fast-staging.interneturok.ru/article/how-you-can-use-interneturok

"""

import allure
import time
from POM.setUp import StartInterneturokClassMethod


@allure.feature("Проверка title, description, keywords на разных страницах")
@allure.story("Перейти по страницам и сравнить title, description, keywords")
class CheckMetaTeg(StartInterneturokClassMethod):
    @allure.step("Проверка на Главной странице")
    def test_meta_teg_in_home_page(self):
        URL = "https://staging.interneturok.ru/"
        driver = self.driver
        with allure.step("Сверить url со ссылкой на которой находится П"):
            assert driver.current_url == URL
        with allure.step("Проверить соответсвия (title)"):
            assert driver.title == "Видеоуроки школьной программы, конспекты, тесты, тренажеры"
        with allure.step("Проверка соответствия (description)"):
            self.assertEqual(u"Видеоуроки школьной программы, конспекты, тесты, тренажеры",
                             driver.find_element_by_name("description").get_attribute('content'))
        with allure.step("Проверка соответствия (Keywords)"):
            self.assertEqual(
                u"видео уроки, видеоуроки, смотреть видео, дистанционное образование, конспекты уроков, электронный учебник, школа-экстернат, помощь в учёбе, удалённая школа",
                driver.find_element_by_name("keywords").get_attribute('content'))

    @allure.step("Проверка на странице урока")
    def test_meta_teg_in_page_lesson(self):
        driver = self.driver
        URL = "https://staging.interneturok.ru/lesson/physics/8-klass/teplovye-yavleniya/teplovoe-dvizhenie-temperatura"
        driver.get(URL)
        time.sleep(2)
        with allure.step("Сверить url со ссылкой на которой находится П"):
            assert driver.current_url == URL
        with allure.step("Проверить соответсвия Title"):
            assert driver.title == "Тепловое движение. Температура. Видеоурок. Физика 8 Класс"
        with allure.step("Проверка соответствия (description)"):
            self.assertEqual(u"Видеоурок: Тепловое движение. Температура по предмету Физика за 8 класс.",
                             driver.find_element_by_name("description").get_attribute('content'))
        with allure.step("Проверка соответствия (Keywords)"):
            self.assertEqual(
                u"Видеоурок Физика, видеоурок Физика 8 класс, Тепловое движение. Температура",
                driver.find_element_by_name("keywords").get_attribute('content'))

    @allure.step("Проверка на странице Предмет-Класс ")
    def test_meta_teg_in_page_subject_grades(self):
        URL = "https://staging.interneturok.ru/subject/literatura/class/8"
        driver = self.driver
        driver.get(URL)
        time.sleep(2)
        with allure.step("Сверить url со ссылкой на которой находится П"):
            assert driver.current_url == URL
        with allure.step("Проверить соответсвия Title"):
            assert driver.title == "Литература 8 класс"
        with allure.step("Проверка соответствия (description)"):
            self.assertEqual(
                u"Видеоуроки, тесты и тренажёры по Литература за 8 класс по школьной программе. Используйте конспект уроков раздела «Литература 8 класс» для закрепления полученных знаний.",
                driver.find_element_by_name("description").get_attribute('content'))
        with allure.step("Проверка соответствия (Keywords)"):
            self.assertEqual(u"Литература 8 класс",
                             driver.find_element_by_name("keywords").get_attribute('content'))

    @allure.step("Проверка на статичной странице")
    def test_meta_teg_in_static_page(self):
        URL = "https://staging.interneturok.ru/article/kak-ispolzovat-sayt-interneturok-ru-v-shkole"
        driver = self.driver
        driver.get(URL)
        time.sleep(2)
        with allure.step("Сверить url со ссылкой на которой находится П"):
            assert driver.current_url == URL
        with allure.step("Проверить соответсвия Title"):
            assert driver.title == "Как использовать сайт InternetUrok.ru в школе?"

        with allure.step("Проверка соответствия (description)"):
            self.assertEqual(u"Как использовать сайт InternetUrok.ru в школе?",
                             driver.find_element_by_name("description").get_attribute('content'))
        with allure.step("Проверка соответствия (Keywords)"):
            self.assertEqual(u"Как использовать сайт InternetUrok.ru в школе?",
                             driver.find_element_by_name("keywords").get_attribute('content'))
