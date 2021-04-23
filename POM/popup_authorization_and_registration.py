import time


class PopupSignIn(object):
    def __init__(self, driver):
        self.driver = driver

    def close_popup(self):
        self.driver.find_element_by_class_name("m-close").click()

    def go_to_popup_registration(self):
        self.driver.find_element_by_link_text("Регистрация").click()

    def go_to_popup_authorization(self):
        self.driver.find_element_by_link_text("Вход").click()

    def click_button_vk_reg(self):
        self.driver.find_element_by_css_selector("a.icon-social_vk").click()

    def click_button_vk_auth(self):
        self.driver.find_element_by_css_selector("a.icon-social_vk").click()
        assert (self.driver.find_element_by_css_selector("div.header__menu.header__menu_profile"))

    def click_button_odnoklassniki(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item_icon_od").click()

    def click_button_mail(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_mm").click()

    def click_button_facebook(self):
        self.driver.find_element_by_css_selector("b-omniauth__item.b-omniauth__item_icon_fb").click()

    def click_button_google(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_gplus").click()

    def click_button_twitter(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_tw").click()

    def click_button_yandex(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_yd").click()

    def click_button_login(self):
        self.driver.find_element_by_css_selector("button.popup-button.button").click()
        time.sleep(4)
        assert (self.driver.find_elements_by_css_selector("div.header-userinfo.ember-view"))
        time.sleep(1)
        # self.assertEqual(u"Мой профиль", self.driver.find_element_by_css_selector("div.header__menu_profile").text)

    def click_button_login_in_admin_panel(self):
        self.driver.find_element_by_css_selector("input.btn").click()
        time.sleep(1)


class PopupRegistration(PopupSignIn):
    def __init__(self, driver):
        super(PopupRegistration, self).__init__(driver)

    def click_sign_up(self):
        self.driver.find_element_by_css_selector("button.button_blue").click()
        assert (self.driver.find_element_by_link_text(u"Проверить почту"))
        assert (self.driver.find_element_by_css_selector("div.header__menu.header__menu_profile"))
