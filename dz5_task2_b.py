# intelligence bot
from random import randrange

def input_amount(name):
    x = int(
        input(f'{name},введите колличество конфет,которое берете от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f"{name},введите колличество согласно правилам игры: "))
    return x


def gamer_output(name, amount, counter, balance):
    print(
        f'ходил {name},взял {amount},на счету {counter},на столе осталось {balance}')

def intelligence(balance):
    amount = randrange(1,29)
    while balance-amount <= 28 and balance > 29:
        amount = randrange(1,29)
    return amount


gamer1 = input("Введите имя игрока 1 > ")
gamer2 = "Bot"
balance = int(input("Введите колличество конфет на столе > "))
turn = randrange(0,2)
if turn:
    print(f"очередь игрока 1 {gamer1}")
else:
    print(f"очередь игрока 2 {gamer2}")
counter1 = 0
counter2 = 0
while balance > 28:
    if turn:
        amount = input_amount(gamer1)
        counter1 += amount
        balance -= amount
        turn = False
        gamer_output(gamer1, amount, counter1, balance)
    else:
        amount = intelligence(balance)
        counter2 += amount
        balance -= amount
        turn = True
        gamer_output(gamer2, amount, counter2, balance)
if turn:
    print(f'WINNER >{" "}"{gamer1}"')
else:
    print(f'WINNER >{" "}"{gamer2}"')
