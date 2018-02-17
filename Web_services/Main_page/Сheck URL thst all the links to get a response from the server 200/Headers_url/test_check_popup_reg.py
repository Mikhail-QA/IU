# """
# Посылаю запрос на появление попапа регистрации и проверяю есть ли элемент (попап регистрации) в HTML коде
# """
#
# import requests
#
#
# def test_popup_reg_displayed():
#     url = "https://interneturok.ru/users/sign_in?tab=regTab"
#     r1 = requests.get(url)
#     try:
#         r1.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print('ERROR: %s' % e)
#     assert r1.status_code == 200
