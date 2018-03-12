class UrlLesson(object):
    def __init__(self, driver):
        self.driver = driver

    def go_algebra_8_grade(self):
        self.driver.get("https://fast-staging.interneturok.ru/algebra/8-klass")
