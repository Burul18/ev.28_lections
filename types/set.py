# Set - Множества
# Это изменяемый неупорядочный, итерируемый

# неиндексируемый тип данных
# множества хранят в себе только неизменяемые типы данных

# 1 -> set()
# a = set([1, 2, 3, 4])
# print(a)

# a = set({1: 2, 3: 4})
# print(a)

# 2 - {}
# set2 = {1, 2, 4}
# print(set2)

# set1 = {1, 2, 2, 2, 2, 3}
# print(set1)

# frozenset - неизменяемое множество
# a = frozenset([1, 2, 3, 4, 5])
# # a.add(7)
# print(a)

# set1 = {1, }
# print(type(set1))

# set1 = {1, 0, True, False}
# print(set1)

# a = 0
# print(bool(a))

# Методы SET 

# add -> для добавления 

# set1 = {1, 2, 3}
# # set1.add(4)
# # print(set1)
# # set1.add((1, 2, 3, 4, 5))
# # set1.add((1, 2, 3, 4, 5))
# # print(set1)

# # update / он может добавлять, но не повторяя имеющееся, добавляет все итерируемые

# set1.update({3: '1', 4: '5'})
# print(set1)
# set1.update('string', {1, 2, 3, 4, 5, 6, 7})
# print(set1)

# set1.update([1, 2, 3, 45, 6])
# print(set1)

# Удаление в set
# # clear - очищает все множества
# remove(element) - удаляет элемент, если его нет выдает ошибку
# discard(element) - Если элемента нет ничего не происходит
# pop() - удаляет из set (FIFO) first in first out

# set1 = {1, 2, 3, 4, 5}
# # # set1.remove(9)
# # # set1.clear()
# # # set1.discard(5)
# set1.update('string')
# print(set1.pop())
# print(set1)
# print(set1.pop())
# print(set1)

# difference - выводит отличие
# set1 = {1, 2, 3, 4}
# set2 = {2, 5, 3, 7}
# print(set2.difference(set1))
# print(set1.difference(set2))
# # print(set1 - set2)

# print(set1.symmetric_difference(set2))
# print(set1^set2)

# set1.symmetric_difference_update(set2)
# print(set1)

# print(set1.intersection(set2))
# print(set1 & set2)
# print(set1.union(set2))
# print(set1 | set2)

# Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором

# set1 = {1, 2, 3, 4}
# set2 = {2, 4, 5, 6, 7}
# print(set2.difference(set1))


# Нужно проверить, все ли числа в последовательности уникальны

# num = list(input())
# print(len(num) == len(set(num)))

# tuple - неизменяемый, индексируемый, итерируемый, упорядочный тип данных
# index(element) - возвращает индекс этого элемента в кортеж
# литералы ()
# a = (True, 'a', 1, 1, 1, 1)
# # print(a, type(a))
# b = tuple()
# print(a.index(True))

# # count(element) - возвращает число вхождения этого элемента в кортеж

# # print(a.count(1))

# string = 'Python is the best'
# print(string.find('Python'))

