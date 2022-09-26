# Напишите программу которая будет на вход принимать число N и выводить числа от -N до N.



# n = int(input("Enter number "))
# num = -n
# while (num <= n):
#     print(num, end = " " )
#     num += 1

# ИЛИ ТАК 

# n = int(input("Enter number "))
# for i in range (-n,n + 1):
#     print(i, end= " ")

# Либо вот так 

print ("Enter number")

value = int(input())

print(list (range(- value, value+1)))
