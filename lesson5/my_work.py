# Вспоминаем как объявлять функции
# def x(num):
#     if num >= 3:
#         return print(f"The product of a number by two is: {num * 2}")
#     else:
#         return print("The number is less than three!")
#
#
# x(int(input("Enter the number: ")))


# Как работает функция lambda без функций высшего порядка (тоже самое можно сделать при помощи декоратора)
# def fff1(my_callback):
#     print("fff1 start")
#     my_callback()
#     print("fff1 finish")
#
#
# def fff2(my_callback):
#     print("fff2 start")
#     my_callback()
#     print("fff2 finish")
#
#
# hui = (lambda: print("-- hui!"))
# fff1(hui)
# fff2(hui)

# Разобраться с задачей 4 урока 5:

import functools
import time


def timer(func):
    """Выводит время выполнения декорируемой функции"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Функция {func.__name__!r} выполнена за {run_time:.4f} с")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(1)

