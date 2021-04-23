import time


class URLAbonement(object):
    def __init__(self, driver):
        self.driver = driver

    def go_page_abonement(self):
        self.driver.get("https://staging.interneturok.ru/abonement")
        time.sleep(3)

    def go_page_class(self):
        self.driver.get('https://staging.interneturok.ru/class')
        time.sleep(3)

    def click_link_abonement(self):
        self.driver.find_element_by_css_selector('div.col-12.col-sm-6.col-md-3:nth-child(4) li:nth-child(5) a ').click()


class PageAbonement(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_buy_ticket_in_header(self):
        self.driver.find_element_by_xpath("//div[2]/div/main/div[2]/div[2]/div[1]/div[2]/a").click()
        time.sleep(1.5)

    def click_button_buy_ticket_in_footer(self):
        self.driver.find_element_by_xpath("//div[2]/div/main/div[2]/div[4]/div/a").click()
        time.sleep(1.5)
