from selenium import webdriver
import time


class URLPaidLesson(object):
    def __init__(self, driver):
        self.driver = driver

    def go_algebra_8_grade_video(self):
        self.driver.get(
            "https://fast-staging.interneturok.ru/chemistry/8-klass/bpervonachalnye-himicheskie-predstavleniyab/himicheskie-elementy-simvoly-himicheskih-elementov")
        time.sleep(2)

    def go_algebra_8_grade_trainers(self):
        self.driver.get(
            "https:/fast-staging.interneturok.ru/chemistry/8-klass/bpervonachalnye-himicheskie-predstavleniyab/himicheskie-elementy-simvoly-himicheskih-elementov/trainers")
        time.sleep(1.5)

    def go_algebra_8_grade_test(self):
        self.driver.get(
            "https://fast-staging.interneturok.ru/chemistry/8-klass/bpervonachalnye-himicheskie-predstavleniyab/himicheskie-elementy-simvoly-himicheskih-elementov/testcases")
        time.sleep(1.5)

    def go_algebra_8_grade_questions(self):
        self.driver.get(
            "https://fast-staging.interneturok.ru/chemistry/8-klass/bpervonachalnye-himicheskie-predstavleniyab/himicheskie-elementy-simvoly-himicheskih-elementov/questions")
        time.sleep(1.5)
