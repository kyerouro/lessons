# """Что происходит в данном модуле"""
#
#
# def square(n):
#     """Принимает число и возвращает его квадрат"""
#     return n**2
#
# print(square.__doc__)

# lambda функция
# a_list = list(map(lambda num: num + ' - qwe', ["4", "5", "6"]))
# print(a_list)

# Функция высшего порядка / map
# a_list = list(map(lambda num: num + ' - qwe', ["4", "5", "6"]))

# print(list(lambda num: num + ' - qwe', ["4", "5", "6"]))
# print(map(lambda num: num + ' - qwe', ["4", "5", "6"]))
# print(list(map(lambda num: num + ' - qwe', ["4", "5", "6"])))

# Функция filter
# result = list(
#     filter(
#         lambda num: num % 2 != 0,
#         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     )
# )
#
# print(result)

# Функция reduce
# from functools import reduce
#
# num = reduce(
#     lambda item_1, item_2: item_1 * item_2,
#     [1, 2, 3, 4, 5], 10
# )
#
# print(num)
#
# # Декораторы
# def my_dec(func):
#     def wrapper():
#         print('Start')
#         func()
#         print('Stop')
#     return wrapper
#
#
# @my_dec
# def my_func():
#     print('Hello')
#
# my_func()
