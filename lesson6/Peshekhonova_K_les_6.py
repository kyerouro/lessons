""" Katherine Peshekhonova, lesson 6 """

import json

""" Task 1 """


byte_code = b'r\xc3\xa9sum\xc3\xa9'
decoded_utf = byte_code.decode()
print(f'The first decoded string: {decoded_utf}')

byte_latin = decoded_utf.encode('latin1')
print(f'Byte value: {byte_latin}')

decoded_latin = byte_latin.decode('latin1')
print(f'The second decoded string: {decoded_latin}')

""" Task 2 """


str_1 = 'Hello there!'
str_2 = 'Long time no see!'
str_3 = 'Look who’s here!'
str_4 = 'Good to see you!'

file = open('text.txt', 'w+')
file.write(str(str_1) + "\n" + str(str_2) + "\n")
file.close()

file = open('text.txt', 'a')
file.write(str(str_3) + "\n" + str(str_4))
file.close()

file = open('text.txt', 'r')
print(file.read())
file.close()

""" Task 3 aaa"""


data = {
    673904: ("Noah", 31),
    357103: ("Jacob", 24),
    846592: ("William", 29),
    346859: ("Liam", 34),
    947657: ("Cory", 23)
}

with open('data.json', 'w') as write_file:
    json.dump(data, write_file)

print(data)

""" Task 4 """

