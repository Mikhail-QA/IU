import requests

def test_comments():
    url_list = [
        'https://staging-api.interneturok.ru/v1/articles/610',
        'https://staging-api.interneturok.ru/v1/articles/14',
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
