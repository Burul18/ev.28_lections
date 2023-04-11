# sentence = input('Vvedite predlojeniye: ')


# # if sentence[-1] == '?':
# #     print('Yes, voprositel\'noe!')
# # else:
# #     print('No, normal\'noe')

# print('Yes, voprositel\'noe!' if sentence[-1] == '?' else 'No, normal one!') 


# # ~~~~~~~~~~~~~~~
# Ternary operators(Тернарный оператор) - это конструкция которая по своему действию аналогична конструкция if/else, но при этом записывается в одну строчку

# number = int(input('Vvedite chislo: '))
# res = 'even number' if number % 2 == 0 else 'odd number'
#     #    четное                                нечетное
# print(res)

# <выражение если True> if <само условие> else <выражение если False>

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite max or min: ')
# # res = max(ls) if choice.lower().strip() == 'max' else min(ls)
# # print(res)

# # if choice.lower().strip() == 'min':
# #     print(min(ls))
# # elif choice.lower().strip() == 'max':
# #     print(max(ls))
# # else:
# #     print('Invalid choice')
 
# res = max(ls) if choice.lower().strip() == 'max' else min(ls) if choice.lower().strip() == 'min' else 'invalid choice!'
# print(res)

# # ~~~~~~~~~~~~~

flag = True
symbols = '0123456789' + '-' + '.'


while flag:
    print()
    num1 = input('Vvedite chislo1: ')
    is_correct_number = True
    for x in num1:
        if x not in symbols:
             print('Vy vveli nepravil\'noe chislo!')
             is_correct_number = False
             break
        
        if not is_correct_number:
            continue

num2 = input('Vvedite chislo2: ')
for x in num2:
    if x not in symbols:
        print('Vy vveli nepravil\'noe chislo!')
        is_correct_number = False
        break   
    if not is_correct_number:
        continue
    
num1 = int(input()) 
# num2 = int(input()) 
    
# print(num1, type(num1))
# print(num2, type(num2))

operator = input('Vvedite operator(+, -, /, *): ').strip()
    
if operator == '+':
    print(f'Rezultat: {num1 + num2}')
elif operator == '-':
    print(f'Rezultat: {num1 - num2}')
elif operator == '/':
    if num2 == 0:
        print('Na 0 delit\' nelzya!')
    else:
        print(f'Rezultat: {num1 / num2}')
elif operator == '*':
    print(f'Rezultat: {num1 * num2}')
else:
    print('Vy vveli nevernyi operator!')
    
choice = input('hotite prodoljit\' (yes/ no)? ')
if choice.lower().strip() != 'yes':
    flag = False
    print('poka poka!')
    






# x = int(input("Vvedite chislo1: "))
# y = int(input('Vvedite chislo2: '))
# if x % y != 0:
#     print('x не делится на y')
#     a = x // y
#     print(f'Частное: {a}')
#     b = x % y
#     print(f'Остаток: {b}')
# else: 
#     print('x делится на y') 
#     d = x//y
#     print(f'Частное: {d}')

# year = int(input('Введите год: '))
# if year % 4 == 0 and year % 100 == 0:
#     print('Yes')
# elif year % 400 == 0:
#     print('Yes')
# else:
#     print('No')

# num = chr(int(input('Vvedite chislo: ')))
# if num.isalpha():
#     print(f'это буква {num}')
# else:
#     print(f'Это не буква, а символ {num}')

    