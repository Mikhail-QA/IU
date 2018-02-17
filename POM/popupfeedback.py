class PopupFeedback(object):

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, username):
        self.driver.find_element_by_id("user_feedback_sender").send_keys(username)

    def enter_email(self, email):
        self.driver.find_element_by_id("user_feedback_email").send_keys(email)

    def enter_text_feedback(self, text):
        self.driver.find_element_by_id("user_feedback_content").send_keys(text)

    def where_did_you_hear_about_us(self, text):
        self.driver.find_element_by_id("user_feedback_from").send_keys(text)

    def click_button_send(self):
        self.driver.find_element_by_class_name(".btn.m-actions").click()

    # def go_to_yandex(self):
    #     driver.get("https://mail.yandex.ru/")
    #     driver.implicitly_wait(10)
    #     driver.find_element_by_css_selector("#nb-1 > span > input").clear()
    #     driver.find_element_by_css_selector("#nb-1 > span > input").send_keys("test@interneturok.ru")
    #     driver.find_element_by_css_selector("#nb-2 > span > input").clear()
    #     driver.find_element_by_css_selector("#nb-2 > span > input").send_keys("xvmb-nfrb-q0sp")
    #     driver.find_element_by_css_selector(
    #         "body > div.b-page.b-page_ru > div.new-left > div.new-auth.js-new-auth > form > div:nth-child(6) > span > button").click()
    #     time.sleep(4)
    #     self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text,
    #                              r"^[\s\S]*背靠燕山[\s\S]*$")
