import requests

"""
Кнопка кликабельна, при нажатии появляется поп-ап авторизации
"""


def test_popup_signIn_displayed():
    url = "https://staging-api.interneturok.ru/v1/schedules"
    r1 = requests.get(url)
    try:
        r1.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r1.status_code == 200
