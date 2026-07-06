class SuccessMessages:
    """Успешный ответ"""

    CREATE_SUCCESS = '{"ok":true}'


class ErrorsMessages:
    """Ошибки для ручек курьера"""

    CREATE_NOT_ENOUGH_DATA = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    CREATE_LOGIN_ALREADY_USED = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    LOGIN_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для входа'}
    LOGIN_NOT_FOUND = '{"code":404,"message":"Учетная запись не найдена"}'
