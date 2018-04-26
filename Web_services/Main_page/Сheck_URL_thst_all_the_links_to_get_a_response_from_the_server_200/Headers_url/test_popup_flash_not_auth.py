# """
# Отправить запрос по ссылке Подробнее о флешке https://interneturok.ru/flash
# Отправить запрос по ссылке Подробнее об абонементе https://interneturok.ru/abonement
# Отправить запрос по ссылке Оплатить абонемент https://interneturok.ru/payment/popup?id=2"
# Отправить запрос по сслыке Войти https://interneturok.ru/users/sign_in?tab=authTab"
# """
#
# import requests
#
#
# def test_link_one():
#     link = 'https://interneturok.ru/flash'
#     url = requests.get(link)
#     try:
#         url.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print('ERROR: %s' % e)
#     assert url.status_code == 200
#
#
# def test_link_two():
#     link_q = 'https://interneturok.ru/abonement'
#     url = requests.get(link_q)
#     try:
#         url.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print('ERROR: %s' % e)
#     assert url.status_code == 200
#
#
# def test_link_three():
#     link_3 = 'https://interneturok.ru/payment/popup?id=2'
#     url = requests.get(link_3)
#     try:
#         url.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print('ERROR: %s' % e)
#     assert url.status_code == 200
#
#
# def test_link_for():
#     link_4 = 'https://interneturok.ru/users/sign_in?tab=authTab'
#     url = requests.get(link_4)
#     try:
#         url.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print('ERROR: %s' % e)
#     assert url.status_code == 200
#
#
# def test_widget_flash():
#     link_5 = 'https://interneturok.ru/flash_drive/widget'
#     url = requests.get(link_5)
#     try:
#         url.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print('ERROR: %s' % e)
#     assert url.status_code == 200
