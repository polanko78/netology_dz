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
       

    def call(self):
        sound_tup = ('Муу','Бее','Мее','Кря-Кря','Ко-Ко','Го-Го')
#        sound =''

        sound = input('Какой звук мы слышим?')
        if sound in sound_tup:
            for s in sound_tup:
                if sound == self.sound:
                    print('Это нас завет {}'.format(self.name))
                    break
        else:
            print('Непонятный звук')
        

class bird(animal):
    product = 0      #eggs

    def get_product(self):
        self.product += 1
        print('мы получили одно яйцо. Всего яиц собрано {}'.format(self.product))

    
       
        

class milky(animal):
#    product = 0      # milk

    def get_product(self):
        self.product += 10
        print('мы получили 10 литров молока. Всего молока {}'.format(self.product))

    
            

class wooly(animal):
#    product = 0      #wool

    def get_product(self):
        self.product += 5
        print('мы получили 5 клубков шерсти. Всего шерсти собрано {}'.format(self.product))

    
    
    
    

bird1 = bird('Серый', 5, 0, 10, 'Го-Го')
bird2 = bird('Белый', 0, 0, 11, 'Го-Го')
cow1 = milky('Манька', 0, 0, 150, 'Муу')
sheep1 = wooly('Барашек', 10, 0, 60, 'Бее')
sheep2 = wooly('Кудрявый', 0, 0, 45, 'Бее')
bird3 = bird('Ко-Ко', 0, 0, 10, 'Ко-Ко')
bird4 = bird('Кукареку', 5, 0, 10, 'Ко-Ко')
bird5 = bird('Кряква', 5, 0, 10, 'Кря-Кря')
goat1 = milky('Рога', 0, 0, 50, 'Мее')
goat2 = milky('Копыта', 0, 0, 45, 'Мее')

print(animal.farm)

for an in animal.farm:
    an.eat()

    





        
