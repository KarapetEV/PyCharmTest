import random

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги закончились!'.format(self.name), color='red')

    def go_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом!!!'.format(self.name), color='grey', on_color='on_white')

    def get_cat(self, cat):
        self.cat = cat
        self.cat.go_into_the_house(self.house)

    def buy_whiskas(self):
        self.house.cat_food += 50
        self.house.money -= 50
        cprint('{} купил кошачий корм'.format(self.name), color='yellow')

    def clean(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint('{} сделал уборку в доме'.format(self.name), color='yellow')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 10:
            self.buy_whiskas()
        elif self.house.dirt > 100:
            self.clean()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 10
        self.money = 50
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}.\n' \
               'Кошачего корма осталось {}, степень загрязненности - {}'.format(
                self.food, self.money, self.cat_food, self.dirt)


class Cat:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 50

    def __str__(self):
        return 'Сытость {}а - {}'.format(self.name, self.fullness)

    def go_into_the_house(self, house):
        self.house = house
        cprint('Ребята завели кота и назвали его {}!'.format(self.name), color='grey', on_color='on_white')

    def eat(self):
        self.fullness += 20
        self.house.cat_food -= 10
        cprint('{} поел'.format(self.name), color='cyan')

    def turn_up_walls(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('{} подрал обои'.format(self.name), color='cyan')

    def sleep(self):
        self.fullness -= 10
        cprint('{} немного поспал'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness < 20:
            self.eat()
        else:
            dice = random.randint(0, 2)
            if dice == 0:
                self.sleep()
            else:
                self.turn_up_walls()


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_the_house(house=my_sweet_home)

cat = Cat(name='Мурзик')
random.choice(citizens).get_cat(cat)

for day in range(1, 366):
    print('===================== день {} ====================='.format(day))
    for citizen in citizens:
        citizen.act()
    cat.act()
    print('------------------ в конце дня -------------------')
    for citizen in citizens:
        print(citizen)
    print(cat)
    print(my_sweet_home)

