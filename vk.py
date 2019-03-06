import requests
from urllib.parse import urlencode
from pprint import pprint


class VK_USER:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def __and__(self, other):
        params = {
            'access_token': token,
            'v': 5.92,
            #            'user_id': self.user_id
            'source_uid': self.user_id,
            'target_uid': other.user_id
        }
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return response.json()


def print(user):
    pprint('https://vk.com/id{}'.format(user.user_id))
    return

if __name__ == '__main__':

    token = 'd26bab6163aedeb679b5a6fcce59108807d58b823382b945edd6fa06b9931d7de207a56c980c052a8d457'

    user1 = VK_USER(token, 139344497)
    user2 = VK_USER(token, 165822593)
    t = user1&user2
    pprint(t['response'])
    print(user1)
    print(user2)

