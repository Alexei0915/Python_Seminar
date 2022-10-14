# Дан список,вывести отдельно буквы и цифры.

inp_string = list (map (str, input('Введите строку').split()))
res_digit = [i for i in inp_string if i.isdigit()==True]
res_letters=[i for i in inp_string if i.isdigit()==False]
print (res_digit,"\n",res_letters)


# a = ["4","4","5","hola"]
# b = ["hola"]
# c = ["4","4","5"]

# b = filter(str.isalpha, a)
# c = filter(str.isdigit, a)

# print(*b)
# print(*c)
