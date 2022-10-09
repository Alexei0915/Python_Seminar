# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint
import itertools

k = randint(2, 7)

def get_coefficient(k):
    coefficient = [randint(0, 10) for i in range (k + 1)]
    while coefficient[0] == 0:
        coefficient[0] = randint(1, 10) 
    return coefficient

def get_polynomial(k, coefficient):
    var = ['*x^']*(k-1) + ['*x']
    poly = [[a, b, c] for a, b, c  in itertools.zip_longest(coefficient, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in poly:
        x.append(' + ')
    poly = list(itertools.chain(*poly))
    poly[-1] = ' = 0'
    return "".join(map(str, poly)).replace(' 1*x',' x')


coefficient = get_coefficient(k)
polynomial = get_polynomial(k, coefficient)
print(polynomial)

with open('File2.txt', 'w') as data:
    data.write(polynomial)


# # Второй многочлен для второго файла,следующей задачи 

k = randint(2, 5)

coefficient = get_coefficient(k) 
polynomial2 = get_polynomial(k, coefficient)
print(polynomial2)

with open('File2_2.txt', 'w') as data:
    data.write(polynomial2)