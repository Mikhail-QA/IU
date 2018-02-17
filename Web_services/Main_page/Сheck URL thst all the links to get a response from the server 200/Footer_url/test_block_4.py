import requests

def test_about_the_project():
    url_list = [
        # 'https://staging.interneturok.ru/about-us/o-proekte', # страницу поместили в фронтенд
        'https://staging-api.interneturok.ru/v1/teachers',
        'https://staging-api.interneturok.ru/v1/articles/1158',
        'https://staging-api.interneturok.ru/v1/articles/17',
        # 'https://staging.interneturok.ru/abonement', # страницу поместили в фронтенд
        # 'https://staging.interneturok.ru/kontakty', # страницу поместили в фронтенд
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
