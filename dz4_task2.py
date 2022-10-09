#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2 # первое простое число
li = []
num1 = num
while i <= num:
    if num % i == 0:
        li.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f" множители числа {num1} приведены в списке: {li}")

# def check_number_simple(n: int):
#     i = 2
#     while n % i != 0 or i == n - 1:
#         i += 1
#     if i == n:
#         return n

# def fill_simple_list(n: int) -> list:
#     s_list = [1]
#     for i in range(2, n+1):
#         if n % i == 0:
#             if check_number_simple(i) != None:
#                 s_list.append(check_number_simple(i))
#             else:
#                 continue
#     return s_list


# n = int(input('Введите натуральное число N: '))
# s_list = fill_simple_list(n)
# print(s_list)