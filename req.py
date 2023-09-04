import requests


def get_gif():
    # Замените 'YOUR_API_KEY' на ваш API-ключ GIPHY
    api_key = 'D6GTuKutX7hUuUJqcvWVEAWwh2A8wJC1'

    # URL-адрес эндпоинта API GIPHY для поиска гифок
    url = 'https://api.giphy.com/v1/gifs/random?api_key=D6GTuKutX7hUuUJqcvWVEAWwh2A8wJC1&tag=I+love+You&rating=g'

    # Отправка GET-запроса к API GIPHY
    response = requests.get(url)

    # Обработка ответа
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            gif_url = data['data']['images']['fixed_width_still'].get('url')
            if gif_url:
                print(gif_url)
                return gif_url
            else:
                print('Не удалось получить URL гифки.')
        else:
            print('Данные о гифке отсутствуют в ответе.')
    else:
        print('Произошла ошибка при выполнении запроса.')
