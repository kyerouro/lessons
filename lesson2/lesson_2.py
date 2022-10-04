# ___________________________________________________________Строковые методы
# str = "12"
#
# print(str.upper())
# https://docs.python.org/3.10/library/stdtypes.html#string-methods

# print(str.isdigit())
#
# id / print /input /return

# num_1 = 5
# print('1', id(num_1))
#
# num_2 = 5
# print('2', id(num_2))
#
# num_3 = num_1
# num_3 = 6
# print('3', id(num_3))
# print('4', id(num_1))


# ________________________________________________________Типы данных (базовые)
#  string - строки "Привет мир!!!"
#  int - числа (целочисленные) 1, 10 15, 1000 .....
#  float - числа (пл) 1.5, 2.7, 88.4
#  bool - логические if, else elif ( True, False)

# типы данных (коллекции)

# list (список) - [], ['Hello', 123, True, [1,2,3...]] - изменяемым типом данных
# https://docs.python.org/3.10/library/
# list_a = ['a', 'b', 42, 55]
# print(list_a)
# list_a.append('p')
# print(list_a[3])
# print(list_a)
# num_1 = list_a[2]
# num_2 = list_a[3]
# print('Result: ', num_1 + num_2)
# print(len(list_a))
# list_a[0] = 77
# print(list_a)

# tuple (кортеж) - (), (1, 5.7, 'hello', False) - не изменяемый тип данных
# tuple_1 = (1, 5.7, 'hello', False)
# print(tuple_1)

# set (множество) - {}, {1,2, 'a'} - изменяемым типом данных
# num = {2, 4, 1, 3, 4}
# print(num)
# num.add(1)
# print(num)  # 1,2,3,4,1

# dict (словарь) - {}, {'num': 2, 'str': 'Hello'} - изменяемым типом данных
# d_dict = {'num': 2, 'str': 'Hello'}
# print(d_dict.get('str2'))  # способ получения 1
# print(d_dict['num'])  # способ получения 2
# d_dict['new'] = 55  # способ добавления 1
# d_dict.update({'qwe': False})  # способ добавления 2
# print(len(d_dict))
# print(d_dict)
# del d_dict['str']
# print(d_dict)
# print(len(d_dict))

# num = 0
# print(type(num))
# print(bool(num))  # 1 - True, 0 - False

# str = 'qwe'
# print(type(str))
# print(bool(str))

# num = 55
# print(type(num))
# num = str(num)
# print(type(num))

# str = 'Hello: world'
# print(str.split(':'))

# TODO: удалить код
# Функция print
# print('Hello, world', sep=',', end='\n\n')
# Функция input
# input('Введите данные: ')

# str = """
# Поддерживаемые опперции Калькулятора          + - / *
# ыход из программы
# """
#
# print(type(str))

# GIT
# https://github.com/
