import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class All_elements(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        # self.verificationErrors = []
    def logotype_internetUrok(self):
        try:
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.b-header__logo.b-header__logo_style"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def button_flash(self):
        try:
            self.assertTrue(self.is_element_present(By.ID, "flash-drive-widget"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def button_sign_in(self):
        try:
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Войти"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def button_subjects(self):
        try:
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Предметы"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def button_grades(self):
        try:
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Класcы"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def element_search(self):
        try:
            self.assertTrue(self.is_element_present(By.NAME, "q"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def button_search(self):
        try:
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.b-search__submit"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def subject_algebra(self):
        try:
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Алгебра"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def subject_geometry(self):
        try:
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Геометрия"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def subject_mathematics(self):
        try:
            self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Математика"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def elem(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "1231313a.b-header__logo.b-header__logo_style"))
        self.assertTrue(self.is_element_present(By.ID, "flash-drive-widget"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Вой2ти"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "h1.b-home__title"))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True



