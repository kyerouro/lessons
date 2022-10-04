number = int(input(f'Enter a positive number: '))
quantity = 0
amount = 0

if number == 0:
    print('The first number must not be zero!')
    quit()

while number != 0:
    amount += number
    number = int(input(f'Enter a positive number: '))

    quantity += 1

print("Average value:", amount / quantity)

