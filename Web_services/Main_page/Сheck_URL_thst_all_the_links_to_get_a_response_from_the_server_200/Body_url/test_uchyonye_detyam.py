import requests

"""
Отправить запрос по ссылке https://interneturok.ru/search?q=Clear
"""


def test_popup_reg_displayed():
    url = "https://staging-api.interneturok.ru/v1/schedules/434"
    r1 = requests.get(url)
    try:
        r1.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r1.status_code == 200
