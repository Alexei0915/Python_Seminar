# Вычислить число c заданной точностью d. 
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

from math import pi

d =  int(input("Введите число для заданной точности числа π:"))
print(f'число π с заданной точностью {d} = {round(pi, d)}')
