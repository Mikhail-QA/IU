import requests

def test_education_center():
    url_list = [
        'https://interneturok.ru/school_landing/',
        'https://interneturok.ru/ege/',
        'http://univertv.ru/'
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
