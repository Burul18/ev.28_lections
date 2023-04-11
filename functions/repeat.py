# Decorators
# Scope
# Built in functions

# Декораторы - функция высшего порядка (функция которая принимает 
# другую функцию в качестве аргумента)

# def decorator(func):
#     def wrapper():
#         print(f'this function named {func.__name__}')
#         return func()
#     return wrapper

# @decorator
# def hello():
#     print('Hello')

# hello()

# def sq(func):
#     def wrapper(num):
#         nums = func(num)
#         return list(map(lambda x : x ** 2, nums))
#     return wrapper

# @sq
# def func(num: int):
#     return list(range(1, num))

# @sq
# def func2(num):
#     return list(range(1, num, 2))

# print(func(5))
# print(func2(6))

# first_size = 100

# def second():
#     second_size = 50
#     global first_size
#     first_size += second_size
#     def third():
#         third_size = 25
#         global first_size
#         first_size += third_size
#     third()

# second()
# print(first_size)

# sogl = 'бвгджзйклмнпрстфхцчшщ'
# glas = 'аеёиоуэюя'

# def let_count(word: str):
#     res_sogl = 0
#     res_glas = 0
#     res_another = 0
#     for letter in word:
#         if letter in sogl:
#             res_sogl += 1
#         elif letter in glas:
#             res_glas += 1
#         else:
#             res_another += 1
#     return res_sogl, res_glas, res_another

# print(let_count('привет'))



