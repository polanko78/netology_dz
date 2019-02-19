# читаем файл

 with open('recipes.txt') as f:
     while True:
        name = f.readline().strip()
        number = f.readline().strip()
        while number >= 0:
            line = f.readline().strip()
            list_line = line.split(' | ')
            line_dict ={'ingridient_name': list_line[0], 'quantity': ist_line[1], 'measure': list_line[2]}
            ingr_line.append(line_dict)
