"""
Проверить наличия элементов на главной странице в Footer
URL: https://interneturok.ru/"	На странице отображаются: http://joxi.ru/8AnW6anuqN8BPr
"""

import allure
from Web_services.URL import SubjectPage
from Web_services.SetUp import StartInterneturokClassMethod
from Web_services.Main_page.Elements.Footer import ChecksAllElementsThePageInFooter


@allure.feature("Страница Предмет-Класс (Алгебра 8 класс)")
@allure.story("Проверка наличия элементов и текста в Footer")
class ChecksAllElementsInSubjectPageThePageInFooter(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 8 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = SubjectPage(StartInterneturokClassMethod)
        go_page.go_algebra_8_grade()

    def test_check_footer(self):
        ChecksAllElementsThePageInFooter()
        return
