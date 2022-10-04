# Функция snake_case/style пример: get_data():

# def summa(a, b):
#     return a + b
#
# print(summa(2, 3))

# def hello(name):
#     return f"Hello {name}"
#
# print(hello("Vasy"))

# Аргументы по умолчанию
# def my_format(string, char_1='**( ', char_2=' )**'):
#     return f'{char_1}{string}{char_2}'
#
# print(my_format("Привет весм"))

# Сбор аргументов в коллекцию
# def print_tuple(*args):
#     print(args)
#
# print_tuple(1, 2, 3, 4)

# Обобщенное понятие функции
# def full_func(*args, **kwargs):
#     print(args)
#     print(type(args))
#     print(type(kwargs))
#     print(kwargs)
#
# full_func(1, 2, 3, a=[1, 2, 3], b=5, c=6)

# Именованные аргументы
# def my_pow(power, number):
#    return number ** power + 1
#
# result = my_pow(power=3, number=5)
#
# print(result)

# Сбор аргументов в словарь
# def my_func(**kwargs):
#    keys, values = [], []
#    for key, value in kwargs.items():
#        print(key, value)
#        keys.append(key)
#        values.append(value)
#    return keys, values  #  == tuple
#
# print(my_func(a=5))
# print(type(my_func(a=5)))

# def my_func_2(name, *args, **kwargs):
#     print(name)
#     print(args)
#     print(kwargs)
#
# my_func_2('Vasy', 555,777, a=[1, 2, 3], b=5, c=6)

# Область видимости локальная
# def my_func():
#     num = 5
#     print(num)
#     input("Введите {num} чисел ")

# Область видимости глобальная
# num_1 = 10

# def my_func():
#     num_2 = 5
#     print(num_2)
#     print(num_1)
#     # input("Введите {num} чисел ")
#
# print(num_1)
#
# my_func()

# num_1 = 10
#
# def my_func_3():
#     num_2 = 5
#     global num_1
#     num_1 = 20
#     print(num_2)
#     print(num_1)
#
# def my_func_5():
#     pass
#
# my_func_3()
# print(num_1)
#
# my_func_5()


# Аннотации типов
# def my_func(name: str, age: int) -> tuple:
#     x: float = 1.4
#     return name, age, x
#
# data = my_func("Vasy", 20)
# print(data)
#
# import random
#
# print(type(random.randint(1, 5)))


# Генераторы списков
# part_1 лист компрекейшен
# b = [i for i in range(10)]
# print(b)
# part_2
# b = []
# for i in range(10):
#     b.append(i)
#
# print(b)

# Генераторы списков
# print([i for i in range(10)])
# # Генераторное выражения
# print((i for i in range(10)))
# # Сет
# print({i for i in range(10)})
# # Словарь
# print({x: x**2 for x in range(10)})

# """
# asdasd
# """
#
# def func_1():
#     pass
#
# def func_2():
#     pass
#
# def func_3():
#     pass
#
# def func_4():
#     pass
#
# a = func_1()
# b = func_2()
# c = func_3()
# d = func_4()
#
# print(a, b,c, d)
