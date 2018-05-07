import time


class SubjectPage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_algebra_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/algebra/8-klass")
        time.sleep(1)

    def go_literature_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/literatura/8-klass")


class PaidLessonPage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_lesson_page(self):
        self.driver.get(
            "https://staging.interneturok.ru/urok/bpovtorenie-kursa-algebry-10-klassabtrigonometricheskie-funktsii-y-sin-t-y-cos-t/271")
        time.sleep(1)

    def go_lesson_page_tab_trainers(self):
        self.driver.get(
            "https://staging.interneturok.ru/urok/bpovtorenie-kursa-algebry-10-klassabtrigonometricheskie-funktsii-y-sin-t-y-cos-t/271/trainers")
        time.sleep(1)

    def go_lesson_page_tab_test(self):
        self.driver.get(
            "https://staging.interneturok.ru/urok/bpovtorenie-kursa-algebry-10-klassabtrigonometricheskie-funktsii-y-sin-t-y-cos-t/271/testcases")
        time.sleep(1)

    def go_lesson_page_tab_question(self):
        self.driver.get(
            "https://staging.interneturok.ru/urok/bpovtorenie-kursa-algebry-10-klassabtrigonometricheskie-funktsii-y-sin-t-y-cos-t/271/questions")
        time.sleep(1)
