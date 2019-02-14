class animal:
    hunger = 0
    name = ''
    sound =''
    product = 0
    weight = 0
    farm = []
    
    
    def __init__(self, name, hunger, product, weight, sound):
        self.name = name
        self.hunger = hunger
        self.product = product
        self.sound  = sound
        self.weight = weight
        animal.farm.append(self)
    
    def eat(self):
        if self.hunger <= 0:
            self.hunger += 10
            print('Покормили {}'.format(self.name))
       

    def call():
        sound_tup = ('Муу','Бее','Мее','Кря-Кря','Ко-Ко','Го-Го')

        sound = input('Какой звук мы слышим?')
        if sound in sound_tup:
            for an in animal.farm:
                if sound == an.sound:
                    print('Это кричит {}'.format(an.name))
        else:
            print('Непонятный звук')
        

class bird(animal):
    product = 0      

    def get_product(self):
        self.product += 1
        print('мы получили одно яйцо у {}. '.format(self.name))
            
       
        

class milky(animal):

    def get_product(self):
        self.product += 10
        print('мы получили 10 литров молока у {}.'.format(self.name))

    
            

class wooly(animal):

    def get_product(self):
        self.product += 5
        print('мы получили 5 клубков шерсти у {}'.format(self.name))

    
    
def collect_product():
    prod_type = input('Какой продукт хотите собрать? ')
    if prod_type == 'яйца':
        for an in animal.farm:
            if type(an) == bird:
                an.get_product()
    elif prod_type == 'молоко':
        for an in animal.farm:
            if type(an) == milky:
                an.get_product()
    elif prod_type == 'шерсть':
        for an in animal.farm:
            if type(an) == wooly:
                an.get_product()
    else:
        print('Такого на нашей ферме нет.')

def weight_status():
    all_weight = 0
    weight_check = 0
    ws = ''
    for an in animal.farm:
        all_weight += an.weight
        if an.weight > weight_check:
            weight_check = an.weight
            ws = an.name
    print('Самое тяжелое животное {}'.format(ws))               
    print(all_weight,' кг. таков общий вес животных')
    
    
        
        
    

bird1 = bird('Серый', 5, 0, 10, 'Го-Го')
bird2 = bird('Белый', 0, 0, 11, 'Го-Го')
cow1 = milky('Манька', 0, 0, 150, 'Муу')
sheep1 = wooly('Барашек', 10, 0, 60, 'Бее')
sheep2 = wooly('Кудрявый', 0, 0, 45, 'Бее')
bird3 = bird('Ко-Ко', 0, 0, 10, 'Ко-Ко')
bird4 = bird('Кукареку', 10, 0, 10, 'Ко-Ко')
bird5 = bird('Кряква', 5, 0, 10, 'Кря-Кря')
goat1 = milky('Рога', 0, 0, 50, 'Мее')
goat2 = milky('Копыта', 0, 0, 45, 'Мее')




for an in animal.farm:
    an.eat()
collect_product()
animal.call()
weight_status()







        
