# Кодировка
# !"№%:,.;()
# ячсячс
# zxcvbn

# я - 102
# z - 103
# " - 105
# @ - 106

# UTF-8 | UTF-16 - формат кодировки
#
# text = "Hell©o"
#
# code = text.encode()
# print(code)
#
# decode = code.decode()
# print(decode)

# Работа с файлами способ №1 запись
# file = open('text.txt', 'w')
# file.write('Hello world1!!!\nHello world2!!!')
# file.close()
# Работа с файлами способ №1 чтение
# file = open('text.txt', 'r')
# print(file.read())
# print(file.read(3))
# for item in file:
#     print(item)
# print(file.readline())
# print(file.readlines())
# file.close()

# Работа с файлами способ №2
# file = open('text.txt', 'r')

# try:
#     print(file.readline())
# finally:
#     file.close()

# Работа с файлами способ №3
# with open('text.txt', 'r') as file:
#     print(file.readlines())

#
# # Формат JSON
# import json
#
# # data = {
# #     "first_name": "Anna",
# #     "last_name": "Ivanova",
# #     "age": 23,
# #     "children": [
# #         {
# #             "first_name": "Pety",
# #             "age": 2
# #         },
# #     ]
# # }
# #
# # with open('data.json', 'w') as file:
#     # json.dump(data, file)
#
# # Формат CSV
# # import csv
# #
# # with open('csv_tables.csv', 'r', encoding='utf-8') as file:
# #     file_reader = csv.reader(file, delimiter=',')
# #
# #     for row in file_reader:
# #         print(row)
#
# # Формат Excel
# # pip install openpyxl
# from openpyxl import Workbook
# import datetime
#
# wb = Workbook()
#
# # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = 42
#
# # Rows can also be appended
# ws.append([1, 2, 3])
#
# # Python types will automatically be converted
# ws['A2'] = datetime.datetime.now()
#
# # Save the file
# wb.save("sample.xlsx")

