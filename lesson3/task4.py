age = int(input(f'Enter the age of the visitor: '))
number = 0

while age != "" \
             "":
    if 3 < int(age) < 12:
        number += 14
    elif 12 < int(age) < 65:
        number += 23
    elif int(age) > 65:
        number += 18
    else:
        number += 0
    age = input(f'Enter the age of the visitor: ')

print(f'Total ticket price: {number}' ' BYN')



