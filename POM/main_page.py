import time

from selenium.webdriver import ActionChains


class MainPage(object):
    def __init__(self, driver):
        self.driver = driver

    def click_logo(self):
        self.driver.find_element_class_name("a.b-header__logo.b-header__logo_style").click()

    def click_the_flash_button(self):
        self.driver.find_element_by_id("flash-drive-widget").click()

    def go_to_sgnIn(self):
        self.driver.find_element_by_css_selector("span.button_login").click()
        time.sleep(0.5)

    def click_the_feedback(self):
        self.driver.find_element_class_name("b-button-review__trigger-form").click()

    def click_button_check_mail(self):
        self.driver.find_element_by_css_selector(
            "#payment-blocks > div > div > div > a.info__item-button.b-button.b-button_color_green").click()

    def go_to_internetUrok(self):
        self.driver.get("https://staging.interneturok.ru")
        time.sleep(2)

    def enter_data(self, data="ty"):
        self.driver.find_element_by_css_selector("input.search.home-search").send_keys(data)

    def click_search(self):
        self.driver.find_element_by_class_name("home-search__button").click()
        time.sleep(0.5)

    def hover_mouse_to_button_my_profile(self):
        element_to_hover_over = self.driver.find_element_by_css_selector("div.header__title")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(1)

    def click_button_exit_in_tab_my_profile(self):
        self.driver.find_element_by_xpath("//div[1]/div[2]/div/div/ul/li[4]").click()


class PopupFeedback(object):
    def __init__(self, driver):
        self.driver = driver

    def open_popup(self):
        self.driver.find_element_by_css_selector("div.review_open").click()

    def enter_name(self, name="Mament5"):
        self.driver.find_element_by_xpath("//div/label/input[1]").send_keys(name)

    def enter_email(self, email="paym.not@yandex.ru"):
        self.driver.find_element_by_xpath("//div/label[2]/input").send_keys(email)

    def enter_text(self, text="背靠燕山"):
        self.driver.find_element_by_xpath("//div/label[3]/textarea").send_keys(text)

    def click_button_send(self):
        self.driver.find_element_by_css_selector("button.button_blue").click()
        time.sleep(2)

    def click_in_button_name_close(self):
        self.driver.find_element_by_css_selector("div.popup-header__close").click()
