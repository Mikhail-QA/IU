class Search(object):
    def __init__(self, driver):
        self.driver = driver

    def test_click_to_video(self):
        self.driver.find_elements.by_css_selector(".ember-view > div.search-result__box_item-thumb").click()
