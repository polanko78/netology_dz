import requests
import json

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(my_text, to_lang):
    params = {
        'key': API_KEY,
        'text': my_text,
        'lang': '{}-ru'.format(to_lang),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return json_['text']


def file_send_and_write(x):
    with open(x + '.txt', encoding='UTF-8') as file:
        my_text = file.read()
    param = {
        'key': API_KEY,
        'text': my_text
    }
    res = requests.post('https://translate.yandex.net/api/v1.5/tr.json/detect', params=param)
    resj = res.json()
    new_text = translate_it(my_text, resj['lang'])
    with open(x + '-ru.txt', 'w', encoding='UTF-8') as nfile:
        nfile.write(new_text[0])


list_of_texts = ['de', 'es', 'fr']
for x in list_of_texts:
    file_send_and_write(x)


