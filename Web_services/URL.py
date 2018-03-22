import time


class SubjectPage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_algebra_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/algebra/8-klass")

    def go_literature_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/literatura/8-klass")


class Paid_lesson_page(object):
    def __init__(self, driver):
        self.driver = driver

    def go_lesson_page(self):
        self.driver.get(
            "https://staging.interneturok.ru/algebra/8-klass/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyami/osnovnye-ponyatiya")
        time.sleep(1)

    def go_lesson_page_tab_trainers(self):
        self.driver.get(
            "https://staging.interneturok.ru/algebra/8-klass/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyami/osnovnye-ponyatiya/trainers")
        time.sleep(1)

    def go_lesson_page_tab_test(self):
        self.driver.get(
            "https://staging.interneturok.ru/algebra/8-klass/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyami/osnovnye-ponyatiya/testcases")
        time.sleep(1)

    def go_lesson_page_tab_question(self):
        self.driver.get(
            "https://staging.interneturok.ru/algebra/8-klass/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyami/osnovnye-ponyatiya/questions")
        time.sleep(1)
