"""
Захожу на страницу Идеи и смыслы
Прохожу по всем ссылкам и ожидаю ответа 200
"""

import requests


def test_ideas_and_meanings():
    url_list = [
        'https://staging-api.interneturok.ru/v1/schedules',
        'https://staging-api.interneturok.ru/v1/schedules/472',
        'https://staging-api.interneturok.ru/v1/schedules/473',
        'https://staging-api.interneturok.ru/v1/schedules/474',
        'https://staging-api.interneturok.ru/v1/schedules/475',
        'https://staging-api.interneturok.ru/v1/schedules/476'

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

    print('\n FOUND_ERROR %s' % found_error)
    assert found_error is False
