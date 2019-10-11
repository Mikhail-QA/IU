from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class URLPaidLesson(object):
    def __init__(self, driver):
        self.driver = driver

    def go_chemistry_8_grade_video(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/chemistry/8-klass/bpervonachalnye-himicheskie-predstavleniyab/himicheskie-elementy-simvoly-himicheskih-elementov")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_physics_7_grade_trainers(self):
        self.driver.get("https://staging.interneturok.ru/lesson/physics/7-klass/vzaimodejstvie-tel/plotnost/trainers")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_algebra_8_grade_test(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/8-klass/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyami/osnovnye-ponyatiya/testcases")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_chemistry_8_grade_questions(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/chemistry/8-klass/bpervonachalnye-himicheskie-predstavleniyab/himicheskie-elementy-simvoly-himicheskih-elementov/questions")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_algebra_11_grade_comment(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bzadachi-iz-egeb/urok-17-vopros-3-vypolnyayte-proverku-v-uravneniyah-i-neravenstvah/questions")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))


class URLFreeLesson(object):
    def __init__(self, driver):
        self.driver = driver

    def go_biology_11_grade_comment(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/biology/11-klass/evolyucionnoe-uchenie/obzor-evolyutsionnyh-predstavleniy/testcases")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_biology_11_grade_questions(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/biology/11-klass/evolyucionnoe-uchenie/razvitie-evolyutsionnyh-vzglyadov-v-dodarvinovskiy-period/questions")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_biology_7_grade_test(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/biology/7-klass/zhivotnye-ploskie-chervi/lentochnye-chervi/testcases")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_lesson_in_YouTube_player(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/obzh/6-klass/ekstremalnaya-situatsiya-v-prirode-i-pervoocherednye-deystviya-cheloveka-popavshego-v-neyo/opasnye-i-ekstremalnye-situatsii-chto-k-nim-privodit")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))

    def go_biology_11_grade_video(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/biology/11-klass/evolyucionnoe-uchenie/obzor-evolyutsionnyh-predstavleniy")
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson-note-widget")))
