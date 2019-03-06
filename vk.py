import requests
from urllib.parse import urlencode
from pprint import pprint


class VK_USER:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_param(self):
        return {
            'access_token': token,
            'v': 5.92,
            'user_id': self.user_id
        }

    def get_friends(self):
        params = self.get_param()
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()



token = 'd26bab6163aedeb679b5a6fcce59108807d58b823382b945edd6fa06b9931d7de207a56c980c052a8d457'


user1 = VK_USER(token, 139344497)
user2 = VK_USER(token, 165822593)
spisok1 = user1.get_friends()
spisok2 = user2.get_friends()
s1 = set(spisok1['response']['items'])
s2 = set(spisok2['response']['items'])
print(s1 & s2)
