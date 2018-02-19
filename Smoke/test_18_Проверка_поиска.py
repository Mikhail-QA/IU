import unittest
from POM.setUp import StartInterneturok
from POM.main_page import MainPage


class CheckSearch(StartInterneturok):
    def test_search_shows_successfully(self):
        driver = self.driver
        steps_search = MainPage(driver)

        steps_search.enter_data()
        steps_search.click_search()
        self.assertIn("По запросу «ty» найдено 6 видеоуроков",
                      driver.find_element_by_css_selector("div.search-result__wrap").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
