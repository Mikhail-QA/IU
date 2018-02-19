import allure
import time
import unittest
from POM.page_free_lesson import PageFreeLessonCheckVideo
from POM.setUp import StartInterneturok

@allure.feature("Плеер Ютуб")
@allure.story("Проверяю воспроизведения видео в плеере YouTube")
class PlayVideoYouTube(StartInterneturok):
    def test_video_plays_youtube(self):
        driver = self.driver
        steps_video = PageFreeLessonCheckVideo(driver)
        with allure.step("Перейти на урок"):
            driver.get(
                "https://fast-staging.interneturok.ru/idei-i-smysly/osnovy-ratsionalnogo-povedeniya/spisok-urokov/kogda-nam-trudno-vybirat-paradoks-kondorse")
        time.sleep(5)
        with allure.step("Нажать на область превью"):
            steps_video.click_play_video_YouTube()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
