from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0

    def __str__(self):
        return 'Денег: {} | Еды: {} | Степень загрязненности: {}'.format(self.money, self.food, self.dirt)


class Man:
    total_food = 0

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house
        self.food_count = 0

    def __str__(self):
        return '{} - Сытость: {} | Уровень счастья: {}'.format(self.name, self.fullness, self.happiness)

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 0 or self.happiness < 10:
            if isinstance(self, Husband):
                cprint('{} умер...'.format(self.name), color='red')
            else:
                cprint('{} умерла...'.format(self.name), color='red')
            return
        elif self.fullness <= 10:
            self.eat()
        else:
            return True

    def eat(self):
        self.food_count = randint(1, 30)
        self.house.food -= self.food_count
        self.fullness += self.food_count
        if isinstance(self, Husband):
            cprint('{} съел {} еды.'.format(self.name, self.food_count), color='blue')
        else:
            cprint('{} съела {} еды.'.format(self.name, self.food_count), color='magenta')
        Man.total_food += self.food_count


class Husband(Man):
    total_money = 0

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            dice = randint(1, 4)
            if self.house.money < 20:
                self.work()
            elif dice == 1:
                self.eat()
            elif dice == 2:
                self.work()
            else:
                self.gaming()

    def eat(self):
        super().eat()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        cprint('{} сходил на работу.'.format(self.name), color='blue')
        Husband.total_money += 150

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint('{} играл в танки.'.format(self.name), color='blue')


class Wife(Man):
    total_fur_coat = 0

    def __init__(self, name, house):
        super().__init__(name=name, house=house)
        self.dirt_count = 0

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            dice = randint(1, 4)
            if self.house.food < 20:
                self.shopping()
            elif dice == 1:
                self.eat()
            elif dice == 2:
                self.shopping()
            elif dice == 3:
                self.buy_fur_coat()
            else:
                self.clean_house()

    def eat(self):
        super().eat()

    def shopping(self):
        if self.house.money >= 20:
            self.fullness -= 10
            self.house.money -= 50
            self.house.food += 50
            cprint('{} сходила в магазин.'.format(self.name), color='magenta')
        else:
            cprint('{} хотела сходить в магазин, но нет денег.'.format(self.name), color='magenta')

    def buy_fur_coat(self):
        if self.house.money >= 370:
            self.fullness -= 10
            self.house.money -= 350
            self.happiness += 60
            cprint('{} купила себе шубу.'.format(self.name), color='magenta')
            Wife.total_fur_coat += 1
        else:
            cprint('{} хотела купить себе шубу, но не хватило денег.'.format(self.name), color='magenta')

    def clean_house(self):
        self.dirt_count = randint(1, 100)
        if self.house.dirt < self.dirt_count:
            self.dirt_count = self.house.dirt
        self.fullness -= 10
        self.house.dirt -= self.dirt_count
        cprint('{} сделала уборку на {} единиц грязи.'.format(self.name, self.dirt_count), color='magenta')


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

for day in range(1, 10):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    home.dirt += 5
    cprint(serge, color='yellow')
    cprint(masha, color='yellow')
    cprint(home, color='cyan')
cprint('================== Итог ==================', color='red')
cprint('Всего заработано денег: {} | съедено еды: {} | куплено шуб: {}'.format(
    Husband.total_money, Man.total_food, Wife.total_fur_coat), color='cyan')