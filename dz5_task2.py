# Задача №38: Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"


def input_amount(name):
    x = int(input(f'{name},введите колличество конфет,которое берете от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f"{name},введите колличество согласно правилам игры: "))
    return x
def gamer_output (name,amount,counter,balance):
    print(f'ходил {name},взял {amount},на счету {counter},на столе осталось {balance}')
gamer1 = input ("Введите имя игрока 1 > ")
gamer2 = input ("Введите имя игрока 2 > ")
balance = int(input("Введите колличество конфет на столе > "))
turn = (0,2)
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
        gamer_output(gamer1,amount,counter1,balance)
    else:
        amount = input_amount(gamer2)
        counter2 += amount
        balance -= amount
        turn = True
        gamer_output(gamer2,amount,counter2,balance)
if turn:
    print(f'WINNER >{" "}"{gamer1}"')   
else:
    print(f'WINNER >{" "}"{gamer2}"')

