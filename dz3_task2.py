# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randrange


num = int(input('Введите размер списка '))
list = []
list1 = []

for i in range(num):
    list.append(randrange(0,9))

for i in range(len(list)):
    while i < len(list)/2 and num > len(list)/2:
        num = num - 1
        a = list[i] * list[num]
        list1.append(a)
        i += 1

print(list)
print(list1)