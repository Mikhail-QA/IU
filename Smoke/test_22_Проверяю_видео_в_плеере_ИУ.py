import unittest
import allure
from POM.page_free_lesson import PageFreeLessonCheckVideo
from POM.setUp import StartInterneturok


@allure.feature("Плеер ИУ")
@allure.story("Проверяю воспроизведения видео в плеере ИУ")
class PlayVideoIu(StartInterneturok):
    def test_check_player_iu(self):
        driver = self.driver
        steps_video = PageFreeLessonCheckVideo(driver)
        with allure.step("Перейти на урок"):
            driver.get(
                "https://fast-staging.interneturok.ru/geografy/6-klass/bgidrosferab/svoystva-vod-mirovogo-okeana")
        with allure.step("Нажать на кнопку Плей"):
            steps_video.click_play_video_iu()
        with allure.step("После вкл видео в плеере появилась кнопка Pause"):
            self.assertEquals(u"Pause", self.driver.find_element_by_class_name("vjs-control-text").text)
        with allure.step("Элемент плеера поменял статус на vjs-playing"):
            assert (self.driver.find_element_by_class_name("vjs-playing"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
