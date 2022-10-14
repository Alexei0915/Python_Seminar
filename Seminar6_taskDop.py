# Вводится список целых чисел в одну строку через пробел.Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции (filter).
# Результат отобразить на экране в виде последовательности оставшихся чисел через пробел.

# sequence = list(map(int,input("Введите список целых чисел через пробел").split()))
# ok =list(filter((lambda x: True if 9 < x < 100 else False),sequence))
# print(ok)

# data =[1,2,3,4,5,555,555,666,22,111]
# result = list(filter(lambda x:9 < x < 100,data))
# print(result)

print(*list(filter(lambda x: len(str(abs(int(x)))) == 2, input().split())))