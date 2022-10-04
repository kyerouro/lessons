# Katherine Peshekhonova, lesson 4
# Task 1

dict_list = {"November": 11, "March": 3, "August": 8}

dict_generator = [(value, key) for key, value in dict_list.items()]
new_dict = dict(dict_generator)

print(f'New dictionary: {new_dict}')

# Task 2
# Finding factorials using a loop

num = int(input("Enter the number: "))
fact = 1
for i in range(1, num+1):
    # n! = 1 * 2 * … * n
    fact *= i
print(f'{num}! = {fact}')

# Finding the factorial with a recursive function

def fact(number):
    if number <= 1:
        return 1
    else:
        # n! = (n - 1)! * n
        return fact(number - 1) * number


input_number = int(input("Enter the number: "))
result = fact(input_number)

print(f'{input_number}! = {result}')

# Task 3

def finished_list(num1, num2, amount, l):
    from random import randint
    for i in range(amount):
        l.append(randint(num1, num2))


def process(our_list, our_dict):
    for i in our_list:
        if i in our_dict:
            our_dict[i] += 1
        else:
            our_dict[i] = 1


your_list = []
your_dict = {}

minimum = int(input('Enter the minimum value: '))
maximum = int(input('Enter the maximum value: '))
quantity = int(input('Enter the number of items: '))

finished_list(minimum, maximum, quantity, your_list)
process(your_list, your_dict)

print(f'Random list: {your_list}')
print('Number of repeating numbers:')

for item in sorted(your_dict):
    print("'%d':%d" % (item, your_dict[item]))


