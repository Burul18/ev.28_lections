# num1 = 1

# while num1 >= 0:
#     num1 = input('Vvedite chislo:') 
#     if num1[0] == '-' and num1[1:].isdigit():
#         num1 = int(num1)
#     else:
#         num1 = 1

# print('vstretilsya otricatelnoe chislo!')

# """""""""
# from random import randint
# ls = []
# for x in range(0, 100):
#     ls.append(randint(0, 100))


# ls.sort()
# print(ls, len(ls))

# res = []
# for x in ls:
#     if x not in res:
#         res.append(x)
# print(res, len(res))

''''''''
'''
Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на в
торую одним ходом.Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки. Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.
Вводить в порядке x1, y1, x2, y2
'''


# x1 = int(input('Vvedite 1 coordinatu gde stoit ladya:'))
# y1 = int(input('Vvedite 2 coordinatu gde stoit ladya:'))
# ladya = [x1 , y1] #2, 5

# x2 = int(input('Vvedite 1 coordinatu kuda idet ladya:'))
# y2 = int(input('Vvedite 2 coordinatu kuda idet ladya:'))
# target = [x2 , y2] # 4, 6

# if x1 == x2 or y1 == y2:
#     print(True)
# else:
#     print(False)

# """""""""""""""""""
# import random

# ls = ['plov', 'besh-barmak', 'kuurdak', 'oromo', 'lagman']
# p = 0
# b = 0
# k = 0
# o = 0
# l = 0

# for x in range(0, 1_000_000):
#     meal = random.choice(ls)
#     # print(meal)
#     if meal == 'besh-barmak':
#         b += 1
#     elif meal == 'plov':
#         p += 1
#     elif meal == 'kuurdak':
#         k += 1
#     elif meal == 'oromo':
#         o += 1
#     else:
#         l += 1

# print('Resultaty golodnayx igr:')
# print(f'plov: {p}\nbesh-barmak: {b}\nkuurdak: {k}\noromo: {o}\nlagman: {l}')    

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.


# 1) nums = [2, 7, 11, 15]
# target = 9
# 0, 1 """""""""" 2+ 7 = 9

# 2) nums = [4, 11, 2, 5, 1, 6]
#  target = 8
# # 2, 5 """""""""" 2 + 6 = 8

# nums = [2, 7, 11, 15]
# target = 9


# for x in range(0, len(nums)):
#     num = target - nums[x]
#     if num in nums:
#         print(f'Otvet: {x}, {nums.index(num)}' )
#         break

# nums = [4, 11, 2, 5, 1, 6]
# target = 8

# for x in range(0, len(nums)):
#     num = target - nums[x]
#     if num in nums:
#         if num != nums[x]:
#             print(f'Otvet: {x}, {nums.index(num)}')
#         break

# words = ['John', 'Ono', 'kazak', 'peter', 'dovod', 'radar', 'apa', 'piko']

# def get_polindrom(words):
#     result = []
#     for i in words:
#         if i.lower() == i[::-1].lower():
#             result.append(i)
#     return result

# polindrom_words = get_polindrom(words)
# print(polindrom_words)

'''Напишите функцию которая будет возвращать ваш депозит через определенное время с процентом 10%, возвращать фин количество денег.'''

# def get_percenage(money, period):
#     if money < 30_000:
#         raise ValueError('Вложить можно более 30000')
#     if period < 3:
#         raise ValueError('Период должен быть не менее 3 лет')
#     year = 0
#     while year < period:
#         money += money * 0.1
#         year += 1
#     return money

# try:
#     money = float(input('Введите сумму вложения: '))
#     period = int(input('Введите период: '))
#     print(get_percenage(money, period))
# except ValueError:
#     print('Неправиоьный ввод!')

# def test_func(a, b):
#     pass

# test_func(1, 4)

# def range(first, last, step):
#     pass

# print(list(range(1, 4)))




# list_= list(i for i in range(1, 50) if i % 2 !=0)
# print(list_)

# list_ = list(i for i in range(1, 26)  i ** 2 )
# print(list_)

a = ("топот", "комок", "Оно")

def is_polindrome(a):
    for i in a:
        if i() == i[::-1]():
          print('True')
        else:
          print('False')

is_polindrome(a)