import requests
import json
import time
from pprint import pprint

class VK_USER:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
        self.params = {
            'access_token': token,
            'v': 5.92,
            'user_id': self.user_id,
            'extended': 1,
            'fields': 'members_count'
         }

def get_groups(user_x):
    response_gr = requests.get('https://api.vk.com/method/groups.get', user_x.params)
    res_er = response_gr.json()
    try:
        if res_er['error']['error_code'] == 6:
            time.sleep(3)
            response_gr = requests.get('https://api.vk.com/method/groups.get', user_x.params)
    except KeyError:
        pass
    return response_gr.json()


def enter_user_and_key():
    with open('token.json') as file:
        json_data = json.load(file)
        token = json_data['token']
    x = True
    user_id = ''
    while x == True:
        user_data = input('Введите имя или id пользователя :')
        params = {
            'user_ids': user_data,
            'access_token': token,
            'v': 5.92
        }
        response = requests.get('https://api.vk.com/method/users.get', params)
        res = response.json()
        try:
            for i in res['response']:
                user_id = i['id']
                x = False
        except KeyError:
            print('{}'.format(res['error']['error_msg']))
    return user_id, token

def get_user_data(user):
    group_list = []
    friend_list = []
    response_fr = requests.get('https://api.vk.com/method/friends.get', user.params)
    response_gr = requests.get('https://api.vk.com/method/groups.get', user.params)
    r_fr = response_fr.json()
    r_gr = response_gr.json()
    for x in r_gr['response']['items']:
        group_list.append(x['id'])
    user_group = set(group_list)
    pprint(user_group)
    for x in r_fr['response']['items']:
        friend_list.append(x['id'])
    return r_gr, user_group, friend_list

def main_work(friend_list, user_group):
    for x in friend_list:
        user_x = VK_USER(token, x)
        res = get_groups(user_x)
        tmp_group_list = []
        try:
            for y in res['response']['items']:
                tmp_group_list.append(y['id'])
            tmp_group = set(tmp_group_list)
            user_group.difference_update(tmp_group)
            print('.', end='', flush = True)
        except KeyError:
                pass
    return user_group

def data_to_file(r_gr, user_group):
    big_data = []
    with open('groups.json', 'w', encoding='UTF-8') as file:
        for z in r_gr['response']['items']:
            for y in user_group:
                if y == z['id']:
                    data = {'name': z['name'], 'gid': z['id'], 'members_count': z['members_count']}
                    big_data.append(data)
        json.dump(big_data, file, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    user_id, token = enter_user_and_key()
    user = VK_USER(token, user_id)
    r_gr, user_group, friend_list = get_user_data(user)
    user_group = main_work(friend_list, user_group)
    data_to_file(r_gr, user_group)

