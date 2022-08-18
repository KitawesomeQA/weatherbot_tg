import os

BOT_TOKEN = os.environ.get('5475603723:AAFGS3vWqpA6bA9jmlntVWBnHzsTtIVwmMA')
YANDEX_GEOCODER_API_TOKEN = os.environ.get('66ff42d2-f4a5-4a9e-b3e7-cc2ffe87578e')
OPEN_WEATHER_API_TOKEN = os.environ.get('2f4d502b8cfd1212980cacfc222d1eaf')


def check_all_tokens_set():
    """Проверка на то, что установлены все переменные глобального окружения, необходимые для работы бота"""
    return BOT_TOKEN is not None and YANDEX_GEOCODER_API_TOKEN is not None and OPEN_WEATHER_API_TOKEN is not None
