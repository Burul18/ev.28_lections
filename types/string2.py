# str
# ''
# 'Hello'
# str(5)

# print(dir(str))
# print(dir(int))

# a = 'Hello'
# b = 'John'
# # print(a != b)
# # print('abc' == 'abc')

# print(a > b)
# print(a < b)

# print('a') #97 -> 1100001
# print('a' > 'b')
# print('h' > 'c')

# print('hello' > 'harry') #true
# print('abc' > 'abc') #false

# a = 'Hello'
# b = 'john snow'
# # len()- возрващает кол-во символа в строке
# print(len(a) < len(b))
# print(len(a), len(b))

# <, >, ==, !=, <=, >=

# Методы строк
# replace(old, new, [count] - меняет в строке символы old на new, если вы укажете count, то заменит count раз)

# text = 'ha ha ha ha ha'
# result = text.replace('a', 'e', 2)
# print(result)
# print(f'result after replace: {result}')

# str1 = 'Hello world! My name is John Snow!'
# res = str1.replace('John Snow', 'Tirion Lanister')
# print(res)

# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))

# print(dir(str))

# isdigit - Проверяют состоит ли наша строка полностью из чисел
# isnumeric
# isdecimal

# num = input(' Vvedite chislo:')
# print(f'Vvedeno chislo?: {num.isdigit()}')

# num = input('Vvedite chislo:')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5}')
# else:
#     print('Vy vveli ne chisla!')

# text = '/u0031'
# print(text)
# print(text.isdigit())
# print(text.isnumeric())
# print(text.isdecimal())

# isalnum() -> проверяет состоит ли наша строка из чисел символов латинского алфавита и киррилицы

# str1 = '56ㅓㅕㅗ'
# print(str1.isalnum())
# str2 = '56_d'
# print(str2.isalnum())

# isalpha() -> состоит ли наша строка полностью из символов алфавита

# text = 'Hello world'
# res = text.replace(' ', '')
# print(res)
# print(res.isalpha())

# islower() -> 
# isupper()
# istitle()

# str1 = 'Is'
# print(str1.islower())
# print(str1.isupper())
# print(str1.istitle())

# index(value, [start], [end]) - выводит индекс значения value, которые мы передаем в нашей строке.

# text = 'Hello'
# print(text.index('l', 3))

# text = 'Hello john snow'
# print(text.index('john'),2, 5)

# text = 'Hello world! My name is John Snow!'
# # print(text.index('o'))
# res = text.index('o')
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)

# count(value, [start]) - считает кол- во вхождений value в нашу строку

# text = 'hello o o o hello'
# print(text.count('o'))
# print(text.count('hello'))
# print(text.count('ojhd'))

# split(separator) - дробит нашу строку на несколько частей по разделителю, все части сохраняюются в типе list

# text = 'Let me speak by my hearth in English! Cause my name is John Snow!'
# res = text.split(' ')
# print(res)
# print(len(res))


# a = 'hello#hello#hello#hello'
# res = a[1:].split('#')
# print(res)

# 'connector'.join(list) -> соединяет по connector строки которые находились в list

# text = 'Let me speak by my hearth in English! Cause my name is John Snow!'
# res = text.split(' ')
# print(res)
# str1 = ' -- '.join(res)
# print(str1)

# find(value, [start], [end]) -> делает тоже самое что и index, но если не нашел то вернется -1

# text = 'Hello'
# print(text.find('l'))
# print(text.find('lytui'), type(text.find('lytui')))
# print('John Snow')

# swapcase()- переводит все символы в протиполодный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello world! JOHN snow'
# # print(f'Original: {text}')
# # print(text.upper())
# # print(text.lower())
# print(text.swapcase())

# capitalize()- переводит самый первый символ в верхний регистр
# title() - переводит первые символы всех слов в верхний регистр

# name = input('Vvedite imya:').capitalize()
# print(name)
# print(f'Hello Mr/Mrs {name}!')

# fio = 'johH edArt snOw'
# print(fio.title())
