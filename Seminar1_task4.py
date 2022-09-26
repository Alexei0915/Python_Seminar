# Напишите программу которая будет принимать на вход дробь и показывать
# первую чифру дробной части  числа.

# import math


# a = float(input(" Введите число >  "))
# num_result = a * 10
# if num_result % 10 == 0:
#     print("Введите дробь")
# else:
#     print(math.floor(num_result) % 10)

# Либо 


# f = float(input())
# d = int((f*10) % 10)
# print(f, d, sep="->")

# Или так

result1 = float(input(" Введите число >  "))
result = int((result1 * 10)% 10)
print(result1, int (result1), result1- int (result1))
# проверка для определения имеет число дробную часть или нет (из вещественного в натуральное)