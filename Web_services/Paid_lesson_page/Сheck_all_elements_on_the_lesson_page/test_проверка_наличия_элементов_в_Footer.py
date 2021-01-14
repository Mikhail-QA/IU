import allure
from Web_services.URL import PaidLessonPage
from Web_services.SetUp import StartInterneturokClassMethod
from Web_services.Main_page.Elements.Footer import ChecksAllElementsThePageInFooter


@allure.feature("Страница урока Тригонометрические функции y = sin t, y = cos t (Алгебра 11 класс)")
@allure.story("Проверка наличия элементов и текста в Footer")
class ChecksAllElementsInLessonPageThePageInFooter(StartInterneturokClassMethod):
    @allure.step("Перейти на страницу Алгебра 11 класс")
    def test_000_open_page(self):
        StartInterneturokClassMethod = self.driver
        go_page = PaidLessonPage(StartInterneturokClassMethod)
        go_page.go_lesson_page()

    def test_check_footer(self):
        ChecksAllElementsThePageInFooter()
        return
