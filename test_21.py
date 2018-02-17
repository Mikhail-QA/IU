import time
import unittest
from POM.page_free_lesson import PageFreeLessonCheckVideo
from POM.setUp import StartInterneturok
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class PlayVideoYouTube(StartInterneturok):
    def test_video_plays_youtube(self):
        driver = self.driver
        steps_video = PageFreeLessonCheckVideo(driver)
        driver.get(
            "https://fast-staging.interneturok.ru/idei-i-smysly/osnovy-ratsionalnogo-povedeniya/spisok-urokov/kogda-nam-trudno-vybirat-paradoks-kondorse")
        time.sleep(5)
        steps_video.click_play_video_YouTube()
        time.sleep(2)

        #     self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.ytp-endscreen-content"))
        #
        # def is_element_present(self, how, what):
        #     try:
        #         self.driver.find_element(by=how, value=what)
        #     except NoSuchElementException as e:
        #         return False
        #     return True
        # self.assertTrue(driver.find_element_by_css_selector("div.ytp-upnext.ytp-upnext-autoplay-paused"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
