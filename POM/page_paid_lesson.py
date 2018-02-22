import time


# https://web-dev01.interneturok.ru/algebra/11-klass/bpovtorenie-kursa-algebry-10-klassab/kasatelnaya?seconds=0&chapter_id=51

class PagePaidLessonComment(object):
    def __init__(self, driver):
        self.driver = driver

    def click_link_comments(self):
        self.driver.find_element_by_id("comments-link").click()
        time.sleep(1)

    def write_comment(self):
        self.driver.find_element_by_name("text").send_keys("Привет Rich")
        time.sleep(1)

    def post_comment(self):
        self.driver.find_element_by_css_selector("div > div.comment__col.comment__col-body > div > button").click()
        assert (u"Привет Rich", self.driver.find_element_by_name("text").text)
        time.sleep(2)

    def delete_comment(self):
        self.driver.find_element_by_xpath("//div/div[2]/div/span[3]").click()
        assert (u"Отправить",
                self.driver.find_element_by_css_selector(
                    "div > div.comment__col.comment__col-body > div > button").text)

    def click_button_send(self):
        self.driver.find_element_by_xpath("//div/div[2]/div/button").click()

    def click_field_textarea(self):
        self.driver.find_element_by_xpath("//div/textarea").click()


class PagePaidLessonQuestion(object):
    # https://web-dev01.interneturok.ru/russian/9-klass/slozhnopodchinyonnye-predlozheniya/pravopisanie-predlozheniy-s-soyuzom-kak/questions

    def __init__(self, driver):
        self.driver = driver

    def ask_question(self):
        self.driver.find_element_by_name("text").send_keys("Привет Rich")
        time.sleep(1)

    def post_question(self):
        self.driver.find_element_by_css_selector("button.comment__button").click()
        time.sleep(1)

    def delete_question(self):
        self.driver.find_element_by_xpath("//div/div[2]/div/span[3]").click()


# https://staging.interneturok.ru/physics/7-klass/rabota-moshnost-energija/energiya-zakon-sohraneniya-energii
class Notes(object):
    def __init__(self, driver):
        self.driver = driver

    def open_notes(self):
        self.driver.find_element_by_css_selector("div.lesson-note-widget").click()
        time.sleep(1)

    def write_note(self, note="Hello"):
        self.driver.find_element_by_css_selector("textarea.ember-text-area.ember-view").send_keys(note)
        time.sleep(0.5)

    def save_note(self):
        self.driver.find_element_by_css_selector(
            "div.lesson-note-widget__mobile.lesson-note-widget__text.show > form > button").click()

    def go_to_profile(self):
        self.driver.get("https://staging.interneturok.ru/profile/notes")
        time.sleep(1.5)
        self.driver.refresh()

    def click_textarea(self):
        self.driver.find_element_by_css_selector("textarea.ember-text-area.ember-view").click()
        time.sleep(0.5)

    def check_notes(self):
        assert (self.driver.find_element_by_link_text("Hello"))


# https://staging.interneturok.ru/chemistry/8-klass/bpervonachalnye-himicheskie-predstavleniyab/himicheskie-elementy-simvoly-himicheskih-elementov
class PaidLesson(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_play_video(self):
        self.driver.find_element_by_css_selector("div.player__block-play").click()

    def click_button_pay_abonement(self):
        self.driver.find_element_by_css_selector("a.abonement__buy").click()

    def click_button_sing_in_cover(self):
        self.driver.find_element_by_css_selector("div.video-blocker__body > div > div:nth-child(1) > p > a").click()

    def click_button_comments(self):
        self.driver.find_element_by_css_selector("span.comment__action").click()


class Favourites(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_favourites(self):
        self.driver.find_element_by_css_selector("div.icon.icon-lesson-add").click()


class Value(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_value_lesson(self):
        self.driver.find_element_by_css_selector("label.ember-radio-button").click()
