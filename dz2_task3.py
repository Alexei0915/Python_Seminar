# Задайте список из n чисел 
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите чмсло : ')) 

def seq(n):
  return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(seq(n))
print(round(sum(seq(n))))
