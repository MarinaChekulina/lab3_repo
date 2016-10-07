from base_client import BaseClient
from datetime import date

#получение возраста
def get_age(birthday):
    today = date.today()
    #формат даты рождения дд.мм.гггг
    #для года
    age = today.year - int(birthday[2], base=10)
    #проверка по месяцам
    if today.month < int(birthday[1], base=10):
        age -= 1
    #проверка по дню в месяце
    elif today.month == int(birthday[2], base=10) and today.day < int(birthday[0], base=10):
        age -= 1
    return age

class GetUser(BaseClient):
# можно через браузер проверить http://api.vk.com/method/users.get?user_ids=id33732528
    BASE_URL = 'https://api.vk.com/method/'
    method = 'users.get'

    def response_handler(self, response):
        # строка
        user_1 = response.json()
        # response-словарь см.main
        us_id = user_1['response'][0]['uid']
        return us_id


    def __init__(self, name):
        self.username = name

    def get_params(self):
        return {
            'user_ids': self.username
        }


class GetFriendsAges(BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'friends.get'

    def response_handler(self, response):
        result = []
        friends = response.json()  # массив словарей
        for i in range(len(friends['response'])):
            if ('bdate' in friends['response'][i] and len(friends['response'][i]['bdate'].split('.')) == 3):
                result.append(get_age(friends['response'][i]['bdate'].split('.')))
        return result

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self):
        return {
            'user_id': self.user_id,
            'fields': 'bdate'
        }