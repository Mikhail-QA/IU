class Search(object):
    def __init__(self, driver):
        self.driver = driver

    def test_click_to_video(self):
        self.driver.find_element_by_css_selector(".ember-view > div.teacher-tabs__box_item-content > p").click()
