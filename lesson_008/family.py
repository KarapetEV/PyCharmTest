from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0


class Man:

    def __init__(self, name):
        self.name = name
        self. fullness = 30
        self.happiness = 100


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def gaming(self):
        pass


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def shopping(self):
        pass

    def buy_fur_coat(self):
        pass

    def clean_house(self):
        pass


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')