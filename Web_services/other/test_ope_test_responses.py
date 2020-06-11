import requests


def test_success():
    url_login = "https://web-dev01.interneturok.ru/users/sign_in"
    url_main = "https://web-dev01.interneturok.ru"
    url_test = 'https://dev-quiz.interneturok.ru/v2/testcases/2440/start?token=707297&behavior=all_in_one'

    playload = {
        "authenticity_token": "RsM5CN2r53bxAfF2TqhbmTSvuk/ANAiV2H5L9OmlgYM=",
        "user[email]": "hexcal@mail.ru",
        "user[password]": "123456",
        "commit": "Войти"
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4",
        "Connection": "keep-alive",
        "Host": "web-dev01.interneturok.ru",
    }
    r = requests.post(url_login, data=playload, headers=headers)
    cookies = r.cookies.get_dict()
    cookies[
        '_identity_hosting'] = 'df0fc8bda049e5a8153084d6bf3e040af258179c5e68b49276f445b7acbc9537a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity_hosting%22%3Bi%3A1%3Bs%3A58%3A%22%5B%22ci91199%22%2C%22e8d68688-ef73-4b01-bf6f-b2a245770b56%22%2C2592000%5D%22%3B%7D'
    r2 = requests.get(url_main, cookies=cookies, headers=headers)
    r3 = requests.get(url_test, cookies=cookies, headers=headers)

    try:
        r3.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r3.status_code == 200

    print('北京位於華北平原的西北边缘' in r2.text)
    print(r2.text)
    # print(r2)
    # r3.status_code == requests.codes.ok
    # r3.raise_for_status()
    # print(r2.url)
    # print(r2.status_code)
    # print(r3.url)
    # print(r3.status_code)
    # print(r3.text)
