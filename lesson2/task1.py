a = input(f' Enter the first value: ')
if not a.replace("-", "", 1).replace(".", "", 1).isdigit():
    print(f' Invalid number')
    quit()
a = float(a)

b = input(f' Enter the second value: ')
if not b.replace("-", "", 1).replace(".", "", 1).isdigit():
    print(f' Invalid number')
    quit()
b = float(b)

operator = input(f' Enter operator: ')

if operator == "+":
    print(f' Result of addition: {a + b}')
elif operator == "-":
    print(f' Subtraction result: {a - b}')
elif operator == "*":
    print(f' Multiplication result: {a * b}')
elif operator == "**":
    if a == 0 and b < 0:
        print(f' Can\'t be raised to a negative power')
        quit()
    print(f' The result of the exponent: {a ** b}')
elif b == 0:
    print(f' Division by zero')
    quit()
elif operator == "/":
    print(f' Division result: {a / b}')
elif operator == "%":
    print(f' The result of dividing by a modulo: {a % b}')
elif operator == "//":
    print(f' The result of integer division: {a // b}')
else:
    print("Invalid operator, enter one of these: +, -, *, /, %, **, //")

