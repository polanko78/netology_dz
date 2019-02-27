from pprint import pprint
import xml.etree.ElementTree as ET
tree = ET.parse("newsafr.xml")
root = tree.getroot()
my_string = []
new_string =[]
count_string = []
top_string = []
xml_channel = root.findall("channel")
xml_item = root.findall("channel/item")
for ch in xml_channel:
    for item in xml_item:
        string = item.find('description')
        my_string += string.text.split(" ")
for x in my_string:
    if len(x) >= 6 :
        new_string.append(x)
for x in new_string:
    if new_string.count(x) not in count_string:
         count_string.append(new_string.count(x))
count_string.sort(reverse = True)
for x in new_string:
    if x not in top_string:
        if new_string.count(x) in count_string[:10]:
            top_string.append(x)
print('TOP 10 слов в файле новостей: ')
pprint(top_string)