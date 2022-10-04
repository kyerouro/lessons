#list_1 = [1, 2, 3, 4, 5]
#for i in list_1:
#    if i == 4:
#        print(i)



#dict_1 = {1:2, 3:4, 5:6}
#for i in dict_1:
#    print(i)



#list_1 = [1, 2, 3, 4, 5]
#counter = 0
#for i in list_1:
#    if i == 4:
#        print(i, counter)
#    counter += 1
#print(counter)



#list_1 = [1, 2, 3, 4, 5]
#for index, i in enumerate(list_1):
#    print(index, i)



#list_1 = [1, 2, 3, 4]
#for index, _ in enumerate(list_1):
#    print(index)



#for i in range(1001):
#    print(i)



#for i in range(10, 100):
#    print(i)



#for i in range(10, 100, 10):
#    print(i)



#for i in range(1, 1000):
#    if i % 20 == 0 and i % 200 == 0:
#        print(i)
#        break



#for i in range(1, 1000):
#    if i == 400 or i == 500:
#        print(i)
#        continue



#a = input()
#list_1 = []
#while a != "0":
#    a = input()
#    list_1.append(a)
#print(list_1)



#a = 0
#while True:
#    a += 1
#    print(a)
#    break




#a = "1, 2, 3, 4, 5, 6"
#list_1 = a.split(",")
#print(list_1)



#a = 18
#b = 4 if a > 18 else 4
#print(b)



#list_1 = [1, 2, 3, 4, 5]
#list_2 = [6, 7, 8, 9]
#for i in list_1:
#    for j in list_2:
#        print(i, j)



# Задча 1. Сделать таблицу умножения с помощью вложенного цикла (двойного).
#for i in range(1, 10):
#    for j in range(1, 10):
#        print(j * i)



# Задача 2. Найти все элементы, которые не четные, не включая 1k.
#for i in range(1, 1000):
#    if i % 2 != 0:
#        print(i)



# Задача 3. Сумма чисел от 0 до 100 (100 включая).
#summ_num = 0
#for i in range(0, 101):
#    summ_num += i
#print(summ_num)



# Задача 4. Найти факториал от 20.
#a = 1
#for i in range(1, 21):
#    a *= i
#print(a)




# Сортировка пузырьком. Берем начальный элемент и сравниваем со всеми, если он больше - меняем со след.
#a = [5, 4, 3, 2, 1]
#for index_i in range(len(a)):
#    for index_j in range(index_i + 1, len(a)):
#        if a[index_i] > a[index_j]:
#            num = a[index_i]
#            a[index_i] = a[index_j]
#            a[index_j] = num
#print(a)



# Задача 5. Перевернуть число.
#a = 5432
#res = 0
#while a > 0:
#    d = a % 10
#    a = a // 10
#    res = res * 10 + d
#print(res)
















