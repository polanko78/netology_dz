def main():
    dish = ''
    print('Блюда в нашей книге : ', cook_book.keys())
    dish = input('Введите названия блюд (разделитель пробел) : ')
    dishes = dish.split(' ')
    check(dishes)
    person = input('Введите количество персон: ')
    get_shop_list_by_dishes(dishes, person)

def check(dishes):
    for i in dishes:
        if i not in cook_book.keys():
            print('Нет таких блюд у нас')
            main()


def get_shop_list_by_dishes(dishes, person):
    show_list = {}
    print('Список покупок: ')
    for i in dishes:
       for x in cook_book[i]:
           show_list[x] = {'quantity':list_line[1], 'measure':list_line[2]}





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

print(cook_book)
main()
