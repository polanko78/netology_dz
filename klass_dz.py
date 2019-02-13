class animal:
    hunger = 0
    name = ''
#    sound_tup = ('Муу','Бее','Мее','Кря-Кря','Ко-Ко','Го-Го')
    sound =''
    product = 0
    
    def __init__(self, name, hunger, product, sound):
        self.name = name
        self.hunger = hunger
        self.product = product
        self.sound  = sound
    
    def eat(self):
        if self.hunger <= 0:
            self.hunger += 10
       

    def call(self):
        for s in sound_tup:
            print(self.sound)
        

class bird(animal):    
#    product = 0      #eggs

    def get_product(self):
        product += 1
        print('мы получили одно яйцо. Всего яиц собрано {}'.format(product))

    
       
        

class milky(animal):
#    product = 0      # milk

    def get_product(self):
        product += 10
        print('мы получили 10 литров молока. Всего молока {}'.format(product))

    
            

class wooly(animal):
#    product = 0      #wool

    def get_product(self):
        product += 5
        print('мы получили 5 клубков шерсти. Всего шерсти собрано {}'.format(product))

    
    
    
    

bird1 = bird('Серый', 5, 0, 'Го-Го')
cow1 = milky('Манька', 0, 0, 'Муу')
if cow1.hunger == 0:
    print('{} голодна'.format(cow1.name))
    cow1.eat()
    print(cow1.hunger)
print(cow1.__dict__)
cow1.get_product()
bird1.get_product()
cow1.get_product()


    





        
