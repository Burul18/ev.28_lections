# list() -> (списки, массив) - изменяемый, последовательный тип данных, который представляет из себя коллекцию каких- либо обьектов(значения).

# my_list = [1, 'str', False, True, None, [1, 2, 3, 4, 5]]
# print(my_list, type(my_list))

# range() - возвращает последовательность элементов(чисел)
# ls = range(1, 101)
# my_list = list(ls)
# print(my_list)

# list()

# my_list = list('Hello world!')
# # print(my_list)

# tuple_ = ('banana' , 'apple', 'cherry')
# print(tuple_, type(tuple_))
# ls = list(tuple_)
# print(ls, type(ls))

# Индексация в списках 
# ls = [1, 2, 3, 4, 5, 'str', [True, False, None]]
# print(ls, len(ls))
# print(ls[1], ls[2])
# print(ls[4:])
# print(ls[2:4])

# ls = [1, 2, 3, 4, 5, 'str', [True, False, None], 4, 5, 6]
# print(ls[6][:2])
# print(ls[5])

# i = 0
# while i < 5:
#     print(i)
#     i +=1

# ls = list(range(1, 11))
# print(ls)
# for num in ls:
#     print(num)

# ls = ['John', 'Sansa', 'Tririon', 'Eddart', 'Serseya', 'Jamie']
# print(ls, len(ls))
# for x in ls:
#     print(f'Hello, Mr/Mrs {x}! Welcome to the club!')

# #     print('1')

# # print('2')

# ls -> 1, 21 - четных чисел - квадрат числа
#               нечетных чисел - куб числа

# ls = list(range(1, 21))
# for num in ls:
#     if num % 2 == 0:
#         print(f'chislo chetnoe {num}, kvadrat {num ** 2}')
#     else:
#         print(f'nenchetnoe chislo {num}, kub {num ** 3}')

# *************
# методы списков
# print(dir([]))

# append(element) - добавляет элемент в конец списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# # ls.append('Hello')
# ls.append([True, False, None])
# ls.append('Hello')
# print(ls)

# extend(object) - расширяет список
# ls = [1, 2, 3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# ls,extend(str(56))
# ls.extend([1, 2, 3])
# print(ls)

# ls = [1, 2, 3]
# ls1 = [4, 5, 6]
# print(ls + ls1)

# sort() - сортирует список, если передать reverse = True, то список отсортируется в убывающем порядке

# from random import randint
# ls = []
# for x in range (0, 100):
#     num = randint(0, 1000)
#     ls.append(num)

# print(ls)
# # ls.sort()
# ls.sort(reverse = True)
# print('After')
# print(ls)

# ls = ['John', 'Burul', 'Hello', 'Bye']
# ls.sort()
# # ls.sort(key = len)
# print(ls)

# # insert(index, element) - добавляет элемент по указанному index
# ls = ['str', 2, 3, False]
# ls.insert(2, 15)
# print(ls)

# remove(element) - удаляет элемент из списка, если такого нет, то выводится ошибка
# pop(index) - удаляет и возвращаяет элемент из списка по index, но если index не передать, удаляет последний элемент

# ls = [5, 1, 2, 4, 4, 5, 5, 5]
# # ls.remove(5)
# # print(ls)
# # print(5 in ls)
# while 5 in ls:
#     ls.remove(5)

# print(ls)

# while 4 in ls:
#     ls.remove(4)

# print(ls)

# ls = [5, 1, 2 , 4, 5, 5]
# # print(ls.pop(0))
# # # print(ls)
# # print(ls.remove(5))
# deleted = ls.pop()
# print(ls)
# print(deleted)

# update**********************************

# ls = [1, 'h', 3]
# print(ls)
# ls[1]= 2
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza:
#     if not x.startswith('f'):
#         spisok.append(x)

#     print(spisok)
