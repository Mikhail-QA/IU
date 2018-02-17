"""
Захожу во Вкладку "Классы"
1. Проверка статус ответов, прохожу по всем номерам классов на главной странице.
2. Захожу в 1 класс и пролистываю по всем номерам классов с помощью стелок Влево/Вправо. "Карусель"
"""

import requests


def test_tab_classes():
    url_list = [
        'https://staging-api.interneturok.ru/v1/subjects',  # Проверка всех классов
        'https://staging-api.interneturok.ru/v1/schedules',  # Проверка всех Предметов
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
