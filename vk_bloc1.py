from class_for_vk import VK_USER
import requests
import json
import time
import sys


def decorator_for_readtimeout(function):
    def warp(*args):
        try:
            function
        except requests.exceptions.ReadTimeout:
            i = 3
            while i > 0:
                time.sleep(3)
                try:
                    function
                except requests.exceptions.ReadTimeout:
                    i -= 1
                    if i == 0:
                        sys.exit('ReadTimeout Error!')
                else:
                    i = 0
        return function(*args)
    return warp


@decorator_for_readtimeout
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


@decorator_for_readtimeout
def enter_user_and_key():
    with open('token.json') as file:
        json_data = json.load(file)
        f_token = json_data['token']
    x = True
    t = -1
    f_user_id = ''
    while x == True:
        user_data = input('Введите имя или id пользователя :')
        while t < 0:
            t = input('Введите число N. В список групп будут добавленны те,'
                    ' в которых есть общие друзья, но не более, чем N человек :')
            try:
                t = int(t)
            except ValueError:
                print('Вы ввели не число. Попробуйте еще раз.')
                t = -1
        params = {
            'user_ids': user_data,
            'access_token': f_token,
            'v': 5.92
        }
        response = requests.get('https://api.vk.com/method/users.get', params)
        res = response.json()
        try:
            for i in res['response']:
                f_user_id = i['id']
                x = False
        except KeyError:
            print('{}'.format(res['error']['error_msg']))
    return f_user_id, f_token, t


@decorator_for_readtimeout
def get_user_data(user):
    f_group_list = []
    f_friend_list = []
    response_fr = requests.get('https://api.vk.com/method/friends.get', user.params)
    response_gr = requests.get('https://api.vk.com/method/groups.get', user.params)
    r_fr = response_fr.json()
    f_r_gr = response_gr.json()
    for x in f_r_gr['response']['items']:
        f_group_list.append(x['id'])
    f_user_group = set(f_group_list)
    for x in r_fr['response']['items']:
        f_friend_list.append(x['id'])
    return f_r_gr, f_user_group, f_friend_list


def main_work(f_friend_list, f_user_group):
    z = len(f_friend_list)
    new_user_group = f_user_group
    check_list = []
    new_user_group = set(new_user_group)
    for x in f_friend_list:
        user_x = VK_USER(token, x)
        res = get_groups(user_x)
        tmp_group_list = []
        try:
            for y in res['response']['items']:
                tmp_group_list.append(y['id'])
            tmp_group = set(tmp_group_list)
            f_user_group.difference_update(tmp_group)
            check = new_user_group.intersection(tmp_group)
            check_list.append(list(check))
#            print('.', end='', flush=True)
        except KeyError:
            pass
        z -= 1
        if z != 0:
            print('Еще обработать {} друзей'.format(z))
    return f_user_group, check_list


def more_work_with_gropus(f_check_list, n):
    new_list = []
    final_list = []
    for x in f_check_list:
        for y in x:
            if y != '':
                new_list.append(y)
    for x in new_list:
        if int(new_list.count(x)) <= int(n):
            final_list.append(x)
    final_list = set(final_list)
    return final_list


def data_to_file(r_gr, f_user_group, f_some_groups):
    big_data = []
    f_user_group.update(f_some_groups)
    with open('groups.json', 'w', encoding='UTF-8') as file:
        for z in r_gr['response']['items']:
            for y in f_user_group:
                if y == z['id']:
                    data = {'name': z['name'], 'gid': z['id'], 'members_count': z['members_count']}
                    big_data.append(data)
        json.dump(big_data, file, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    user_id, token, n = enter_user_and_key()
    user = VK_USER(token, user_id)
    r_gr, user_group, friend_list = get_user_data(user)
    user_group, check_list = main_work(friend_list, user_group)
    some_groups = more_work_with_gropus(check_list, n)
    data_to_file(r_gr, user_group, some_groups)
