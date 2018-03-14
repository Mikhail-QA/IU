"""
2. Rel-canonical. Должен соответствовать страницы на которой находится П и быть речерез HTTPS
"""

import time
import allure
from POM.setUp import StartInterneturokClassMethod


@allure.feature("Проверка rel=canonical на разных страницах")
@allure.story("Перейти по страницам и убедиться что атрибут в rel=canonical отображается HTTPS протокол ")
class CheckCanonical(StartInterneturokClassMethod):
    @allure.step("Проверка rel=canonical на Главной странице")
    def test_attribute_canonical_is_HTTPS(self):
        driver = self.driver
        driver.get("https://fast-staging.interneturok.ru/")
        time.sleep(2)
        with allure.step("В rel=canonical отображается ссылка через протокол HTTPS"):
            self.assertEqual("https://fast-staging.interneturok.ru/",
                             driver.find_element_by_xpath("//link[@rel='canonical']").get_attribute('href'))
