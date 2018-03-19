import allure
import unittest
from POM.page_free_lesson import PageFreeLessonCheckVideo
from POM.setUp import StartInterneturok
from POM.url_lesson import URLFreeLesson


@allure.feature("Плеер Ютуб")
@allure.story("Проверяю воспроизведения видео в плеере YouTube")
class PlayVideoYouTube(StartInterneturok):
    def test_video_plays_youtube(self):
        driver = self.driver
        steps_video = PageFreeLessonCheckVideo(driver)
        ger_url = URLFreeLesson(driver)
        with allure.step("Перейти на урок"):
            ger_url.go_lesson_in_YouTube_player()
        with allure.step("Нажать на область превью"):
            steps_video.click_play_video_YouTube()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
