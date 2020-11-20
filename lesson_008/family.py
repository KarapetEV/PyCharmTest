from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return 'Денег: {} | Еды: {} | Степень загрязненности: {} | Кошачего корма: {}'.format(
            self.money, self.food, self.dirt, self.cat_food)


class Man:
    total_food = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.food_count = 0

    def __str__(self):
        return '{} - Сытость: {} | Уровень счастья: {}'.format(self.name, self.fullness, self.happiness)

    def move_to_house(self, house):
        self.house = house
        cprint('{} въехал в новый дом!'.format(self.name), color='grey', on_color='on_white')

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 0 or self.happiness <= 0:
            if isinstance(self, Husband):
                cprint('{} умер...'.format(self.name), color='red')
            else:
                cprint('{} умерла...'.format(self.name), color='red')
            return
        else:
            return True

    def eat(self):
        self.food_count = randint(1, 30)
        if self.food_count > self.house.food:
            self.food_count = self.house.food
        self.house.food -= self.food_count
        self.fullness += self.food_count
        if isinstance(self, Husband):
            cprint('{} съел {} еды.'.format(self.name, self.food_count), color='blue')
        else:
            cprint('{} съела {} еды.'.format(self.name, self.food_count), color='magenta')
        Man.total_food += self.food_count

    def pet_the_cat(self):
        self.happiness += 10
        if isinstance(self, Husband):
            cprint('{} весь день гладил кота.'.format(self.name), color='blue')
        else:
            cprint('{} весь день гладила кота.'.format(self.name), color='magenta')


class Husband(Man):
    total_money = 0
    wot_days = 0

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            dice = randint(1, 4)
            if self.fullness <= 20:
                self.eat()
            elif self.happiness < 20:
                self.gaming()
            elif self.house.money < 20:
                self.work()
            elif dice == 1:
                self.eat()
            elif dice == 2:
                self.work()
            elif dice == 3:
                self.gaming()
            else:
                super().pet_the_cat()

    def eat(self):
        if self.house.food > 0:
            super().eat()
        else:
            cprint('{} голоден, но еда закончилась.'.format(self.name), color='blue')

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        cprint('{} сходил на работу.'.format(self.name), color='blue')
        Husband.total_money += 150

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint('{} играл в танки.'.format(self.name), color='blue')
        Husband.wot_days += 1
        return True


class Wife(Man):
    total_fur_coat = 0

    def __init__(self, name):
        super().__init__(name=name)
        self.dirt_count = 0

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            dice = randint(1, 5)
            if self.fullness <= 20:
                self.eat()
            elif self.happiness <= 20:
                if not self.buy_fur_coat():
                    self.pet_the_cat()
            elif self.house.food < 20 or self.house.cat_food < 10:
                self.shopping()
            elif self.house.dirt >= 150:
                self.clean_house()
            elif dice == 1:
                self.eat()
            elif dice == 2:
                self.shopping()
            elif dice == 3:
                if not self.buy_fur_coat():
                    super().pet_the_cat()
            elif dice == 4:
                super().pet_the_cat()
            else:
                self.clean_house()

    def eat(self):
        if self.house.food > 0:
            super().eat()
        else:
            self.shopping()

    def shopping(self):
        if self.house.money >= 60:
            self.fullness -= 10
            self.house.money -= 60
            self.house.food += 50
            self.house.cat_food += 10
            cprint('{} сходила в магазин за продуктами.'.format(self.name), color='magenta')
        else:
            cprint('{} хотела сходить в магазин за продуктами, но денег не хватило.'.format(self.name), color='magenta')

    def buy_fur_coat(self):
        if self.house.money >= 400:
            self.fullness -= 10
            self.house.money -= 350
            self.happiness += 60
            cprint('{} купила себе шубу.'.format(self.name), color='magenta')
            Wife.total_fur_coat += 1
            return True
        else:
            return False

    def clean_house(self):
        self.dirt_count = randint(1, 100)
        if self.dirt_count > self.house.dirt:
            self.dirt_count = self.house.dirt
        self.fullness -= 10
        self.house.dirt -= self.dirt_count
        cprint('{} сделала уборку на {} единиц грязи.'.format(self.name, self.dirt_count), color='magenta')


class Child(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.name = name
        self. happiness = 100
        self.food_count = 0

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 2)
        if self.fullness < 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.eat()

    def eat(self):
        self.food_count = randint(1, 10)
        if self.food_count > self.house.food:
            self.food_count = self.house.food
        self.house.food -= self.food_count
        self.fullness += self.food_count
        cprint('Малыш {} съел {} еды.'.format(self.name, self.food_count), color='green')
        Man.total_food += self.food_count

    def sleep(self):
        self.fullness -= 10
        cprint('Малыш {} весь день спал.'.format(self.name), color='green')


class Cat:

    def __init__(self, name):
        self.cat_food_count = 0
        self.name = name
        self.house = None
        self.cat_fullness = 30

    def __str__(self):
        return 'Кот {} - сытость: {}'.format(self.name, self.cat_fullness)

    def move_to_house(self, house):
        self.house = house
        cprint('{} обрел новый дом!'.format(self.name), color='grey', on_color='on_white')

    def eat(self):
        self.cat_food_count = randint(1, 11)
        self.house.cat_food -= self.cat_food_count
        self.cat_fullness += self.cat_food_count * 2
        cprint('{} съел {} единиц кошачего корма.'.format(self.name, self.cat_food_count), color='white')

    def sleep(self):
        self.cat_fullness -= 10
        cprint('{} проспал весь день.'.format(self.name), color='white')

    def soil(self):
        self.house.dirt += 5
        self.cat_fullness -= 10
        cprint('{} весь день драл обои.'.format(self.name), color='white')

    def act(self):
        if self.cat_fullness <= 0:
            cprint('{} сдох...'.format(self.name), color='red')
        else:
            dice = randint(1, 3)
            if self.cat_fullness <= 10:
                self.eat()
            elif dice == 1:
                self.sleep()
            elif dice == 2:
                self.eat()
            else:
                self.soil()


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
barsik = Cat(name='Барсик')
serge.move_to_house(house=home)
masha.move_to_house(house=home)
barsik.move_to_house(house=home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    barsik.act()
    cprint(serge, color='yellow')
    cprint(masha, color='yellow')
    cprint(kolya, color='yellow')
    cprint(barsik, color='yellow')
    home.dirt += 5
    cprint(home, color='cyan')
cprint('================== Итог ==================', color='red')
cprint('Всего заработано денег: {} | съедено еды: {} | куплено шуб: {}'.format(
    Husband.total_money, Man.total_food, Wife.total_fur_coat), color='cyan')
cprint('{} играл в танки {} дней'.format(
    serge.name, Husband.wot_days), color='cyan')