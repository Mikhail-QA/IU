# """
# Проверяю ответы от сервера статус 200, прохожу по всем вкладкам, меню Мой профиль
# """
#
# import requests
#
#
# def test_my_profile():
#     url_login = "https://web-dev01.interneturok.ru/users/sign_in"
#     url_main = "https://web-dev01.interneturok.ru"
#     url_profile = 'https://web-dev01.interneturok.ru/profile'
#     url_profile_comments = 'https://web-dev01.interneturok.ru/profile/comments'
#     url_profile_question = 'https://web-dev01.interneturok.ru/profile/questions'
#     url_profile_signout = 'https://web-dev01.interneturok.ru/signout'
#     playload = {
#         "authenticity_token": "RsM5CN2r53bxAfF2TqhbmTSvuk/ANAiV2H5L9OmlgYM=",
#         "user[email]": "hexcal@mail.ru",
#         "user[password]": "123456",
#         "commit": "Войти"
#     }
#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate",
#         "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4",
#         "Connection": "keep-alive",
#         "Host": "web-dev01.interneturok.ru",
#     }
#     r = requests.post(url_login, data=playload, headers=headers)
#     cookies = r.cookies.get_dict()
#     cookies[
#         '_identity_hosting'] = 'df0fc8bda049e5a8153084d6bf3e040af258179c5e68b49276f445b7acbc9537a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity_hosting%22%3Bi%3A1%3Bs%3A58%3A%22%5B%22ci91199%22%2C%22e8d68688-ef73-4b01-bf6f-b2a245770b56%22%2C2592000%5D%22%3B%7D'
#     r2 = requests.get(url_main, cookies=cookies, headers=headers)
#     r3 = requests.get(url_profile, cookies=cookies, headers=headers)
#     r4 = requests.get(url_profile_comments, cookies=cookies, headers=headers)
#     r5 = requests.get(url_profile_question, cookies=cookies, headers=headers)
#     r6 = requests.delete(url_profile_signout, cookies=cookies, headers=headers)
#
#     try:
#         r3.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print('ERROR: %s' % e)
#     assert r3.status_code == 200
#     assert r4.status_code == 200
#     assert r5.status_code == 200
#     assert r6.status_code == 200
