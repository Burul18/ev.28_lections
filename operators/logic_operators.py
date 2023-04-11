# Операторы сравнения
# Условные операторы и логические операторы

# операторы сравнения
# <, >, ==(равно), !=(не равно), <=, >=

# 1 < 5 True
# 7 > 9 False

# Условные операторы
# if
# elif
# else

# if <condition>:
#     <body if>  # сработает если в condition if придет true
# [elif] <comdition>:
#     <body elif>
# [else]:
#     <body else> # сработает если во всех стоящих условиях пришло False

# str = input('Enter smt:')

# if str.lower == 'hello':
#     print('Hello? it\'s me\nI was wondering if after all these years you\'d like to meet')
# elif str.lower == 'john':
#     print('Welcome back John Snow! The King of North!')
# elif str.lower == 'abra- kadabra':
#     print('Sim salamon Kadabra')
# else:
#     print('Совпедений не найдено!')

# print('Registration Form:')
# email = input('Enter your email:')
# password = input('Enter the password:')
# if len(password) < 8:
#     raise ValueError('Password is too short!\n Need to be 8 symbols or more!')
# elif password.isdigit():
#     raise ValueError('Password is invalid!\n Password must contain symbols too!')
# elif password.isalpha():
#     raise ValueError('Password is invalid!\n Password must contain number  or special symbols too!')

# password2 = input('Enter password confirmation!')

# if password != password2:
#     raise ValueError ('Password did not match!')

# print(f'Succesfully registered! Hello Mr/Mrs {email}!')

# age = input('Enter your age!')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('[Invalid value for age]')

# if age < 18:
#     print(f'Access Denied! Come again after {18 - age} year!')
# else:
#     print('You can pass! Welcome to KZ!')

# and - логическая и
# or - логич или
# not - логич отрицание

# money = 1_000_001
# status = 'base'

# if money > 1_000_000 and status == 'premium':
#     print('You\'re president of our club!')
# elif money > 1_000_000 or status == 'premium':
#     print('You\'re ministr of our club!')
# else:
#     print('You\'re honorable member of our club!')

# str1 = 'hello world'
# print(str1)
# symbol = input('Enter the symbol:')

# # if symbol not in str1:
# #     print(f'The symbol: {symbol} does not exists!')
# # else:
# #     print(f'The symbol: {symbol} exists')

# if symbol in str1:
#     print(f'The symbol: {symbol}  exists!')
# else:
#     print(f'The symbol: {symbol} does not exists') 

# разрешаем доступ, если он юзер гита или гугла и его возраст больше 21 или у него деньги (10000)

# user = 'Burul'
# is_google_user = True
# is_github_user = False
# age = 15
# user_coins = 9000

# if (is_github_user or is_google_user) and (age >= 21 or user_coins > 10000):
#     print(f'You can enter the system Mr/Mrs {user}!')
# else:
#     print(f'Sorry, you couldn\'t enter Mr/Mrs {user}!')