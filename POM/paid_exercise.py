import time

from selenium.common.exceptions import NoSuchElementException


class Exercise(object):
    def __init__(self, driver):
        self.driver = driver

    def go_exercise(self):
        self.driver.find_element_by_css_selector("li:nth-child(1) > div.col-action > span > a").click()
        time.sleep(3)

    def test(self):
        step = 1
        answer = 1
        please = False
        for n in range(1, 7):
            time.sleep(2)
            major_text = self.driver.find_element_by_css_selector("small.b-progress-test__desc").text
            cont_list = major_text.split(" ")
            # print(">>> ANSW COUNT", major_text)
            # print(">>> CONT LIST", cont_list)
            if int(cont_list[1]) is 1 and not please:
                step = 2
                answer = 1
                please = True
            elif int(cont_list[1]) is 2:
                return True
            element = self.driver.find_element_by_css_selector("body > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child({0}) > dd > ul > li:nth-child({1}) > div > label > span".format(
                    str(step), str(answer)))
            element.click()
            answer += 1


    def old_test(self):
        step = 1
        answer = 1
        # sample_text = u"При повороте автобуса вправо пассажиры отклоняются влево относительно автобуса, то есть, благодаря инерции, сохраняют прежнее направление движения"
        while True:
            element = self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child({0}) > dd > ul > li:nth-child({1}) > div > label > div".format(str(step), str(answer)))
            element.click()
            print(">>> ELEMENT CLICKED " + str(step) + "-" + str(answer), end="\n\n\n\n\n\n")
            try:
                # answer_text = self.driver.find_element_by_xpath("//body[@id='lessonPage']/div[5]/table/tbody/tr/td/div/div/div[4]/div/div/dl/div/dd/div/p").text
                print(">>> ANSWER FOUND " + str(step) + "-" + str(answer) + "TEXT: {}".format(answer_text), end="\n\n\n\n\n\n")
                print(">>> REFRESHING COUNTERS " + str(step) + "-" + str(answer), end="\n\n\n\n\n\n")
                step += 1
                answer = 1
                continue
            except NoSuchElementException:
                print(">>> NEXT STEP " + str(step) + "-" + str(answer), end="\n\n\n\n\n\n")
                answer += 1
                continue
        # element2 = self.driver.find_element_by_css_selector(
        #     "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(1) > dd > ul > li:nth-child(2) > div > label > div")
        # element3 = self.driver.find_element_by_css_selector(
        #     "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(1) > dd > ul > li:nth-child(3) > div > label > div")
        # if len(answer) > 0:
            # element1.click()
        # elif len(answer) == 0:
        #     element2.click()
        # elif len(answer) == 0:
        #     element3.click()
        # elif answer <= "Влево":
        #     self.driver.find_element_by_css_selector(
        #         "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(1) > dd > ul > li:nth-child(2) > div > label > div").click()

        # elements = self.driver.find_element_by_css_selector(
        #     "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(1) > dd > ul > li:nth-child(1) > div > label > div")



    def choose_the_answer(self):
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(1) > dd > ul > li:nth-child(1) > div > label > div").click()
        time.sleep(1)

        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(1) > dd > ul > li:nth-child(2) > div > label > div").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(1) > dd > ul > li:nth-child(3) > div > label > div").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(2) > dd > ul > li:nth-child(1) > div > label > div").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(2) > dd > ul > li:nth-child(2) > div > label > div").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#lessonPage > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child(2) > dd > ul > li:nth-child(3) > div > label > div").click()
        time.sleep(1)

    def click_button_finish(self):
        self.driver.find_element_by_css_selector("body > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__footer.b-practice__actions > div > a").click()
        self.driver.refresh()
        assert self.driver.find_element_by_css_selector("span.result-mark.good")
