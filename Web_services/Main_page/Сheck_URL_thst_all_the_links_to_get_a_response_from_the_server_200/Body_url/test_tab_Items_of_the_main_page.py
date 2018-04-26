"""
1. Захожу на главную старницу прохожу по всем предметам
кнопку "Карусель" Влево/Право. Убеждаюсь то что, ответ от сервера 200
"""

import requests


def test_tab_Items_of_the_main_page():
    url_list = [
        'https://staging-api.interneturok.ru/v1/subjects/1',  # algebra
        'https://staging-api.interneturok.ru/v1/subjects/7',  # geometria
        'https://staging-api.interneturok.ru/v1/subjects/13',  # matematika
        'https://staging-api.interneturok.ru/v1/subjects/12',  # informatika
        'https://staging-api.interneturok.ru/v1/subjects/14',  # obchestvoznanie
        'https://staging-api.interneturok.ru/v1/subjects/47',  # obj
        'https://staging-api.interneturok.ru/v1/subjects/3',  # fizika
        'https://staging-api.interneturok.ru/v1/subjects/6',  # himia
        'https://staging-api.interneturok.ru/v1/subjects/2',  # biologia
        'https://staging-api.interneturok.ru/v1/subjects/8',  # geografia
        'https://staging-api.interneturok.ru/v1/subjects/15',  # prirodavedenie
        'https://staging-api.interneturok.ru/v1/subjects/37',  # okryzauchiyMir
        'https://staging-api.interneturok.ru/v1/subjects/5',  # russkiyzik
        'https://staging-api.interneturok.ru/v1/subjects/9',  # literatura
        'https://staging-api.interneturok.ru/v1/subjects/52',  # istoriaRussia
        'https://staging-api.interneturok.ru/v1/subjects/10',  # vseobjayIstoria
        'https://staging-api.interneturok.ru/v1/subjects/4',  # angliyskiyAyzik
        'https://staging-api.interneturok.ru/v1/subjects/42',  # Chtenie

    ]

    found_error = False

    for url in url_list:
        r1 = requests.get(url)
        try:
            r1.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('ERROR: %s' % e)
            if not found_error and r1.status_code is not 200:
                found_error = True

    print('\nFOUND_ERROR %s' % found_error)
    assert found_error is False
