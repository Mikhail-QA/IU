import time
import allure
from selenium.webdriver import ActionChains
from POM.setUp import StartInterneturokClassMethod
from POM.social_networks import SocialVk
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn


@allure.feature("Авторизация через соцсеть")
@allure.story("Авторизоваться на сайте ИУ П через соцсеть ВК (zheltyy.fio@mail.ru)")
class RegistrationAndAuthUserInSocialNetwork(StartInterneturokClassMethod):
    def test_000_reg_user(self):
        driver = self.driver
        auth_vk = SocialVk(driver)
        get_main_page = MainPage(driver)
        activity_popup = PopupSignIn(driver)
        with allure.step("Зайти на сайт ВК, авторизоваться П (+79852635831/Testng1991)"):
            auth_vk.auth_user_vk()
        with allure.step("Перейти на главную страницу ИУ"):
            get_main_page.go_to_internetUrok()
        with allure.step("Нажать на кнопку Войти"):
            get_main_page.go_to_sgnIn()
        with allure.step("В поп-апе авторизации нажать на кнопку Регистрация"):
            activity_popup.go_to_popup_registration()
        with allure.step("В поп-апе регистрации нажать на иконку соцсети ВК"):
            activity_popup.click_button_vk_reg()
        with allure.step("Переключится на окно dev-passport"):
            self.driver.switch_to_window(driver.window_handles[-1])
        with allure.step("В окне Регистрации dev-passport отображается заголовок с текстом (Регистрация)"):
            self.assertEqual(u"Регистрация", driver.find_element_by_css_selector("h3").text)
        with allure.step("В окне Регистрации dev-passport отображается имя П (Желтый Друсь)"):
            self.assertEqual("Желтый Друсь", driver.find_element_by_css_selector("p.b-oauth-user__name").text)
        with allure.step("В окне Регистрации dev-passport отображается E-mail П (zheltyy.fio@mail.ru)"):
            self.assertEqual("zheltyy.fio@mail.ru", driver.find_element_by_css_selector("p.b-oauth-user__email").text)
        with allure.step("В окне Регистрации dev-passport отображается текст П (zheltyy.fio@mail.ru)"):
            self.assertEqual(u"Вы впервые на InternetUrok.ru или у вас уже есть аккаунт ?",
                             driver.find_element_by_css_selector("p.center").text)
        with allure.step("В окне Регистрации dev-passport отображается кнопка (Я новый пользователь)"):
            self.assertEqual(u"Я новый пользователь", driver.find_element_by_link_text(u"Я новый пользователь").text)
        with allure.step("В окне Регистрации dev-passport отображается кнопка (У меня уже есть аккаунт)"):
            self.assertEqual(u"У меня уже есть аккаунт",
                             driver.find_element_by_link_text(u"У меня уже есть аккаунт").text)
        with allure.step("В окне Регистрации dev-passport нажать на кнопку (Я новый пользователь)"):
            auth_vk.click_button_new_user()
        with allure.step("В окне Регистрации dev-passport отображается текст (Для завершения регистрации....)"):
            self.assertEqual(
                u"Для завершения регистрации введите ваш e-mail. На указанный\nвами e-mail будет отправлено письмо с ссылкой для подтверждения.",
                driver.find_element_by_css_selector("p.center").text)
        with allure.step("В окне Регистрации dev-passport отображается текст (Действующий e-mail)"):
            self.assertEqual(u"Действующий e-mail", driver.find_element_by_css_selector("label").text)
        with allure.step(
                "В окне Регистрации dev-passport в блоке Действующий e-mail отображается E-mail П (zheltyy.fio@mail.ru)"):
            self.assertEqual("zheltyy.fio@mail.ru", driver.find_element_by_id("user_email").get_attribute("value"))
        with allure.step("В окне Регистрации dev-passport нажать на кнопку (Зарегистрироваться)"):
            auth_vk.click_button_reg()
        with allure.step("Переключится на окно IU.ru"):
            self.driver.switch_to_window(driver.window_handles[0])
        with allure.step("Дождаться регистрации и убедиться появляения нотификации (Проверить почту)"):
            assert (self.driver.find_element_by_link_text(u"Проверить почту"))

    def test_auth_user(self):
        driver = self.driver
        get_main_page = MainPage(driver)
        activity_popup = PopupSignIn(driver)
        with allure.step("Зайти на сайт ИУ"):
            get_main_page.go_to_internetUrok()
        with allure.step("Навести курсор мышки на кнопку Мой профиль"):
            element_to_hover_over = self.driver.find_element_by_css_selector("div.header__title")
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
            hover.perform()
            time.sleep(1)
        with allure.step("В меню Мой профиль нажать на кнопку Выйти"):
            get_main_page.click_button_exit_in_tab_my_profile()
        with allure.step("Нажать на кнопку Войти"):
            get_main_page.go_to_sgnIn()
        with allure.step("В поп-апе авторизации нажать на иконку соцсети ВК"):
            activity_popup.click_button_vk_auth()
            time.sleep(1)
        with allure.step("Обновить страницу"):
            driver.refresh()
            time.sleep(3)
        with allure.step("Дождать авторизации и убедиться что кнопка Войти поменялась на Мой профиль"):
            assert (self.driver.find_element_by_css_selector("div.header__menu.header__menu_profile"))
