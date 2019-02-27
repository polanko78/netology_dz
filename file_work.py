import json
from pprint import pprint

new_string =[]
top_string =[]
count_string = []

with open('newsafr.json') as newsafr:
    json_data = json.load(newsafr)
    for i in json_data['rss']['channel']['items']:
        my_string = i['description'].split()
        for x in my_string:
            if len(x) >= 6 :
                new_string.append(x)
    for x in new_string:
        if new_string.count(x) not in count_string:
            count_string.append(new_string.count(x))
    count_string.sort(reverse = True)
    for x in new_string:
        if x not in top_string:
            if new_string.count(x) in count_string[0:10]:
                top_string.append(x)
    print('TOP 10 слов в файле новостей: ')
    pprint(top_string)




