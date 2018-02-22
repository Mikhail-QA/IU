import time


class FreeTest(object):
    def __init__(self, driver):
        self.driver = driver

    def go_test(self):
        self.driver.find_element_by_css_selector("div.col-action").click()
        time.sleep(1)

    def start_test(self):
        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(0.5)

        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(0.5)

        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(0.5)

        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(0.5)

        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(0.5)

    def click_button_respond(self):
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__footer.b-practice__actions > div > a.m-actions.m-retreat.b-practice__action").click()

        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div:nth-child(4) > div > div > ul > li:nth-child(1) > div > label").click()
        # time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(3) > dd > ul > li:nth-child(2) > div > label").click()
        # time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(1) > dd > ul > li > div > label").click()
        # time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(2) > dd > ul > li > div > label").click()
        # time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(3) > dd > ul > li:nth-child(2) > div > label").click()
        time.sleep(1)

    def click_button_finish(self):
        self.driver.find_element_by_link_text("Завершить").click()
        time.sleep(0.5)
