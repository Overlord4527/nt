import time
import random

class Resident:
    def  __init__(self, name):
        self.name = name
        self.hunger = 60
        self.energy = 80
        self.shans = 0
        self.is_alive = True
        self.obmorok = False

    def live_day(self):
        if self.obmorok:
            self.energy += 15
            print(f"{self.name} спит без чувств")
            if self.energy >= 30:
                self.obmorok = False
                print(f"{self.name} пришел в себя")
        else:
            self.hunger -= 15
            self.energy -= 15
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False
            print(f'Your chel is 💀')


    def status(self):
        return f'{self.name} | Hunger: {self.hunger} | Energy: {self.energy}'

    def react_to_mess(self):
        if not self.obmorok:
            pass

class RobotSim(Resident):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print('Робот заряжается')
        self.energy += 100
        time.sleep(1)

    def react_to_mess(self):
        print(f'Мусор обнаружен, начинаю уборку')
        self.energy -= self.energy / 100 * 30

class Worker(Resident):
    def __init__(self, name, money):
        super().__init__(name)
        self.money = money

    def work(self):
        print(f'{self.name} is working on two works, he will got 150 dollars')
        self.money += 150
        self.energy -= 40
        self.hunger -= 20

    def react_to_mess(self):
        print(f'{self.name}: Опять мусор (-20 happinies)')
        self.energy -= 10

class Lazy(Resident):
    def __init__(self, name):
        super().__init__(name)
        self.lazyies = 100

    def live_day(self):
        self.hunger -= 5
        self.energy -= 5
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False
            print(f'Your chen is 💀')

    def sleep_on_trash(self):
        print(f'{self.name} is sleeping on trash')
        self.energy += 40
        self.hunger -= 5

    def react_to_mess(self):
        print(F'{self.name} is happy trash')

p1 = Resident('player1')
robot = RobotSim('Morph')
worker = Worker('Arthur (Worker)', 100)
lazy = Lazy('Larry (Lazzier)')
roommates = [worker, lazy, robot]

day = 1
is_messy = True
print('Simulate was started')

while True:
    print(f'\n=== Day {day} ===')

    if not all(r.is_alive for r in roommates):
        dead = next(r for r in roommates if not r.is_alive)
        print('Game over')
        break

    print('arthur money:',  worker.money, '$')
    for r in roommates:
        print(r.status())

    print('Ваш выбор')
    print('1 Артур пойти на рабато +150$')
    print('2 Артур купить пиццу на всех -50$')
    print('3 Ларри поспать в куче хлама +энергия')
    print('4 Ларри Попросиьт у артура денег на еду')
    print('5 Убратся в комнате Артур тратит энергию')
    print('6 Зарядить робота')
    print('7 Устроить вечеринку (-100$)')
    print('0 Выход')

    choice = input('Действие: ')

    if choice == '1':
        if worker.obmorok:
            print("Артур в обмороке и не может работать!")
        else:
                worker.work()
                p1.shans += 1
                if random.randint(p1.shans, 10) == 10:
                    is_messy = True
                    print('Артур попроботал и в доме появился мусор!')
    elif choice == '2':
        if worker.obmorok:
            print("Артур в обмороке и не может заказать пиццу!")
        else:
            if worker.money >= 50:
                worker.money -= 50
                for r in roommates:
                    r.hunger = min(100, r.hunger + 40)
                print('Pizza was ordered! All ate')
                p1.shans += 1
                if random.randint(p1.shans, 10) == 10:
                    is_messy = True
                    print('Все поели и в доме появился мусор!')
            else:
                print('No money for pizza')
    elif choice == '3':
        if worker.obmorok:
            print("Лари в обмороке и не может заснуть еще раз!")
        else:
            if is_messy== True:
                lazy.sleep_on_trash()
            else:
                print('There are no trash')
                lazy.energy += 10
    elif choice == '4':
        if worker.obmorok:
            print("Лари в обмороке и не может попросить денег!")
        else:
            print(f'Larry wants money form arthur, arthur is angry')
            worker.energy -= 5
    elif choice == '5':
        if worker.obmorok:
            print("Артур в обмороке и не может убираться!")
        else:
            print('arthut throwed out 40 bags of trash')
            is_messy = False
            worker.energy -= 30
    elif choice == '6':
        if worker.obmorok:
            print("Робот в обмороке и не может заряжаться!")
        else:
            robot.eat()
    elif choice == '7':
        print('Вечеринка в разгаре(+20 энергии у Артура и Лари)')
        worker.energy += 20
        lazy.energy += 20
        is_messy = True
        worker.money -= 100

    elif choice == '0':
        break

    print('\n Night in flat')
    time.sleep(1)

    for r in roommates:
        r.live_day()
        if is_messy == True:
            r.react_to_mess()

    for r in roommates:
        if r.hunger <= 10:
            print(f'{r.name} на грани голодной смерти')
        if r.energy <= 5:
            print(f'{r.name} упал в обморок и восстанавливает энергию')

    day += 1
    print(p1.shans)

print('Game Closed')
