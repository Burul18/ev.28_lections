# """"""
# 1) Мурат с друзьями на выходных решил собраться и пойти в ночной клуб.
# Но в ночной клуб пропускают только тех, кому 17+.
# Мурату - 24 года, Эржану - 21 год, Карине - 24 года, Алтынай - 17 лет, Айбеку - 16 лет.
# Напишите программу, которая определяет кого пустить в ночной клуб, а кого нет. (работа со словарем)
# """


# dict_ = {'Murat': 24, 'Erjan': 21, 'Karina': 24, 'Altynai': 17, 'Aibek': 16}

# for i in dict_:
#     if dict_[i] >= 17:
#         print(f' {i} You can come in')
#     else:
#         print(f'{i} You cannot come in')
    
# print(dict_)

# ~~~~~~~~~~

# for i, j in dict_.items():
#     if j >= 17:
#         print(f' {i} You can come in')
#     else:
#         print(f'{i} You cannot come in')


"""
1) Мурат с друзьями на выходных решил собраться и пойти в ночной клуб.
Но в ночной клуб пропускают только тех, кому 17+.
Мурату - 24 года, Эржану - 21 год, Карине - 24 года, Алтынай - 17 лет, Айбеку - 16 лет.
Напишите программу, которая определяет кого пустить в ночной клуб, а кого нет. (работа со словарем)
"""
# # #писать код здесь
# dict_ = {'Murat': 24, 'Erjan': 21, 'Karina': 24, 'Altynai': 17, 'Aibek': 16}
# print(dict_)


"""
2) Дан словарь а, значениями которого являются словари,
измените словарь 'а' таким образом, чтобы значения внутреннего словаря стали 
внешними значениями

a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

Вывод:
{'a': 32, 'b': 36, 'c': 37, 'd': 21}
"""
#писать код здесь

# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# #key -> 'a'
# b = {}
# for key, value in a.items():
#     for i_in, j_in in value.items():
#         b[key] = j_in
# print(b)


"""
3) Создайте словарь, где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
"""
# писать код здесь


# dict_ = {'apricot': 120, 'limon': 125, 'apple': 100, 'banana': 130}
# print(dict_)
# for i in dict_.copy():
#     if dict_[i]%2 == 0:
#         dict_.pop(i)
# print(dict_)



"""
4) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.
"""
# # писать код здесь
# dict_ = {'apricot': 120, 'limon': 125, 'apple': 100, 'banana': 130}
# print(dict_)
# total = 0
# for i in dict_.values():
#     total += i

# print(total)

"""
5) Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.
"""
# писать код здесь

# dct = {}

# for i in range(1, 10):
#     dct[i] = i**2
# print(dct)


"""
6) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
"""
# писать код здесь

# dct = {'first': {'a': 1}, 'second': {'b': 2}}
# s = {}
# for key, value in dct.items

"""
7) Дан словарь dict_. Отсортируйте словарь по значениям в порядке уменьшения.
Новые элементы занесите в словарь sorted_dict

dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {}

Вывод:
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
"""
# писать код здесь

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_ = sorted(dict_.values())
# print(sorted_)
# sorted_dict = {}
# print(sorted_)
# for i in sorted_:
#     print(dict_[key])
#     for key in dict_:
#         if dict_[key] == i:
#             sorted_dict[key] = dict_[key]
#             break
# print(sorted_dict)


"""
8) Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то запринтите исключение с текстом "Сумма не может быть отрицательной!"
"""
# писать код здесь
# a = int(input('Введите сумму, которая у вас сейчас есть в бумажнике: '))
# if a >= 0:
#     print('')print(f'У вас {a} денег')
# else:
#     print('Сумма не может быть отрицательной!')

# res =[]
# size = 3
# for  i in range(1, size + 1):
#     grid = []
#     for j in range(1, size + 1):
#         grid.append(j)
#     res.append(grid)
# print(res)


# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

# max_list = max(lists, key = len)
# min_list = None
# if lists:
#     min_list = min(lists, key = len)
# if max_list == min_list:
#     min_list = None
# print(f'max_list {max_list}') 
# print(f'min_list {min_list}')

# Таблица умножения


# print('Таблица умножения')
# for i in range(1, 10):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i * j}\t', end = ' ')

# count = 0
# number = input('Vvedite chislo: ')
# print(type(number))

# a = int(input(''))
# b = int(input(''))
# c = int(input(''))
# print(a, b, c)
# # print(b)
# # print(c)
# if a + b > c:
#     print(f'{a}{b}{c}yes')
# else:
#     print('no')

# a = int(input(''))
# b = int(input(''))
# c = int(input(''))
# if a ** 2 == (b** 2 + c ** 2):
#     print('rectangular')
# elif a ** 2 < (b ** 2 + c ** 2):
#     print('acute')
# elif a ** 2 > (b ** 2 + c ** 2):
#     print('obtuse')
# else:
#     print('impossible')