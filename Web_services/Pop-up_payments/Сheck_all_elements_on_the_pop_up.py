"""
Проверка наличия элементов в попапе Оплаты
"""
import allure
from selenium.webdriver.common.by import By
from Web_services.SetUp import StartInterneturokClassMethod
from POM.main_page import MainPage
from POM.popup_authorization_and_registration import PopupSignIn
from POM.user import AutopaymentMailRu
from POM.pageprofile import PageProfile


@allure.feature("Поп-ап оплаты")
@allure.story("Проверка наличия элементов в поп-апе Оплаты")
class CheckPopupReview(StartInterneturokClassMethod):
    @allure.step("Авторизоваться пользователем")
    def test_000_logged_user(self):
        StartInterneturokClassMethod = self.driver
        steps_main = MainPage(StartInterneturokClassMethod)
        steps_user = AutopaymentMailRu(StartInterneturokClassMethod)
        steps_popup = PopupSignIn(StartInterneturokClassMethod)
        go_profile = PageProfile(StartInterneturokClassMethod)

        steps_main.go_to_sgnIn()
        steps_user.enter_email()
        steps_user.enter_password()
        steps_popup.click_button_login()

        with allure.step("Перейти в мой профиль"):
            go_profile.go_to_my_profile()
        with allure.step("Нажать на кнопку Оплатить абонемент"):
            go_profile.click_button_buy_subscription()

    @allure.step("Левая часть поп-апа")
    def test_left_side_pop_up(self):
        with allure.step("Верхний title левого поп-апа называется 'По абонементу доступны:' "):
            self.assertEqual("По абонементу доступны:",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div:nth-child(2) > h3:nth-child(1)").text)
        with allure.step("Отображается список уроков достпуных по абонементу"):
            self.assertEqual(
                "Сервисы разделов «Математика», «Алгебра», «Геометрия», «Физика», «Химия» и «Русский язык», а также загрузка любых уроков на флешку.",
                self.driver.find_element_by_css_selector(".ember-view > div > div:nth-child(2) > p:nth-child(2)").text)

        with allure.step("Отображается кнопка Подробнее »"):
            self.assertEqual("Подробнее »",
                             self.driver.find_element_by_css_selector(".ember-view> div > div:nth-child(2) > a").text)

        with allure.step("Между текстом отображается пунктирная полоса"):
            self.assertTrue(self.is_element_present(By.XPATH, "//*[@id='ember1746']/div/div[2]/div"))

        with allure.step("Нижний title левого поп-апа называется 'В свободном доступе:' "):
            self.assertEqual("По абонементу доступны:",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div:nth-child(2) > h3:nth-child(5)").text)

        with allure.step("В конце левой части поп-апа отображается текст Все остальные разделы и сервисы"):
            self.assertEqual("Все остальные разделы и сервисы",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div:nth-child(2) > p:nth-child(6)").text)

    @allure.step("Правая часть поп-апа Header")
    def test_right_side_pop_up(self):
        with allure.step("Верхний title правого поп-апа называется 'Стоимость абонемента:'"):
            self.assertEqual("Стоимость абонемента:",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div.popup-payment__price > h3").text)

        with allure.step("В поп-апе отображается кнопка Крестик"):
            self.assertEqual("Стоимость абонемента:",
                             self.driver.find_element_by_css_selector(
                                 "div.popup-payment__close").text)

        with allure.step("В поп-апе отображается кнопка выбора тарифа payment-switcher"):
            self.assertEqual("Стоимость абонемента:",
                             self.driver.find_element_by_css_selector(
                                 "div.popup-payment__payment-switcher").text)

        with allure.step("В поп-апе отображается кнопка выбора тарифа 100 руб. за 1 месяц"):
            self.assertEqual("100 руб.",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div.popup-payment__price > div.popup-payment__payment-switcher > label.popup-payment__payment-switcher-item.active > span.popup-payment__payment-switcher-value").text)
            self.assertEqual("за 1 месяц",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div.popup-payment__price > div.popup-payment__payment-switcher > label.popup-payment__payment-switcher-item.active > span.popup-payment__payment-switcher-label").text)

        with allure.step("В поп-апе отображается кнопка выбора тарифа 900 руб. за 12 мес.(75 руб./мес.)"):
            self.assertEqual("900 руб.",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div.popup-payment__price > div.popup-payment__payment-switcher > label:nth-child(3) > span.popup-payment__payment-switcher-value").text)
            self.assertEqual("за 12 мес. (75 руб./мес.)",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div.popup-payment__price > div.popup-payment__payment-switcher > label:nth-child(3) > span.popup-payment__payment-switcher-label").text)

    @allure.step("Вкладка банковская карта")
    def test_tab_bank_card(self):
        with allure.step("В поп-апе отображается кнопка Банковская карта"):
            self.assertEqual("Банковская карта",
                             self.driver.find_element_by_css_selector(
                                 "ul.popup-payment__wrap-nav").text)
        with allure.step("В поп-апе отображается чек-бокс автопродление"):
            self.assertTrue(self.is_element_present(By.ID, "checkbox"))

        with allure.step("В поп-апе отображается текст Автопродление"):
            self.assertEqual("Автопродление",
                             self.driver.find_element_by_css_selector(
                                 "div.checkbox__wrap").text)

        with allure.step("В поп-апе отображается картинка банковских карт"):
            self.assertEqual("/assets/img/popup/card-085b58e1f9698075b9d0a22339214497.png",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div.popup-payment__price > div.popup-payment__wrap > div > div.popup-payment__wrap-content-item > div.checkbox__wrap > div").get_attribute(
                                 "src"))
        with allure.step(
                "В поп-апе отображается текст 'При включенном автопродлении абонемент будет автоматически продлеваться каждые 30 дней, с вашей карты будут списываться 100 руб. Опцию можно в любой момент отключить в личном кабинете. Автопродление возможно только при оплате банковской картой.' "):
            self.assertEqual(
                "При включенном автопродлении абонемент будет автоматически продлеваться каждые 30 дней, с вашей карты будут списываться 100 руб. Опцию можно в любой момент отключить в личном кабинете. Автопродление возможно только при оплате банковской картой.",
                self.driver.find_element_by_css_selector(
                    ".ember-view > div > div.popup-payment__price > div.popup-payment__wrap > div > div.popup-payment__wrap-content-item > p:nth-child(2)").text)

        with allure.step("В поп-апе отображается кнопка Оплатить абонемент"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.abonement__buy"))

        with allure.step("В поп-апе отображается ссылка - Частые вопросы об абонементе "):
            self.assertEqual("Частые вопросы об абонементе",
                             self.driver.find_element_by_css_selector(
                                 "a.popup-payments__wrap-more-questions").text)
        with allure.step("В поп-апе отображается текст - Оплачивая наши услуги, вы соглашаетесь с условиями"):
            self.assertEqual("Оплачивая наши услуги, вы соглашаетесь с условиями",
                             self.driver.find_element_by_css_selector(
                                 "p.popup-payment__wrap-content-small").text)

        with allure.step("В поп-апе отображается ссылка - договора-оферты "):
            self.assertEqual("договора-оферты",
                             self.driver.find_element_by_css_selector(
                                 "a.popup-payment__payment-licence").text)

    @allure.step("Перейти во вкладку Мобильный перевод")
    def test_onep_tab_mobile_pay(self):
        self.driver.find_element_by_css_selector(
            ".ember-view > div > div.popup-payment__price > div.popup-payment__wrap > ul > li:nth-child(2)").click()

        with allure.step("В поп-апе отображается кнопка Мобильный перевод"):
            self.assertEqual("Мобильный перевод",
                             self.driver.find_element_by_css_selector(
                                 "nav__tabs nav__tabs_active").text)

        with allure.step("В поп-апе отображается картинка МТС"):
            self.assertEqual("/assets/img/popup/mts-5ceca2f1003ebf1ff2a33d0cc444cb6f.png",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div.popup-payment__price > div.popup-payment__wrap > div > div.popup-payment__wrap-content-item > div > div:nth-child(1)").get_attribute(
                                 "src"))

        with allure.step("В поп-апе отображается картинка Билайн"):
            self.assertEqual("/assets/img/popup/beeline-a6c6f262703cc1edb8163b2c89bb5644.png",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div.popup-payment__price > div.popup-payment__wrap > div > div.popup-payment__wrap-content-item > div > div:nth-child(2)").get_attribute(
                                 "src"))

        with allure.step("В поп-апе отображается картинка Теле2"):
            self.assertEqual("/assets/img/popup/tele2-5f94ed38e5bc37725d2142df09de0829.png",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view > div > div.popup-payment__price > div.popup-payment__wrap > div > div.popup-payment__wrap-content-item > div > div:nth-child(3)").get_attribute(
                                 "src"))

        with allure.step("В поп-апе отображается текст Оплата только с российских номеров."):
            self.assertEqual("Оплата только с российских номеров.",
                             self.driver.find_element_by_css_selector(
                                 "p.popup-nav__licence_wrap").text)

        with allure.step("В поп-апе отображается ссылка Условия проведения платежей."):
            self.assertEqual("Условия проведения платежей.",
                             self.driver.find_element_by_css_selector(
                                 ".ember-view> div div.popup-payment__wrap-content-item > p > a:nth-child(2)").text)
