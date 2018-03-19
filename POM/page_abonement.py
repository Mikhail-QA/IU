import time


class URLAbonement(object):
    def __init__(self, driver):
        self.driver = driver

    def go_page_abonement(self):
        self.driver.get("https://fast-staging.interneturok.ru/abonement")
        time.sleep(1.5)


class PageAbonement(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_buy_ticket_in_header(self):
        self.driver.find_element_by_xpath("//div[2]/div/main/div[2]/div[2]/div[1]/div[2]/a").click()

    def click_button_buy_ticket_in_footer(self):
        self.driver.find_element_by_xpath("//div[2]/div/main/div[2]/div[4]/div/a").click()
