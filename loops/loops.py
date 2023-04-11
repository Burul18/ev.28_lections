# while <expression>
#     # <body>
# i = 0
# while i < 10:
#     i +=  1 # i = i + 1
#     print(f'Цикл сработал {i} раз!')


# ls = list(range(1, 51))
# print(ls.reverse())
# while ls:
#     print(ls.pop())

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'raychel':
#     name1 = input('Vvedite imya1: ')
#     name2 = input('Vvedite imya2: ')
#     print()
    
#     if i >= 5:
#         print('Цикл остановлен!')
#         break
#     i += 1
# else:
#    print('Ты угадал!')

# # '''''''''''
# user = {'username': 'JohnSnow', 'password': 'ilovepythin123'}
# i = 3
# # password = None
# while password != input(f'{user['password']} vvedite parol\':' != user['password']:
#     # password = input(f"{user['username']} Vvedite parol\:")
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany!!')
#         break 
#     else:
#         print(f'{user["username"]} vy uspeshno zashli v sistemu!')

# for <variable> in <iterable object>:
#    #<body>

# ls = [0, 1, 2, 3, 4, 5, 6 , 7, 8 , 9 ]
# i = iter(ls)
# print(i)
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))

# import random

# a = 1, 2, 3
# print(a) 
# print(type(a))
# a, b, c = 1, 2, 3
# print(c, b, a)

# import random
# ls = []
# for x in range(1, 101):
#     ls.append(random.randint(1, 50))

# print(len(ls))
# ls = set(ls)
# ls = list(ls)
# print(ls)
# print(len(ls))

# ls = ['Tirion', 'Bilal', 'John', 'Sansa', 'Jamie', 'Eddart']
# # print(ls)
# for x in ls:
#     if x == 'Bilal':
#         continue
#     print(f'Hello Mr/ Mrs {x}!')

# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
    
# число 100
# 1, 2, 4, 5, 10, 
# 20, 25, 50, 100

# num = 1_000_000_000_000
# res = []

# for x in range(1, int(num ** 0.5)+ 1):
#     if num % x == 0:
#         res.extend({x, num // x})

# res.sort()
# print(res)


