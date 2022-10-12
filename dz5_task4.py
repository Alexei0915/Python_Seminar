# 
# def encode(s):
 
#     encoding = "" # сохраняет выходную строку
 
#     i = 0
#     while i < len(s):
#         # подсчитывает количество вхождений символа в индексе `i`
#         count = 1
 
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
 
#         # добавляет к результату текущий символ и его количество
#         encoding += str(count) + s[i]
#         i = i + 1
 
#     return encoding
 
 
# if __name__ == '__main__':
 
#     s = 'dgfdbdzfdzbzdbzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
#     print(encode(s))
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W

with open('Gb.txt', 'w') as data:
    data.write('HHHHhwdawdqwdfsdsdsdsdaaadwllllllaaaaammmmaaaaaannn')

with open('Gb.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded):
    encoded = ''
    count = 1
    char = decoded[0]
    for i in range(1, len(decoded)):
        if decoded[i] == char:
            count += 1
        else:
            encoded = encoded + str(count) + char
            char = decoded[i]
            count = 1
            encoded = encoded + str(count) + char
    return encoded


def rle_decode(encoded):
    decoded = ''
    char_amount = ''
    for i in range(len(encoded)):
        if encoded[i].isdigit():
            char_amount += encoded[i]
        else:
            decoded += encoded[i] * int(char_amount)
        char_amount = ''
    print(decoded)

    return decoded


with open('Gb.txt', 'r') as file:
    decoded = file.read()

with open('deco.txt', 'w') as file:
    encoded = rle_encode(decoded)
    file.write(encoded)

print('Decoded : \n' + decoded)
print('Encoded : \n' + rle_encode(decoded))
