from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class RefreshPage(object):
    def __init__(self, driver):
        self.driver = driver

    def refresh(self):
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, 'span.profile-abonement__title')))
