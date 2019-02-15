documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def main(command):
  if command == 'p':
    man_search()
  elif command == 'l':
    doc_list()
  elif command == 's':
    shelf_search()
  elif command == 'a':
    new_doc()
  elif command == 'd':
    del_doc()
  elif command == 'm':
    move_doc()
  elif command == 'as':
    add_shelf()
  elif command == 'ml':
    man_list()
 
def man_list():
  fake_doc={"type":"ПаСпОрТ", "number":"567 56"}
  documents.append(fake_doc)
  print(documents)
  for doc in documents:
    try:
      print(doc.get('name'))
    except KeyError:
      print('Произошла ошибка в документе {}.'.format(doc.get('number')))
      enter()


def man_search():
  print('Введите номер документа :')
  doc_number = str(input())
  non_doc(doc_number)
  for doc in documents:
    if doc_number == str(doc.get('number')):
      print('Имя: {}'.format(doc.get('name')))


            
def doc_list():
  for doc in documents:
    print(doc.get('type'), doc.get('number'), doc.get('name'), sep='   ')

def shelf_search():
  doc_number = str(input('Введите номер документа : '))
  non_doc(doc_number)
  for shelf in directories:
    if directories.get(shelf).count(doc_number) >= 1:
      print('Номер полки: ', shelf)
    

def new_doc():
  print('Введите новый документ в базу')
  name = str(input('Введите имя : '))
  type_doc = str(input('Введите тип : '))
  doc_number = str(input('Введите номер : '))
  shelf_input = str(input('Введите номер полки : '))
  new_doc={"type": type_doc, "number": doc_number, "name": name}
  documents.append(new_doc)
  direct = {}
  if shelf_input in directories.keys():
    for shelf in directories:     
      if shelf == shelf_input:
        directories.get(shelf).append(doc_number)
  else:
    print('Помещаем документ на новую полку.')
    new_list = []
    new_list.append(doc_number)
    direct = {shelf_input:new_list}
    directories.update(direct)
    

def del_doc():
  doc_number = str(input('Введите номер документа : '))
  non_doc(doc_number)
  for doc in documents:
    if doc_number == str(doc.get('number')):
      documents.remove(doc)
  for shelf in directories:
    if directories.get(shelf).count(doc_number) >= 1:
      directories.get(shelf).remove(doc_number)
   


def move_doc():
  doc_number = str(input('Введите номер документа : '))
  if non_doc(doc_number) == 0:
    return
  shelf_input = input('Введите номер полки : ')
  for shelf in directories:
    if directories.get(shelf).count(doc_number) >= 1:
      directories.get(shelf).remove(doc_number)
  if shelf_input in directories.keys():
    for shelf in directories:     
      if shelf == shelf_input:
        directories.get(shelf).append(doc_number)
  else:
    print('Помещаем документ на новую полку.')
    new_list = []
    new_list.append(doc_number)
    direct = {shelf_input:new_list}
    directories.update(direct)


def add_shelf():
  shelf_input = input('Введите номер полки : ')
  if shelf_input in directories.keys():
    print('Такая полка уже существует')
    return
  blank = list()
  direct = {shelf_input:blank}
  directories.update(direct)

def non_doc(doc_number):
  counter = 0
  check = 1
  for doc in documents:
    if doc_number != str(doc.get('number')):
      counter += 1
  if counter == len(documents):
    print('Вы ввели несуществующий номер документа')
    check = 0
  return check
  

def enter():
  while True:
    print('Введите команду: ')
    command = input()
    main(command)


enter()
