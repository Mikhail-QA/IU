import time


class SubjectPage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_algebra_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/predmet/algebra/klass/8/8")
        time.sleep(1)

    def go_literature_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/predmet/literatura/klass/8/96")


class Paid_lesson_page(object):
    def __init__(self, driver):
        self.driver = driver

    def go_lesson_page(self):
        self.driver.get(
            "https://staging.interneturok.ru/urok/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyamiosnovnye-ponyatiya/75")
        time.sleep(1)

    def go_lesson_page_tab_trainers(self):
        self.driver.get(
            "https://staging.interneturok.ru/urok/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyamiosnovnye-ponyatiya/75/trainers")
        time.sleep(1)

    def go_lesson_page_tab_test(self):
        self.driver.get(
            "https://staging.interneturok.ru/urok/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyamiosnovnye-ponyatiya/75/testcases")
        time.sleep(1)

    def go_lesson_page_tab_question(self):
        self.driver.get(
            "https://staging.interneturok.ru/urok/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyamiosnovnye-ponyatiya/75/questions")
        time.sleep(1)
