# class Checks_all_elements_the_page(StartInterneturokClassMethod):
    # def test_logo_interneturok(self):
    #     self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.b-header__logo.b-header__logo_style"))
    #
    # def test_flash(self):
    #     self.assertTrue(self.is_element_present(By.ID, "flash-drive-widget"))
    #
    # def test_signIn(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Войти"))

    # def test_text_home_title_displayed(self):
    #     self.assertEqual(u"Уроки школьной программы", self.driver.find_element_by_class_name("b-home__title").text)
    #
    # def test_text_home_desc_displayed(self):
    #     self.assertEqual(u"Видео, конспекты, тесты, тренажеры", self.driver.find_element_by_class_name("b-home__desc").text)
    #
    # def test_button_subjects(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Предметы"))
    #
    # def test_button_grades(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Класcы"))
    #
    # def test_field_search(self):
    #     self.assertTrue(self.is_element_present(By.NAME, "q"))
    #
    # def test_button_search(self):
    #     self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.b-search__submit"))
    #
    # def test_button_displayed_algebra(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Алгебра"))
    #
    # def test_button_displayed_geometry(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Геометрия"))
    #
    # def test_button_displayed_mathematics(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Математика"))
    #
    # def test_button_displayed_computer_science(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Информатика"))
    #
    # def test_button_displayed_social_studies(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Обществознание"))
    #
    # def test_button_displayed_health_basics(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"ОБЖ"))
    #
    # def test_button_displayed_physics(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Физика"))
    #
    # def test_button_displayed_chemistry(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Химия"))
    #
    # def test_button_displayed_biology(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Биология"))
    #
    # def test_button_displayed_geography(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"География"))
    #
    # def test_button_displayed_nature_study(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Природоведение"))
    #
    # def test_button_displayed_environmental_study(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Окружающий мир"))
    #
    # def test_button_displayed_russion(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Русский язык"))
    #
    # def test_button_displayed_literature(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Литература"))
    #
    # def test_button_displayed_history_of_russia(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"История России"))
    #
    # def test_button_displayed_world_history(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Всеобщая история"))
    #
    # def test_button_displayed_england(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Английский язык"))
    #
    # def test_button_displayed_reading(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Чтение"))
    #
    # def test_notification_displayed_ideas_and_meanings(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Идеи и смыслы"))
    #
    # def test_text_displayed_scientists_and_children(self):
    #     self.assertEqual(u"Ученые — детям",
    #                      self.driver.find_element_by_css_selector("strong.b-lectures-more__title > span").text)
    #
    # def test_link_displayed_on_the_screen(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Интересные лекции для школьников"))
    #
    # def test_text_displayed_parents_and_teachers(self):
    #     self.assertEqual(u"Родителям и учителям",
    #                      self.driver.find_element_by_xpath("//ul[@id='supported']/li[2]/strong").text)
    #
    # def test_link_displayed_the_screen(self):
    #     self.assertEqual(
    #         u"Полезные видеолекции:  Детская психология, Здоровье ребёнка, Советы специалистов, Психология на Univertv.ru",
    #         self.driver.find_element_by_xpath("//ul[@id='supported']/li[2]/p").text)

    # def test_block_education_center_displayed(self):
    #     self.assertEqual(u"Центр образования",
    #                      self.driver.find_element_by_css_selector("li.b-menu-blog__item.b-menu-blog__group-title").text)
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Домашняя школа"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Репетитор ЕГЭ"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, "Univertv.ru"))
    #
    # def test_block_reviews_displayed(self):
    #     self.assertEqual(u"Отзывы", self.driver.find_element_by_xpath("//div/ul[2]/li").text)
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Отзывы пользователей"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"СМИ о нас"))
    #
    # def test_block_cooperation_displayed(self):
    #     self.assertEqual(u"Сотрудничество", self.driver.find_element_by_xpath("//div/ul[3]/li").text)
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Участие в проекте"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Методический кабинет"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Партнеры"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Благодарности"))
    #
    # def test_block_about_the_project_displayed(self):
    #     self.assertEqual(u"О проекте", self.driver.find_element_by_xpath("//ul[4]/li").text)
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"О проекте"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Наши учителя"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Мы и государство"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Часто задаваемые вопросы"))
    #     self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.b-menu-blog__link > strong"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Контактная информация"))
    #
    # def test_text_apps_for_your_tablet_displayed_the_screen(self):
    #     self.assertEqual(u"Приложения для планшета:",
    #                      self.driver.find_element_by_css_selector("small.b-footer__app-desc").text)
    #
    # def test_icon_android_displayed(self):
    #     self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.b-footer__app.b-footer__app_icon_android"))
    #
    # def test_icon_apple_displayed(self):
    #     self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.b-footer__app.b-footer__app_icon_ios"))
    #
    # def test_text_we_in_social_networks(self):
    #     self.assertEqual(u"Мы в соцсетях:",
    #                      self.driver.find_element_by_css_selector("small.b-footer__social-desc").text)
    #
    # def test_icon_vk_displayed(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"ВКонтакте"))
    #
    # def test_icon_facebook_displayed(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, "Facebook"))
    #
    # def test_icon_youtube_displayed(self):
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, "YouTube"))
    #
    # def test_text_interda_displayed_the_screen(self):
    #     self.assertEqual(u"© 2010-2017 ООО «Интерда»",
    #                      self.driver.find_element_by_css_selector("div.b-footer__copyright > span").text)
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Условия пользования сайтом"))
    #     self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Политика конфиденциальности"))
    #     self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.b-footer__sitemap"))

    # def test_button_review_displayed(self):
    #     self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.b-button-review__trigger-form"))









