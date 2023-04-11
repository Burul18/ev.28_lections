# dict = это словарь - упорядочанная коллекция элементов (python 3.7 -> ordered). Каждый элемент внутри словаря хранится в виде пары: {ключ: значение}

# Ассоциативный массив, hash table, object(js), structure == dictionary(py)

# Ключами могут быть только неизменяемые типы данных и в словаре сохраняется только уникальные ключи.
# Тогда как значениями могут выступать любые типы данных.

# dict_ = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
#     }

# print(dict_)
# print(type(dict_))

# print(dict_['brand'], dict_['model'])
# print(dict_['year'])

# dict_['motor'] = 'GTE Turbo'
# dict_['brand'] = 'Tesla'
# print(dict_)

# a = {}
# b = dict()
# print(type(a))

# ''''''
# print(dir(dict))

# items. keys, values

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com',
#     'role': 'admin',
# }

# ls = user_info.keys()
# ls = list(ls)
# print(ls[2:])

# ls = user_info.values()
# ls = list(ls)
# print(ls)

# items = user_info.items()
# print(items)

# print(user_info)
# for value in user_info.values():
#     print(value)

# for key in user_info.keys():
#     print(key)

# for key, value in user_info.items():
#     # print()
#     print(f'keys: {key}, values: {value}')

# dict_ = {'name': 'Jeck', 'age': 17}
# print(dict_)
# dict_['name'] = 'John'
# dict_['age'] = 24
# dict_['address'] = 'WinterFell'
# print(dict_)

# dict_.update({'age': 25, 'address': 'BlackCastle'})
# print(dict_)

''''''''
# Получение данных со словаря
# dict_ = {1:'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[2], '!!!')
# print(dict_.get(2))

# setdefault - работает так же как get, но если нет такого ключа то создает новую пару из этого ключа

# dict_ = {1:'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault(3, 'Manty'))
# print(dict_)
# print(dict_.setdefault(5, 'manty'))
# print(dict_)

''''''''

# Создание - fromkeys
# ls = list(range(1, 100))
# new_dict = dict.fromkeys(ls, 'value')
# print(new_dict)

''''''''
# Удаление элементов
# pop, popitem

# pop(<key>) - удаляет пару по ключу
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# print(dict_)
# removed = dict_.pop('last_name')
# print(dict_)
# print(removed)

# popitem - удаляет последнюю пару

# dict_ = {'name': 'John', 'last_name': 'Snow'}
# removed = dict_.popitem()
# print(dict_)
# print(removed)

''''''''''''
# roles = {
#     0: 'Admin',
#     1: 'Customer',
#     2: 'Vendor' 
#     }

# users = {
#     1: {
#     'id': 1, 'role': roles[2], 'username': 'Tririon',
#     },
#     2: {
#     'id': 2, 'role': roles[0], 'username': 'John Snow',
#     },
#     3: {
#     'id': 3, 'role': roles[1], 'username': 'Raychel',
#     }
# }

# print(users)

# product = {
#     'id': 1,
#     'title': 'Samsung Galaxy 51',
#     'descrtption': 'Lorem Ipsum',
#     'price': 250,
# }

# print(product)

# id_user = int(input('Vvedite id: '))
# if users[id_user]['role'] == roles[0]:
#     product['descrtption'] = input('Vvedite opisanie: ')
# else:
#     print('You do not have permissions!')

# print(product)

