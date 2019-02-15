def plus(res):
    try:
        print(int(res[1]) + int(res[2]))
    except IndexError:
        print('Нехватает чисел для операции! Попробуйте еще раз')
        enter()
    except ValueError:
        print('Вы ввели не числа. Попробуйте еще раз')
        enter()
    

def minus(res):
    try:
        print(int(res[1]) - int(res[2]))
    except IndexError:
        print('Нехватает чисел для операции!')
        enter()
    except ValueError:
        print('Вы ввели не числа. Попробуйте еще раз')
        enter()


def multiply(res):
    try:
        print(int(res[1]) * int(res[2]))
    except IndexError:
        print('Нехватает чисел для операции!')
        enter()
    except ValueError:
        print('Вы ввели не числа. Попробуйте еще раз')
        enter()

def divide(res):
    try:
        print(int(res[1]) / int(res[2]))
    except IndexError:
        print('Нехватает чисел для операции!')
        enter()
    except ValueError:
        print('Вы ввели не числа. Попробуйте еще раз')
        enter()
    except ZeroDivisionError:
        print('На ноль делить нельзя! Введите другие числа')
        enter()
              


def enter():
    res = []
    check_list = ['+', '-', '*', '/']
    ent_num = input('введите данные для операции : ')
    res = ent_num.split(' ')
    assert res[0] in check_list
    if res[0] == '+':
        plus(res)
    elif res[0] == '-':
        minus(res)
    elif res[0] == '*':
        multiply(res)
    else:
        res[0] == '/'
        divide(res)
    
            
            
enter()
      
