import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage
from POM.page_search import Search


@allure.feature("Поиск")
@allure.story("Произвести поиск по слову ty и перейти на урок Количественные и порядковые числительные. Счет до 100")
class CheckSearch(StartInterneturok):
    def test_search_shows_successfully(self):
        driver = self.driver
        steps_search = MainPage(driver)
        click_video = Search(driver)
        with allure.step("На главной странице в поле поиска ввести слово ty"):
            steps_search.enter_data()
        with allure.step("Нажить поиск"):
            steps_search.click_search()
        with allure.step(
                "После загрузки результата в search-result__title отображается заголовок ""По запросу «ty» найдено 7 видеоуроков"" "):
            self.assertIn("По запросу «ty» найдено 7 видеоуроков",
                          driver.find_element_by_css_selector("div.search-result__wrap").text)
        with allure.step("Проверяю наличие 7-ти уроков на странице результат"):
            self.assertIn(
                "20:41\nКоличественные и порядковые числительные. Счет до 100\nЯгодник Людмила Николаевна\n"
                "09:45\nАффиксация. Суффиксы числительных\nЮлинецкая Юлия Васильевна\n"
                "19:42\nЧислительные\nКомарова Ирина Викторовна\n"
                "39:20\nТема войны в литературе\nЛазарев Михаил Иванович,Ладохина Наталья Александровна\n"
                "00:00\nXIX век в зеркале художественных исканий\n"
                "07:52\nВоздух - это смесь газов\nШарова Ирина Викторовна\n"
                "09:54\nМетеоры и метеориты\nКондратьева Светлана Владимировна",
                driver.find_element_by_css_selector("div.search-result__box").text)
        with allure.step("Нажать на перво видео в списке поиска"):
            click_video.test_click_to_video()
        with allure.step(
                "После перехода? П отображается title-урока ""Количественные и порядковые числительные. Счет до 100"):
            self.assertEqual("Количественные и порядковые числительные. Счет до 100",
                             self.driver.find_element_by_css_selector("h1.lesson-title").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
