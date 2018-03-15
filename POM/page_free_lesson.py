from selenium import webdriver
import time


# https://web-dev01.interneturok.ru/biology/11-klass/evolyucionnoe-uchenie/obzor-evolyutsionnyh-predstavleniy?seconds=0

class PageFreeLessonComment(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_comments(self):
        self.driver.find_element_by_id("comments-link").click()
        time.sleep(3)

    def wtire_comment(self):
        self.driver.find_element_by_name("text").send_keys("Привет Yonga")

    def post_comment(self):
        self.driver.find_element_by_css_selector("button.comment__button").click()
        time.sleep(2)

    def delete_comment(self):
        self.driver.find_element_by_xpath("//div/div[2]/div/span[3]").click()
        assert (u"Отправить",
                self.driver.find_element_by_css_selector("div > div.comment__col.comment__col-body > div > button").text)


# https://web-dev01.interneturok.ru/biology/11-klass/evolyucionnoe-uchenie/razvitie-evolyutsionnyh-vzglyadov-v-dodarvinovskiy-period/questions
class PageFreeLessonQuestion(object):
    def __init__(self, driver):
        self.driver = driver

    def ask_question(self):
        self.driver.find_element_by_name("text").send_keys("Привет Yonga")

    def post_question(self):
        self.driver.find_element_by_css_selector("button.comment__button").click()
        time.sleep(2)

    def delete_question(self):
        self.driver.find_element_by_link_text(u"Удалить").click()


# https://web-dev01.interneturok.ru/geografy/6-klass/bgidrosferab/svoystva-vod-mirovogo-okeana?seconds=0&chapter_id=743
class PageFreeLessonCheckVideo(object):
    def __init__(self, driver):
        self.driver = driver

    def click_play_video_iu(self):
        self.driver.find_element_by_class_name("vjs-paused").click()
        time.sleep(1)

    def watching_that_video_iu_was_reproduced(self):
        assert (u"Pause", self.driver.find_element_by_class_name("vjs-control-text").text)
        time.sleep(0.5)
        assert (self.driver.find_element_by_class_name("vjs-playing"))

    def click_play_video_YouTube(self):
        self.driver.find_element_by_id("player").click()

    # def watching_that_video_YouTube_was_reproduced(self):
    # assert (
    # self.driver.find_element_by_class_name("div.html5-video-player.iv-module-loaded.playing-mode.ytp-autohide"))
    # self.driver.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()
