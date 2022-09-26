# Напишите программу которая будет на вход принимать число N и выводить числа от -N до N.



# n = int(input("Enter number "))
# num = -n
# while (num <= n):
#     print(num, end = " " )
#     num += 1

n = int(input("Enter number "))
for i in range (-n,n + 1):
    print(i, end= " ")