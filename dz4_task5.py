# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('File2.txt', 'w',) as file:
    file.write('2*x^2 + 5*x^5')
with open('File2_2.txt', 'w',) as file:
    file.write('23*x^4 + 9*x^6')

with open('File2.txt','r') as file:
    poly_1 = file.readline()
    polynomial = poly_1.split()


with open('File2_2.txt','r') as file:
    poly_2 = file.readline()
    polynomial2 = poly_2.split()

print(f'{polynomial} + {polynomial2}')
sum_poly = polynomial + polynomial2

with open('sum.txt', 'w',) as file:
    file.write(f'{polynomial} + {polynomial2}')