# list comprehensions - это генераторы списков 

# list comprehensions - упрощенный подход к созданию списков, который задействует в себе цикл for, 
# а так же конструкция if для определения того, что в итоге попадает в наш список

# list -> 0- 200 -> num % 2 == 0

# ls = []
# for i in range(0, 201):
#     if i % 2 == 0:
#         ls.append(i)

# print(ls)


# ls = [x for x in range(0, 201) if x % 2 != 0]
# print(ls)

# list: 0 -300 -> num % 2 == 0, num % 3 == 0

# ls = []
# for i in range(0, 301):
#     if i % 2 == 0 and i % 3 == 0:
#         ls.append(i)

# print(ls)

# ls =[i for i  in range(0, 300) if i % 2 == 0 and i % 3 == 0]
# print(ls)

# list: 0-100 -> x % 2 == 0 : x ** 2, x % 3 == 0: x ** 3 

# ls = []
# for i in range(0, 101):
#     if i % 2 == 0:
#         ls.append(i ** 2)
#     elif i % 3 == 0:
#         ls.append(i ** 3)
# print(ls)


# print(5 if input() == 'yes' else 7)

# ls = [i ** 2 if i % 2 == 0 else i ** 3  for i in range(0, 101) if i % 2 == 0 or i % 3 == 0]
# print(ls)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# new_list = [expression for item in iterable <if condition == True>]

# ls = [str(i * 2) for i in range(0, 11)]
# print(ls)

# ls = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
# # result = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# res = []
# for i in ls:
#     for item in i:
#         res.append(item)
# print(res)

# ls = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
# res = [item for x in ls for item in x]
# print(res)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# from datetime import datetime

# start = datetime.now()
# ls = [x for x in range(0, 100_000_000)]
# # ls = []
# # for i in range(0, 100_000_000):
# #     ls.append(i)
# finish = datetime.now()
# print(finish - start)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# set comprehensions
# set_ = {x for x in range(1, 100)}
# print(set_, type(set_))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# dict comprehensions
# dict_ = {
#     key: value,
#     key: value

# }

# dict_ = {x: x ** 2 for x in range(0, 16)}
# print(dict_)

# names = ['John', 'Tirion', 'Eygan', 'Sansa', 'Ramsi']
# dict_ = {x: len(x) for x in names}
# print(dict_)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# dict1 = {
#     'Soke': {'history': 99, 'physic': 95, 'math': 94},
#     'Omoke': {'history': 84, 'math': 86, 'physic': 68},
#     'John': {'history': 100, 'math': 90, 'physic': 87},
# }
# dict2 = {}
# res = {}
# for key, value in dict1.items():
#     # print(key)
#     # print(value)
#     for inner_key, inner_value in value.items():
#         # print(inner_key)
#         # print(inner_value)
#         if max(value.values()) == inner_value:
#             res[key] = inner_key
# print(dict1)

# print(res)

# dict1 = {
#     'Soke': {'history': 99, 'physic': 95, 'math': 94},
#     'Omoke': {'history': 84, 'math': 86, 'physic': 68},
#     'John': {'history': 100, 'math': 90, 'physic': 101},
# }
# res = {key: inner_key for key, value in dict1.items() for inner_key, inner_value in value.items() if max(value.values()) == inner_value}
# print(res)

'''Запросите у пользователя число от 1 до 10 в переменную n. Затем пройдитесь по промежутку 
чисел от 1 до 500(включительно) и запишите в словарь dict_, 
только те числа, которые кратны числу n (делятся на число n без остатка), 
введенное пользователем. Ключом будет само число, а значением его квадрат.'''

# try:
#     n = int(input('Vvedite chislo: '))
# except ValueError:
#     print('Invalid number!')
# else:
#     dict_= {x: x ** 2 for x in range(1, 501) if x % n == 0}
#     print(dict_)



        
