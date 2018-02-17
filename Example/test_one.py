import requests

url_list = [
    'https://web-dev01.interneturok.ru/',
    'https://web-dev01.interneturok.ru/status/404',
    'https://interneturok.ru/school_landing/',
    'https://interneturok.ru/school_landing/status/404'
]

for url in url_list:
    r1 = requests.get(url)
    try:
        r1.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
        assert r1.status_code == 200
