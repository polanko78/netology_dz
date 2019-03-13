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
    def get_groups(self):
        response_gr = requests.get('https://api.vk.com/method/groups.get', self.params)
        return response_gr.json()


if __name__ == '__main__':
    group_list = []
    friend_list = []
    big_data = []
    token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    id = 'id (171691064)'
    user_id = id[4:13]
    user = VK_USER(token, user_id)
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
    for x in friend_list:
        user_x = VK_USER(token, x)
        res = user_x.get_groups()
        tmp_group_list = []
        try:
            for x in res['response']['items']:
                tmp_group_list.append(x['id'])
            tmp_group = set(tmp_group_list)
            user_group.difference_update(tmp_group)
            print('.', end='', flush=True)
        except KeyError:
            pass
#    print('\n')
#    pprint(user_group)
    with open('groups.json', 'w', encoding='UTF-8') as file:
        for x in r_gr['response']['items']:
            for y in user_group:
                if y == x['id']:
                    data = {'name': x['name'], 'gid': x['id'], 'members_count': x['members_count']}
                    big_data.append(data)
        json.dump(big_data, file, ensure_ascii=False, indent=1)
