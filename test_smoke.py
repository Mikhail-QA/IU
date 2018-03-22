import unittest
from Smoke.test_000_Удаление_юзеров_в_админке import RemovingUsersInAdminPanel
from Smoke.test_001_Удаление_писем_в_почте_яндекс import DeleteMailsInYandex
from Smoke.test_002_Зарегистрироваться_купить_абонемент_100_рублей_вкл_автоплатеж import \
    CreateAccountAndBuyTicket100YesAutoPayment
from Smoke.test_003_Зарегистрироваться_купить_абонемент_900_рублей_вкл_автоплатеж import \
    CreateAccountAndBuyTicket900YesAutoPayment
from Smoke.test_004_Зарегистрироваться_купить_абонемент_100_рублей_выкл_автоплатеж import \
    CreateAccountAndBuyTicket100NoAutoPayment
from Smoke.test_005_Проверить_почтовое_уведомление_ученик_с_вкл_автоплатежом import CheckTheMailUserYesAutoPayment
from Smoke.test_006_Проверить_почтовое_уведомление_ученик_с_выкл_автоплатежом import CheckTheMailUserNoAutoPayment
from Smoke.test_007_Авторизоваться_подтвердить_почту import LoginAndConfirmTheMail
from Smoke.test_008_Авторизоваться_с_абонементом_продлить_абонемент import SignInAndExtendSubscription
from Smoke.test_009_Авторизоваться_с_абонементом_проверить_в_платном_уроке_видеоурок import \
    CheckWithSubscriptionVideoInPayLesson
from Smoke.test_10_Авторизоваться_без_абонемента_проверить_в_платном_уроке_видеоурок import \
    CheckNoSubscriptionVideoInPayLesson
from Smoke.test_11_Оставить_комментарий_в_беспл_уроке import SendCommentInFreeLesson
from Smoke.test_12_Оставить_комментарий_в_платном_уроке import SendCommentInPayLesson
from Smoke.test_13_Задать_вопрос_в_уроке_в_бесплатном_предмете import AskQuestionInFreeLesson
from Smoke.test_14_Задать_вопрос_в_уроке_платного_предмета import AskQuestionInPayLesson
from Smoke.test_15_Пройти_тест_в_бесплатном_уроке import PassTestInFreeLesson
from Smoke.test_16_Пройти_тренажер_в_платном_уроке import PassSimulatorInPayLesson
from Smoke.test_17_Оставить_заметки_в_платном_уроке import WriteNoteInPayLesson
from Smoke.test_18_Проверка_поиска import CheckSearch
from Smoke.test_19_Оставить_отзыв import WriteReview
from Smoke.test_20_Отключить_автоплатеж import DisableAutoPayment
from Smoke.test_21_Проверить_видео_в_плеере_Youtube import PlayVideoYouTube
from Smoke.test_22_Проверить_видео_в_плеере_ИУ import PlayVideoIu
from Smoke.test_23_После_авторизации_проверка_соответствия_почты_пользователя import AuthAndCheckinMailUserToProfile
from Smoke.test_24_После_регистрации_проверка_соответствия_почты_пользователя import ReghAndCheckinMailUserToProfile
from Smoke.test_25_Проверка_выхода_из_профиля import CheckingOutProfile
from Smoke.test_26_Проверка_title_keywords_description import CheckMetaTeg
from Smoke.test_27_Проверка_rel_canonical import CheckCanonical
from Smoke.test_28_Проверка_перехода_по_ссылке_с_www import CheckDomain
from Smoke.test_30_Авторизация_через_соцсеть_ВК import RegistrationAndAuthUserInSocialNetwork

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(RemovingUsersInAdminPanel))
suite.addTest(unittest.makeSuite(DeleteMailsInYandex))
suite.addTest(unittest.makeSuite(CreateAccountAndBuyTicket100YesAutoPayment))
suite.addTest(unittest.makeSuite(CreateAccountAndBuyTicket900YesAutoPayment))
suite.addTest(unittest.makeSuite(CreateAccountAndBuyTicket100NoAutoPayment))
suite.addTest(unittest.makeSuite(CheckTheMailUserYesAutoPayment))
suite.addTest(unittest.makeSuite(CheckTheMailUserNoAutoPayment))
suite.addTest(unittest.makeSuite(LoginAndConfirmTheMail))
suite.addTest(unittest.makeSuite(SignInAndExtendSubscription))
suite.addTest(unittest.makeSuite(CheckWithSubscriptionVideoInPayLesson))
suite.addTest(unittest.makeSuite(CheckNoSubscriptionVideoInPayLesson))
suite.addTest(unittest.makeSuite(SendCommentInFreeLesson))
suite.addTest(unittest.makeSuite(SendCommentInPayLesson))
suite.addTest(unittest.makeSuite(AskQuestionInFreeLesson))
suite.addTest(unittest.makeSuite(AskQuestionInPayLesson))
suite.addTest(unittest.makeSuite(PassTestInFreeLesson))
suite.addTest(unittest.makeSuite(PassSimulatorInPayLesson))
suite.addTest(unittest.makeSuite(WriteNoteInPayLesson))
suite.addTest(unittest.makeSuite(CheckSearch))
suite.addTest(unittest.makeSuite(WriteReview))
suite.addTest(unittest.makeSuite(DisableAutoPayment))
suite.addTest(unittest.makeSuite(PlayVideoIu))
suite.addTest(unittest.makeSuite(PlayVideoYouTube))
suite.addTest(unittest.makeSuite(AuthAndCheckinMailUserToProfile))
suite.addTest(unittest.makeSuite(ReghAndCheckinMailUserToProfile))
suite.addTest(unittest.makeSuite(CheckingOutProfile))
suite.addTest(unittest.makeSuite(CheckMetaTeg))
suite.addTest(unittest.makeSuite(CheckCanonical))
suite.addTest(unittest.makeSuite(CheckDomain))
suite.addTest(unittest.makeSuite(RegistrationAndAuthUserInSocialNetwork))
