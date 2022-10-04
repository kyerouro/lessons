# = - оператор присвоение
# num_1 = 3 + 4
# print(num_1)
# += оператор присвоение "сложение И" добавление
# num_2 = 1
# num_2 += num_1  #  num_2 = num_2 + num_1
# print(num_2)
# -= оператор присвоение "вычитание И"
# num_2 = 10
# num_2 -= num_1  #  num_2 = num_2 - num_1
# print(num_2)
# *=, /=, %=, **=, //=
# Присвоение кортежей
# spam, ham = 'Spam', 'YUM'
# print(spam, ham)
# Присвоение списком
# [spam, ham] = ['Spam', 'YUM']
# print(spam, ham)
# Присвоение последовательностью
# a, b, c, d = 'spam'
# print(a, b, c, d)
# Присвоение распоковка
# a, *b = 'spamertyi'
# print(a, b)
# Обмен значениями
# a = 2
# b = 3
# print(a, b)
# b, a = a, b
# print(a, b)

# Форматирование строк "format"
# name = "Boris"
# print("Hello {var}".format(var=name))
# print("{1}, {0}, {2}".format('a', 'b', 'c'))
# print("{}, {}, {}".format('a', 'b', 'c'))
# print("{}, {}, {}".format('a', 'b', 'c'))
# print("{name[1]}".format(name=['qwe', 'Boris']))

# Форматирование строк "f-string"
# name = "Boris"
# print(f"Hello {name}")
# name = ['qwe', 'Boris']
# print(f"Hello {name[1]}")

# Операторы ветвления (if/else)
# n = True
#
# if n:
#     print("True")
# else:
#     print("False")

# Операторы ветвления (if/elif/else) Дополнительное условие
# num = 5
#
# if num < 2:
#     print("num < 2")
# elif num > 10:
#     print("num > 10")
#     # ....
# else:
#     print("num in {2-10}")

# and, or, not, is, in

# num = 1
# if num and 5:
#     print("Оба условия")
#
# if num or 10:
#     print("Как минимум одно значение True")
#
# if not False:
#     print("0 - False, значит результат - True")
#
# if 5 == 5:
#     print("5 это 5")
#
# if 5 in [num, 2, 5]:
#     print("5 содержится в списке")
#
# a = None
# if a is None:
#     print("a пустое")
#
# if (
#         5 and 5 or 6
#         and not None
# ):
#     print('5 есть пять и не пусто')

# Тернарное выражение
# is_active = True
# state = 'active' if is_active else 'not active'
# print(state)

# Вложенные условия
# num = 5
#
# if num > 0 and num < 10:
#     if num == 5:
#         print('Результат 5')
#     else:
#         print('Не 5')
# else:
#     print('Нет ответа ')

# Циклы while
# condition = True
# i = 0
# while condition:
#     print("Что-то!!!")
#     # stop = input("Введите стоп")
#     i += 1
#     if i == 10:
#         condition = False
#     # if 'stop' == stop:
#     #     condition = False

# Циклы for
# a_list = [1, 2, 3, 4, 5, 'qwe']

# for i in a_list:
#     if i == 4:
#         break
#     print(i)

# for i in a_list:
#     if i == 4:
#         continue
#     print(i)

# num = -1
# for i in a_list:
#     num += 1
#     if num == 2:
#         continue
#     print(i)

# for _id, item in enumerate(a_list):
#     if _id == 2:
#         break
#     print(item)
