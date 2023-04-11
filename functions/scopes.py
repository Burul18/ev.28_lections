# Область видимости и пространства имен (scopes)
# технология которая определяет контекст имени(переменные), 
# в рамках которого мы можем ее использовать

# built-ins(втроенная область видимости) -> print, len, max
# global(Глобальная) -> область одного файла
# enclosed( не локальная(замкнутая), nonlocal)
# local(локальная) -> область внутри одной функции

# x = 200

# def myFunc():
#     print(x)
#     a = 300
#     print(a)

# myFunc()
# # print(a)
# print(x)

# a = 10 #global
# print #built-in
# def hello(): # global
#     a = 'Hello world' # local
#     print(a, 'local inside in func!')

# hello()
# print(a, 'global')

# # LEGB - local enclosed global built-in

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Enclosed - замкнутое пространство имен - локальное пространство, 
# у которого есть внутренне (вложенное) локальное пространство

# x = 'global'
# print(x), '1'

# def enclosed(): #global
#     x = 'enclosed'
#     def local(): # enclosed
#         x = 'local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')


# a = 5

# def func():
#     print(a)

# func()

# globsl -> позволяет изменять значение глобальной переменной находясь внутри локальной области

# nonlocal -> позволяет именять значение не локальной (замкнутой) переменной находясь внутри локальной области

# var = 100

# def increment():
#     global var
#     var += 1 #var + 1

# print(var)
# increment()
# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c = counter()
# print(c) #<function counter.<locals>.increment at 0x7fc7e83d20e0>
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# # print(counter())
# # counter()
    
# def func():
#     pass

# a = func
# print(a())

# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# # globals - func которая возващает все имена внутри глобальной области видимости

# # locals - функция которая возвращает все имена внутри глобальной области видимости и локальной


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# def showStats(heroes, mobs):
#     print()
#     print(f'John Snow ты убил: \n\tгероев: {heroes} \n\tмобов: {mobs}')
#     print()

# counter_heroes = counter()
# counter_mobs = counter()
# heroes = 0
# mobs = 0

# print('Приветствую Вас, короля севера John Snow в Вестеросе!')
# while True:
#     print('Тебе доступны следующие действия: ')
#     print('1 - Убить героя, 2 - Убить моба, 3 - Статистика, 4 - Выйти из игры')
#     choice = input('Введите что хотите сделать: ').strip()
#     if choice == '1':
#         heroes = counter_heroes()
#         print('Вы обезглавили Ланистера!')
#     elif choice == '2':
#         mobs = counter_mobs()
#         print('Вы убили белого ходока!')
#     elif choice == '3':
#         showStats(heroes, mobs)
#     elif choice == '4':
#         print('Пока пока! Ждем еще раз!')
#         break
    
