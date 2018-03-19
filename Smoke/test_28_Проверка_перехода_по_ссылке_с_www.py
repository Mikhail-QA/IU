"""
3. Проверка перехода на https://www.interneturok.ru/ должен открываться без "WWW" https://interneturok.ru/
"""

import time
import allure
from POM.setUp import StartInterneturokClassMethod


@allure.feature("Проверка перехода по ссылке с (WWW)")
@allure.story("Перейти по ссылке https://www.fast-staging.interneturok.ru/ и убедится что в URL не отображается WWW")
class CheckDomain(StartInterneturokClassMethod):
    def test_domain_www(self):
        URL = "https://www.interneturok.ru"
        driver = self.driver
        driver.get(URL)
        time.sleep(2)
        with allure.step(
                "После перехода по ссылке с (www.interneturok) П открывается ссылка без WWW (https://interneturok.ru/) "):
            assert driver.current_url == "https://interneturok.ru/"
