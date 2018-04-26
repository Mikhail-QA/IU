# """
# Посылаю запрос на появление попапа авторизации и проверяю есть ли элемент (попап авторизации) в HTML коде
# """
#
# import requests
#
#
# def test_popup_signIn_displayed():
#     url = "https://web-dev01.interneturok.ru/users/sign_in?tab=authTab"
#     popup_auth = 'class="js-form-toggler" data-form="auth"'
#     r1 = requests.get(url)
#     try:
#         r1.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print('ERROR: %s' % e)
#     assert r1.status_code == 200
#     assert (popup_auth in r1.text)
