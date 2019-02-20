def main():
    dish = ''
    print('Блюда в нашей книге : ', cook_book.keys())
    dish = input('Введите названия блюд (разделитель запятая) : ')
    dishes = dish.split(', ')
    person = int(input('Введите количество персон: '))
    check(dishes, person)
    get_shop_list_by_dishes(dishes, person)

#Вопрос
#Имеет смысл подобный блок выносить в функцию? Мне показалось, что да, но повышает ли это реально удобность читать код?
def check(dishes, person):
    for i in dishes:
        if i not in cook_book.keys():
            print('Нет таких блюд у нас')
            main()
    if person <= 0:
        print('Неверное количество персон')
        main()


def get_shop_list_by_dishes(dishes, person):
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

main()
