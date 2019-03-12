import requests
from pprint import pprint

class VK_USER:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
        self.params = {
            'access_token': token,
            'v': 5.92,
            'user_id': self.user_id,
         }
    def get_groups(self):
        response_gr = requests.get('https://api.vk.com/method/groups.get', self.params)
        return response_gr.json()




if __name__ == '__main__':

    token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    user_name = '(eshmargunov)'
    id = 'id (171691064)'
    name = user_name[1:12]
    user_id = id[4:13]
    user = VK_USER(token, user_id)
    response_fr = requests.get('https://api.vk.com/method/friends.get', user.params)
#    response_gr = requests.get('https://api.vk.com/method/groups.get', params)
    r_fr = response_fr.json()
#    r_gr = response_gr.json()
    pprint(r_fr['response']['items'])
    for x in r_fr['response']['items'][0:3]:
        user_x = VK_USER(token, x)
        response_gr = requests.get('https://api.vk.com/method/groups.get', user_x.params)
        res = response_gr.json()
        pprint(res)


    # user1 = VK_USER(token, r_fr['response']['items'][0])
    # response_gr = requests.get('https://api.vk.com/method/groups.get', user1.params)
    # r_gr = response_gr.json()
    # pprint(r_gr)
