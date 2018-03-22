import unittest
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_пользователь_авторизован_проверка_Header import \
    ChecksAllElementsTheHeadersUserAuth
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_пользователь_не_авторизован_проверка_Header import \
    ChecksAllElementsTheHeadersUserNotAuth
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_попап_оставить_отзыв import \
    CheckPopupReview
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_попап_флешки import \
    ChecksAllElementsInPopupFlash
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_проверка_наличия_элемента_попап_Регистрация import \
    CheckPopupReg
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_проверка_наличия_элементов_в_Body import \
    ChecksAllElementsThePageInBody
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_проверка_наличия_элементов_в_Footer import \
    ChecksAllElementsThePageInFooter
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_проверка_наличия_элементов_вкладка_Идеи_и_смыслы import \
    CheckIdea
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_проверка_наличия_элементов_вкладка_Классы import \
    CheckAllElementsTheGrades
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_проверка_наличия_элементов_вкладка_Классы_1_класс import \
    CheckAllElementsTheGradesOneSubject
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_проверка_наличия_элементов_вкладка_Предметы_Алгебра import \
    CheckAllElementsTheSubject
from Web_services.Main_page.Сheck_all_elements_on_the_home_page.test_проверка_наличия_элементов_попап_Авторизация import \
    CheckPopupAuth
from Web_services.Subject_page.Сheck_all_elements_on_the_subject_page.test_пользователь_авторизован_проверка_Header import \
    ChecksAllElementsInSubjectPageTheHeadersUserAuth
from Web_services.Subject_page.Сheck_all_elements_on_the_subject_page.test_пользователь_не_авторизован_проверка_Body import \
    ChecksAllElementsInSubjectPageTheBodyUserNotAuth
from Web_services.Subject_page.Сheck_all_elements_on_the_subject_page.test_пользователь_не_авторизован_проверка_Header import \
    ChecksAllElementsInSubjectPageTheHeadersUserNotAuth
from Web_services.Subject_page.Сheck_all_elements_on_the_subject_page.test_проверка_наличия_элементов_в_Footer import \
    ChecksAllElementsInSubjectPageThePageInFooter
from Web_services.Subject_page.Сheck_all_elements_on_the_subject_page.test_проверка_отображения_номеров_класса_во_вкладке_Grades import \
    CheckAllElementInGrade
from Web_services.Subject_page.Сheck_all_elements_on_the_subject_page.test_проверка_отображения_предметов_во_вкладке_Subject import \
    CheckAllElementInSubject
from Web_services.Paid_lesoon_page.Сheck_all_elements_on_the_lesson_page.test_пользователь_авторизован_проверка_Header import \
    ChecksAllElementsInLessonPageTheHeadersUserAuth
from Web_services.Paid_lesoon_page.Сheck_all_elements_on_the_lesson_page.test_пользователь_не_авторизован_проверка_Header import \
    ChecksAllElementsInLessonPageTheHeadersUserNotAuth
from Web_services.Paid_lesoon_page.Сheck_all_elements_on_the_lesson_page.test_пользователь_не_авторизован_проверка_Body_вкладка_Видеоурок import \
    ChecksAllElementsInLessonPageTheBodyTabVideoUserNotAuth
from Web_services.Paid_lesoon_page.Сheck_all_elements_on_the_lesson_page.test_пользователь_не_авторизован_проверка_Body_вкладка_Вопросы_к_уроку import \
    ChecksAllElementsInLessonPageTheBodyTabQuestionsUserNotAuth
from Web_services.Paid_lesoon_page.Сheck_all_elements_on_the_lesson_page.test_пользователь_не_авторизован_проверка_Body_вкладка_Тесты import \
    ChecksAllElementsInLessonPageTheBodyTabTestUserNotAuth
from Web_services.Paid_lesoon_page.Сheck_all_elements_on_the_lesson_page.test_пользователь_не_авторизован_проверка_Body_вкладка_Тренажеры import \
    ChecksAllElementsInLessonPageTheBodyTabTrainersUserNotAuth
from Web_services.Paid_lesoon_page.Сheck_all_elements_on_the_lesson_page.test_проверка_наличия_элементов_в_Footer import \
    ChecksAllElementsInLessonPageThePageInFooter
from Web_services.Subject_page.Сheck_all_elements_on_the_subject_page.test_проверка_элементов_Body_в_учебнике import ChecksAllElementsInSubjectPageTheBodyInOpenBook

# Проверка элементов и текста на главной страницы
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(ChecksAllElementsTheHeadersUserNotAuth))
suite.addTest(unittest.makeSuite(CheckPopupReview))
suite.addTest(unittest.makeSuite(ChecksAllElementsTheHeadersUserAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInPopupFlash))
suite.addTest(unittest.makeSuite(CheckPopupReg))
suite.addTest(unittest.makeSuite(ChecksAllElementsThePageInBody))
suite.addTest(unittest.makeSuite(ChecksAllElementsThePageInFooter))
suite.addTest(unittest.makeSuite(CheckIdea))
suite.addTest(unittest.makeSuite(CheckAllElementsTheGrades))
suite.addTest(unittest.makeSuite(CheckAllElementsTheGradesOneSubject))
suite.addTest(unittest.makeSuite(CheckAllElementsTheSubject))
suite.addTest(unittest.makeSuite(CheckPopupAuth))
# Проверка элементов и текста на странице Алгебра 8 класс
suite.addTest(unittest.makeSuite(ChecksAllElementsInSubjectPageTheHeadersUserAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInSubjectPageTheBodyUserNotAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInSubjectPageTheHeadersUserNotAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInSubjectPageThePageInFooter))
suite.addTest(unittest.makeSuite(CheckAllElementInGrade))
suite.addTest(unittest.makeSuite(CheckAllElementInSubject))
suite.addTest(unittest.makeSuite(ChecksAllElementsInSubjectPageTheBodyInOpenBook))
# Проверка элементов и текста на странице урока Основные понятия
suite.addTest(unittest.makeSuite(ChecksAllElementsInLessonPageTheHeadersUserAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInLessonPageTheHeadersUserNotAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInLessonPageTheBodyTabVideoUserNotAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInLessonPageTheBodyTabQuestionsUserNotAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInLessonPageTheBodyTabTestUserNotAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInLessonPageTheBodyTabTrainersUserNotAuth))
suite.addTest(unittest.makeSuite(ChecksAllElementsInLessonPageThePageInFooter))
