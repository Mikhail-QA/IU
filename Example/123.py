import requests


def get_new_post():
    payload = {
        "authenticity_token": "TeIlhUIWJJVXGKWquTopHXYG8YhqN4M7viivfKIrYzo=",
        "user[email]": "hexcal@mail.ru",
        "user[password]": "123456",
        "commit": "Войти"
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4",
        "Connection": "keep-alive",
        "Host": "web-dev01.interneturok.ru"
    }
    session = requests.Session()
    session.headers = headers
    # session.payload = payload
    r1 = session.post("https://web-dev01.interneturok.ru/users/sign_in", data=payload, headers=headers)
    r2 = session.get("https://web-dev01.interneturok.ru/", data=payload)
    print(r1.url)
    print(r1.status_code)
    # print(r1.text)
    print(r2.url)
    print(r2.status_code)
    print(r2.text)
get_new_post()
