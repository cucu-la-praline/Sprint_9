import os


def get_base_url(default_url: str = "https://foodgram-frontend-1.foodgram.education-services.ru/signin") -> str:
    """
    Получение базового URL сервиса из переменных окружения или значения по умолчанию

    Args: default_url: URL по умолчанию, если переменная окружения не установлена
    Returns: str: Базовый URL сервиса
    """
    return os.getenv("BASE_URL", default_url)
