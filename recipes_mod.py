def main(cook_book):
    while True:
        dish = ''
        dishes = []
        person = None
        print('Блюда в нашей книге : ', cook_book.keys())
        dish = input('Введите названия блюд (разделитель запятая)(q - выход) : ')
        if dish == 'q':
            return
        dishes = dish.split(', ')
        person = int(input('Введите количество персон: '))
        if check(cook_book, dishes, person):
            get_shop_list_by_dishes(cook_book, dishes, person)


#Вопрос
#Имеет смысл подобный блок выносить в функцию? Мне показалось, что да, но повышает ли это реально удобность читать код?
def check(cook_book, dishes, person):
    for i in dishes:
        if i not in cook_book.keys():
            print('Нет таких блюд у нас')
            return False
    if person <= 0:
        print('Неверное количество персон')
        return False
    return True


def get_shop_list_by_dishes(cook_book, dishes, person):
    show_list = {}
    print('Список покупок: ')
    for i in dishes:
        for x in cook_book[i]:
            ingridient = x['ingridient_name']
            if ingridient not in show_list.keys():
                show_list[ingridient] = {'quantity': int(x['quantity']) * person, 'measure': x['measure']}
            else:
                quantity = show_list[ingridient]['quantity'] + int(x['quantity']) * person
                show_list[ingridient] = {'quantity':quantity, 'measure':x['measure']}
    print(show_list)


def make_book():
    ingr_line =[]
    cook_book ={}
    with open('recipes.txt') as f:
        while True:
            name = f.readline().strip()
            number = f.readline().strip()
            if number == '':
                break
            if number:
                number = int(number)
                while number > 0:
                    line = f.readline().strip()
                    list_line = line.split(' | ')
                    line_dict = {'ingridient_name':list_line[0], 'quantity':list_line[1], 'measure':list_line[2]}
                    ingr_line.append(line_dict)
                    number -= 1
            cook_book[name] = ingr_line
            ingr_line = []
            f.readline()
    main(cook_book)

make_book()

