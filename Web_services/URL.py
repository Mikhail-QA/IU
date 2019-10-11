from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class SubjectPage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_algebra_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/subject/algebra/class/8")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "h1.subject-title")))

    def go_literature_8_grade(self):
        self.driver.get("https://staging.interneturok.ru/subject/literatura/class/8")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "h1.subject-title")))


class PaidLessonPage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_lesson_page(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bpovtorenie-kursa-algebry-10-klassab/trigonometricheskie-funktsii-y-sin-t-y-cos-t")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_lesson_page_tab_trainers(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bpovtorenie-kursa-algebry-10-klassab/trigonometricheskie-funktsii-y-sin-t-y-cos-t/trainers")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_lesson_page_tab_test(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bpovtorenie-kursa-algebry-10-klassab/trigonometricheskie-funktsii-y-sin-t-y-cos-t/testcases")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_lesson_page_tab_question(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bpovtorenie-kursa-algebry-10-klassab/trigonometricheskie-funktsii-y-sin-t-y-cos-t/questions")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))
