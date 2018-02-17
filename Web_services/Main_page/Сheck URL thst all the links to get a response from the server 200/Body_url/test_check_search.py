"""
Отправить запрос по ссылке https://staging.interneturok.ru/search?query=Clear
"""

import requests


def test_search_displayed():
    data = {'query': 'Clear'}
    r1 = requests.get('https://staging-api.interneturok.ru/v1/search', params=data)
    try:
        r1.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r1.status_code == 200
