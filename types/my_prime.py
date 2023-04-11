# Есть список а = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите элементы, которые меньше 5

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for elem in a:
#     if elem < 5:
#         print(elem)

# print(list(filter(lambda elem: elem < 5, a)))

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков

# set() - Множество - это контейнер, который содержит уникальные не повторяющиеся элементы в случайном порядке

# b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 55, 89]

# res = list(filter(lambda elem: elem in b, a))

# result = list(set(a) & set(b))
# print(result)

# import tkinter as *
# root = Tk()

# win = Tk()
# win.geometry(f'240x260+100+200')
# win['bg'] = '33ffe6'
# win.title('Калькулятор')

# win.mainloop()


# num1 = float(input('Введите первое число:'))
# operation = input('Выберите операцию (-, +, /, *, //, %, **): ')
# num2 = float(input('Введите второе число:'))


# if operation == '+':
#     print('Результат:', num1 + num2)
# elif operation == '-':
#     print('Результат:', num1 - num2)
# elif operation == '*':
#     print('Результат:', num1 * num2)
# elif operation == '/':
#     if num2 != 0:
#        print('Результат:', num1 / num2)
#     else:
#         print('Деление на 0 запрещено!')
# elif operation == '//':
#     if num2 != 0:
#         print('Результат:' , num1 // num2)
#     else:
#         print('Деление на 0 запрещено!')
# elif operation == '%':
#     if num2 != 0:
#         print('Результат:' , num1 % num2)
#     else:
#         print('Деление на 0 запрещено!')
# elif operation == '**':
#     print('Результат:', num1 ** num2)
# else:
#     print('Данной операции нет в системе')

    
# import turtle 
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x % 6])
#     t.width(x/100+1)
#     t.forward(x)
#     t.left(59)
    

# adjective = input('Введите прилагательное: ')
# noun = input('Введите существительное: ')
# verb = input('Введите глагол: ')
# print('Ваша чепуха!')
# print('Этот', adjective, noun, verb, 'На ленивую рыжую собаку')


# import tkinter as TK
# root = TK()
# import turtle
# t = turtle.Pen()
# for x in range(360):
#     t.forward(x)
#     t.left(90)


# from tkinter import *


# window = Tk()
# window.title("Добро пожаловать в приложение PythonRu")
# window.mainloop()

# from tkinter import *  
  
  
# window = Tk()  
# window.title("Добро пожаловать в приложение PythonRu")  
# lbl = Label(window, text="Привет")  
# lbl.grid(column=0, row=0)  
# window.mainloop()


# Trello

