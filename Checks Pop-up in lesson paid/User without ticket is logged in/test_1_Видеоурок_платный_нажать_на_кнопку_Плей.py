from POM.setUp import StartInterneturokClassMethod
from POM.page_paid_lesson import PaidLesson
from POM.url_lesson import URLPaidLesson
from POM.user import AutopaymentMailRu
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn


class ClickButtonPlayInVideo(StartInterneturokClassMethod):

    def test_open_popup_in_payment_subject(self):
        driver = self.driver
        step_user = PaidLesson(driver)
        get_url = URLPaidLesson(driver)
        data_user = AutopaymentMailRu(driver)
        open_popup = MainPage(driver)
        click_enter = PopupSignIn(driver)

        open_popup.go_to_sgnIn()
        data_user.enter_email()
        data_user.enter_password()
        click_enter.click_button_login()
        get_url.go_algebra_8_grade_video()
        step_user.click_button_play_video()
        # self.driver.save_screenshot('C:\Cs\pag.png')
        assert (self.driver.find_element_by_css_selector("div.popup.popup-payment"))
