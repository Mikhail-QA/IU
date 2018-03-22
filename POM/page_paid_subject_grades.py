class PaidLessonAlgebra8(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_open_book(self):
        self.driver.find_element_by_css_selector(
            ".subject-book__body-inner:nth-child(1) .subject-book:nth-child(1)").click()
