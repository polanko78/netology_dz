import datetime

class File_date:

    def __init__(self, file_path):
        self.file_path = file_path
        self.start = datetime.datetime.now()

    def __enter__(self):
        self.dictionary = {}
        self.name_check = []
        name_c = []
        with open(self.file_path) as f:
            while True:
                list_tmp = f.readline()
                if list_tmp == '':
                    break
                else:
                    list = list_tmp.split(', ')
                    name_c.append(list[0])
                    name_tmp1 = list[0].split(' ')
                    self.name_check.append(name_tmp1[0])
                    self.dictionary[name_tmp1[0]] = {'name':name_tmp1[1] + ' ' + name_tmp1[2], 'workplace':list[2], 'position':list[3], 'email':list[4], 'tel':list[6]}
        return self

    def list_dict(self):
        print('Список в записной книге :')
        for name in my_dict.dictionary.keys():
            print(name, my_dict.dictionary[name]['name'])
        print('-_-_-_-_-_-_-_-_-_-_-')


    def man(self):
        name = input('Введите фамилию :')
        if name in my_dict.name_check:
            print("Имя  {} {}".format(name, my_dict.dictionary[name]['name']))
            print('Место работы  {}'.format(my_dict.dictionary[name]['workplace']))
            print('Должность  {}'.format(my_dict.dictionary[name]['position']))
            print('Почта  {}'.format(my_dict.dictionary[name]['email']))
            print('Телефон  {}'.format(my_dict.dictionary[name]['tel']))
        else:
            print('Неверное имя')


    def __exit__(self, exc_type, exc_val, exc_tp):
        self.end = datetime.datetime.now()
        print('Начало работы {}'.format(self.start))
        print('Окончание работы {}'.format(self.end))
        print('Время работы {}'.format(self.end - self.start))
        print('-_-_-_-_-_-_-_-_-_-_-')

def menu(my_dict):
    print('Доступные операции с записной книжкой:')
    print('"l" - список записей')
    print('"m" - развернутый вывод по имени')
    print('Любая другая команда - выход')
    while True:
        command = input('Введите команду: ')
        if command == 'l':
            my_dict.list_dict()
        elif command == 'm':
            my_dict.man()
        else:
            print('Выход.')
            break



with File_date('file.txt') as my_dict:
    menu(my_dict)
