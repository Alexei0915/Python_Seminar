# Задайте список. Напишите программу,которая определяет
# присутсвует ли в заданном списке строк некое число.

array = ['heiufheuifddsd5458ads225d0915']
num = 915
for word in array:
    if str(num) in word:
        print(True)
    else:
        print(False)