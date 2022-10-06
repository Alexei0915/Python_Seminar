# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), 
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

# Формат входных данных
# В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки,
#  содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
# Формат выходных данных:
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
# примеры:
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# """

a = 'anton'

def find_word_in_string(input_string: str, word: str) -> bool:
    string = input_string
    res = ''
    word = word
    list_el = []
    for indx in range(len(word)):
        if string.find(word[indx]) != -1:
            list_el.append(word[indx])
            string = string[string.find(word[indx]):]
    res = ''.join(list_el)
    # print(res)
    # print(res == word)
    return res == word


def test_find_word_in_string():
    result = find_word_in_string('osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen', 'anton')
    assert result == True, f'Wrong answer: {result} = Test_1'
    result = find_word_in_string('anton', 'anton')
    assert result == True, f'Wrong answer: {result} = Test_1'
    result = find_word_in_string('aoooooooooontooooo', 'anton')
    assert result == False, f'Wrong answer: {result} = Test_1'
    result = find_word_in_string('elelelelelelelelelel', 'anton')
    assert result == False, f'Wrong answer: {result} = Test_1'
    result = find_word_in_string('253235235a5323352n25235352t253523523235oo235523523523n', 'anton')
    assert result == True, f'Wrong answer: {result} = Test_1'
    result = find_word_in_string('antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'anton')
    assert result == True, f'Wrong answer: {result} = Test_1'
    print('All Tests => OK !!!')


if __name__ == '__main__':
    test_find_word_in_string()
  