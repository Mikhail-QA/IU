"""
2. Rel-canonical. Должен соответствовать страницы на которой находится П и быть речерез HTTPS
"""

import time
import allure
from POM.setUp import StartInterneturokLendingClassMethod


@allure.feature("Проверка rel=canonical на разных страницах")
@allure.story("Перейти по страницам и убедиться что атрибут в rel=canonical отображается HTTPS протокол ")
class CheckCanonical(StartInterneturokLendingClassMethod):
    @allure.step("Проверка rel=canonical на Главной странице")
    def test_attribute_canonical_is_HTTPS(self):
        driver = self.driver
        time.sleep(2)
        with allure.step("В rel=canonical отображается ссылка через протокол HTTPS"):
            self.assertIn(
                "https://staging.interneturok.ru/",
                driver.find_element_by_xpath("/html/head/meta[4]").get_attribute('content'))
