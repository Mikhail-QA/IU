import requests

def test_static_pages():
    url_list = [
        'https://staging-api.interneturok.ru/v1/articles/1590',  #'https://web-dev01.interneturok.ru/how-you-can-use-interneturok',
        'https://staging-api.interneturok.ru/v1/articles/1589',  #'https://web-dev01.interneturok.ru/video-ob-emotsionalnoy-podache',
        'https://staging-api.interneturok.ru/v1/articles/1788',  #'https://web-dev01.interneturok.ru/zamena-uroka-s-ispolzovaniem-materiala-sayta',
        'https://staging-api.interneturok.ru/v1/articles/1591',  #'https://web-dev01.interneturok.ru/pamyatka-uchitelyam',
        'https://staging-api.interneturok.ru/v1/articles/1666',  #'https://interneturok.ru/best-lessons',
        'https://staging-api.interneturok.ru/v1/articles/15',    #'https://web-dev01.interneturok.ru/smi/informatsiya-dlya-smi',
        'https://staging-api.interneturok.ru/v1/articles/9',     #'https://web-dev01.interneturok.ru/about-us/partnery',
        'https://staging-api.interneturok.ru/v1/articles/611',   #'https://web-dev01.interneturok.ru/o-proekte/blagodarnost-polzovatelyam',
        'https://play.google.com/store/apps/details?id=com.elegion.interneturok.app',
        'https://itunes.apple.com/app/interneturok/id642312818?ls=1&mt=8',
        'https://vk.com/interneturok',
        'https://www.facebook.com/Interneturok.ru',
        'https://www.youtube.com/user/InternetUrokOfficial',
        'https://staging-api.interneturok.ru/v1/articles/200',   #'https://web-dev01.interneturok.ru/usloviya-polzovaniya-saytom',
        'https://drive.google.com/file/d/0BzGDLMANhtc2OEhLd25DdFRPZWc/view',
        'https://staging-api.interneturok.ru/v1/articles/7',
        'https://staging-api.interneturok.ru/v1/posts/1625',
        'https://staging-api.interneturok.ru/v1/articles/1497',
        'https://staging-api.interneturok.ru/v1/collection',
        'https://staging-api.interneturok.ru/v1/teachers/10928',
        'https://staging-api.interneturok.ru/v1/articles/608',
        # 'https://web-dev01.interneturok.ru/flash',             # Страница находиться во фронтенде
        # 'https://staging-api.interneturok.ru/sitemap.xml',       #'https://web-dev01.interneturok.ru/sitemap',
        # 'https://web-dev01.interneturok.ru/feedbacks/new'      # Страница находиться во фронтенде
    ]

    found_error = False

    for url in url_list:
        r1 = requests.get(url)
        try:
            r1.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('\n ERROR: %s' % e)
            if not found_error and r1.status_code is not 200:
                found_error = True

    print('\nFOUND_ERROR %s' % found_error)
    assert found_error is False
