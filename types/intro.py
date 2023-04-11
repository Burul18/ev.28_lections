# Типы данных в питоне

# 1. NoneType - ничего, пустота -> None
# 2. Boolean - истинно или ложь -> True/False
# 3. String - строки - str -> "Hello world", 'Hello world'
# "I'm North King"
# 'I'm North King'
# "My name is John Snow"
# 4. Численные типы данных
# а) integer - целое число int -> -1, 5, 15, 25
# b) float - число с плавающей точкой -> 1.5 , 15.25
# c) complex - 0j: 1 5 9j
# 5. Списковые типы данных (коллекция)
# a) list (массив/список) ->[5 , 2 , 4, True, 'hello']
# b) tuple (кортеж) -> (1, 2, 3, None)
# # c) range (последовательность) -> range (1, 10)
# # 6. set() - множество ->{1, 2, 3, 4, 5, 6, 7, 8, }
# 7. dict(словари) -> содержат данные в себе в виде ключа и значение {1:''}

# Mutable (изменяемые типы данных)
# 1. list
# 2. set
# 3. dict

# Immutable (неизменяемые типы данных)
# 1. None
# 2. bool
# 3. int, float, complex
# 4. str
# 5. tuple, range
# 6. frozenset

# Переменная - проименовая область памяти, предназначение для хранения


# num = 5
# str1 = 'Hello world'

'''
Стандартный вывод данных
'''
# в питоне для вывода данных в терминал используется встроенная функция 
# stroka = 'Hello world! My name is John Snow'
# print(stroka)
# print(27+5)

"""
Стандартный ввод данных через терминал используется функция input()
"""
# a = input('Введите число:')
# num = int(a)
# print (num)
# print (type(num))
# print('данные в переменных', a, num)
# # print('В переменной а хранится:', a, 'ее тип данных', type(a))
# print('В переменной num хранится', num, 'ее тип данных', type(num))

