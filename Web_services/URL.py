import time


class SubjectPage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_algebra_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/subject/algebra/class/8")
        time.sleep(4)

    def go_literature_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/subject/literatura/class/8")
        time.sleep(4)


class PaidLessonPage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_lesson_page(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bpovtorenie-kursa-algebry-10-klassab/trigonometricheskie-funktsii-y-sin-t-y-cos-t")
        time.sleep(4)

    def go_lesson_page_tab_trainers(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bpovtorenie-kursa-algebry-10-klassab/trigonometricheskie-funktsii-y-sin-t-y-cos-t/trainers")
        time.sleep(5)

    def go_lesson_page_tab_test(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bpovtorenie-kursa-algebry-10-klassab/trigonometricheskie-funktsii-y-sin-t-y-cos-t/testcases")
        time.sleep(4)

    def go_lesson_page_tab_question(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bpovtorenie-kursa-algebry-10-klassab/trigonometricheskie-funktsii-y-sin-t-y-cos-t/questions")
        time.sleep(4)
