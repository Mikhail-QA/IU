import time


class URLPaidLesson(object):
    def __init__(self, driver):
        self.driver = driver

    def go_chemistry_8_grade_video(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/chemistry/8-klass/bpervonachalnye-himicheskie-predstavleniyab/himicheskie-elementy-simvoly-himicheskih-elementov")
        time.sleep(2)

    def go_physics_7_grade_trainers(self):
        self.driver.get("https://staging.interneturok.ru/lesson/physics/7-klass/vzaimodejstvie-tel/plotnost/trainers")
        time.sleep(2)

    def go_algebra_8_grade_test(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/8-klass/algebraicheskie-drobi-arifmeticheskie-operacii-nad-algebraicheskimi-drobyami/osnovnye-ponyatiya/testcases")
        time.sleep(2)

    def go_chemistry_8_grade_questions(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/chemistry/8-klass/bpervonachalnye-himicheskie-predstavleniyab/himicheskie-elementy-simvoly-himicheskih-elementov/questions")
        time.sleep(2)

    def go_algebra_11_grade_comment(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/algebra/11-klass/bzadachi-iz-egeb/urok-17-vopros-3-vypolnyayte-proverku-v-uravneniyah-i-neravenstvah/questions")
        time.sleep(2)


class URLFreeLesson(object):
    def __init__(self, driver):
        self.driver = driver

    def go_biology_11_grade_comment(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/biology/11-klass/evolyucionnoe-uchenie/obzor-evolyutsionnyh-predstavleniy/testcases")
        time.sleep(2)

    def go_biology_11_grade_questions(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/biology/11-klass/evolyucionnoe-uchenie/razvitie-evolyutsionnyh-vzglyadov-v-dodarvinovskiy-period/questions")
        time.sleep(2)

    def go_biology_7_grade_test(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/biology/7-klass/zhivotnye-ploskie-chervi/ploskie-chervi/testcases")
        time.sleep(2)

    def go_lesson_in_YouTube_player(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/obzh/6-klass/ekstremalnaya-situatsiya-v-prirode-i-pervoocherednye-deystviya-cheloveka-popavshego-v-neyo/opasnye-i-ekstremalnye-situatsii-chto-k-nim-privodit")
        time.sleep(2)

    def go_biology_11_grade_video(self):
        self.driver.get(
            "https://staging.interneturok.ru/lesson/biology/11-klass/evolyucionnoe-uchenie/obzor-evolyutsionnyh-predstavleniy?block=player")
        time.sleep(2)
