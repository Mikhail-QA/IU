import allure
import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage


@allure.feature("Поиск")
@allure.story("Произвести поиск по слову ty")
class CheckSearch(StartInterneturok):
    def test_search_shows_successfully(self):
        driver = self.driver
        steps_search = MainPage(driver)
        with allure.step("На главной странице в поле поиска ввести слово ty"):
            steps_search.enter_data()
        with allure.step("Нажить поиск"):
            steps_search.click_search()
        with allure.step("После загрузки результата в search-result__title отображается заголовок ""По запросу «ty» найдено 6 видеоуроков"" "):
            self.assertIn("По запросу «ty» найдено 6 видеоуроков",
                          driver.find_element_by_css_selector("div.search-result__wrap").text)
        with allure.step("Проверяю наличие 6-ти уроков на странице результат"):
            self.assertIn(
                "20:41\nКоличественные и порядковые числительные. Счет до 100"
                "\nЯгодник Людмила Николаевна\n09:45\nАффиксация. Суффиксы числительных"
                "\nЮлинецкая Юлия Васильевна\n19:42\nЧислительные\nКомарова Ирина Викторовна\n00:00"
                "\nXIX век в зеркале художественных исканий\n07:52\nВоздух - это смесь газов"
                "\nШарова Ирина Викторовна\n09:54\nМетеоры и метеориты\nКондратьева Светлана Владимировна",
                driver.find_element_by_css_selector("div.search-result__box").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
