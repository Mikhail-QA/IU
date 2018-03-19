class SubjectPage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_algebra_8_grade(self):
        self.driver.get("https://fast-staging.interneturok.ru/algebra/8-klass")

    def go_literature_8_grade(self):
        self.driver.get("https://fast-staging.interneturok.ru/literatura/8-klass")


class Paid_lesson_page(object):
    def __init__(self, driver):
        self.driver = driver

    def go_lesson_page(self):
        self.driver.get(
            "https://fast-staging.interneturok.ru/algebra/8-klass/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyami/osnovnye-ponyatiya")
