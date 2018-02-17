import time


class Cycles(object):
    def __init__(self, driver):
        self.driver = driver

    def delete_all_question(self):
        elements = self.driver.find_elements_by_xpath("//div/div[2]/div/span[3]")
        if len(elements) > 0:
            for element in elements:
                element.click()
                time.sleep(2)

                # elements = self.driver.find_elements_by_link_text(u"Удалить")
                # if len(elements) > 0:
                #     for element in elements:
                #         element.click()
                #         time.sleep(8)

    def delete_old_comments(self):
        elements = self.driver.find_elements_by_xpath("//div/div[2]/div/span[3]")
        if len(elements) > 0:
            for element in elements:
                element.click()
                time.sleep(2)
