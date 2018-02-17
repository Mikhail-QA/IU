import requests

def test_cooperations():
    url_list = [
        'https://staging-api.interneturok.ru/v1/articles/608',
        'https://staging-api.interneturok.ru/v1/articles/1587',
        'https://staging-api.interneturok.ru/v1/articles/9',
        'https://staging-api.interneturok.ru/v1/articles/611',
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
