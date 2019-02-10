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
 

def man_search():
  print('Введите номер документа :')
  doc_number = str(input())
  for doc in documents:
    if doc_number == str(doc.get('number')):
      print('Имя: {}'.format(doc.get('name')))
            
def doc_list():
  for doc in documents:
    print(doc.get('type'), doc.get('number'), doc.get('name'), sep='   ')

def shelf_search():
  print('Введите номер документа :')
  doc_number = str(input())
  for shelf in directories:
    if directories.get(shelf).count(doc_number) >= 1:
      print('Номер полки: ', shelf)

def new_doc():
  print('Введите новый документ в базу')
  name = str(input('Введите имя : '))
  type_doc = str(input('Введите тип : '))
  number = str(input('Введите номер : '))
  shelf_input = str(input('Введите номер полки : '))
  new_doc={"type": type_doc, "number": number, "name": name}
  documents.append(new_doc)
  direct = {}
  if shelf_input in directories.keys():
    for shelf in directories:     
      if shelf == shelf_input:
        directories.get(shelf).append(number)
  else:
    direct = {shelf_input:number}
    directories.update(direct)


def del_doc():
  counter = 0
  number = str(input('Введите номер документа : '))
  for doc in documents:
    counter += 1
    if number == str(doc.get('number')):
      documents.remove(doc)
  for shelf in directories:
      if directories.get(shelf).count(number) >= 1:
        directories.get(shelf).remove(number)
   


def move_doc():
  number = str(input('Введите номер документа : '))
  shelf_input = input('Введите номер полки : ')
  for shelf in directories:
    if directories.get(shelf).count(number) >= 1:
      directories.get(shelf).remove(number)
  for shelf in directories:
    if shelf == shelf_input:
      directories.get(shelf).append(number)


def add_shelf():
  shelf_input = input('Введите номер полки : ')
  blank = list()
  direct = {shelf_input:blank}
  directories.update(direct)



                 
    


        

    

while True:
    print('Введите команду: ')
    command = input()
    main(command)


