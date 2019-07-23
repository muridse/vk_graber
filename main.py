import requests
import collections

def id_request(nick, name):
    #передает id
    user_request = 'https://api.vk.com/method/users.get?v=5.71&access_token=' + access_token + '&user_ids=' + nick
    usr = requests.get(user_request)
    user_id = usr.json()['response'][0]['id']
    if name == True:
        print(usr.json()['response'][0]['first_name'], usr.json()['response'][0]['last_name'], 'ID is:', user_id)
    return user_id

def calc_age(uid):
    #функция с помощью двух запросов
    #вытаскивает список друзей по id и сортирует их по возрасту по возрастанию
    #далее сортирует коичество друзей с возрастом N по убыванию
    uid = id_request(user_nick, 1)
    friends_request = 'https://api.vk.com/method/friends.get?v=5.71&access_token=' + access_token + '&user_id=' + str(uid) + '&fields=bdate'
    friends_data = requests.get(friends_request)

    #получаем список друзей
    #обходим каждого
    statistic = {}
    for i in range(len(friends_data.json()['response']['items'])):
        try:
            bdate = friends_data.json()['response']['items'][i]['bdate'].split('.')
            old = now_year - int(bdate[2])
        except Exception as err:
            old = 0
        try:
            statistic.update({old: statistic.get(old) + 1})
        except Exception as creating:
            statistic.update({old: 1})
    #создаем словарь ключ-возраст, содержание-количество
    calc_age_sorted = collections.OrderedDict(sorted(statistic.items()))
    print('Возраст/Люди:')
    for a, b in calc_age_sorted.items():
        print(a, b)

#задаем инпут(id или ник, токен для работы, актуальный год)
now_year = 2019
access_token = 'b23be4c5b23be4c5b23be4c548b2503776bb23bb23be4c5ef0e4e2e0c40ac12d7bc5f6f'
user_nick = 'muridse'

print('Введите нужный ник/id. Ник по умолчанию:', user_nick)
user_nick = input()

if user_nick == '':
    user_nick = 'muridse'

#вызов функции, которая вылает весь аутпут
calc_age(user_nick)
