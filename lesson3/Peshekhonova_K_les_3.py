# Katherine Peshekhonova, lesson 3
# 1. Ввести предложение состоящее из двух слов. Поменять местами слова, добавить восклицательный знак в начало
# и конец, слова разделить 3-мя символами (пробел, восклицательный знак и еще пробел), вывести итоговое предложение
# на экран. Задание необходимо выполнить 3-мя разными способами форматирования.

print("- task1 (first way) ↓")

first_word = str(input(f'Enter the first word: '))
second_word = str(input(f'Enter the second word: '))
print(f'!{second_word}' + f' ! {first_word}!')

print("_____")
print("- task1 (second way) ↓")

first_word = str(input(f'Enter the first word: '))
second_word = str(input(f'Enter the second word: '))
print("{var}".format(var="!" + second_word + " " + "!" + " " + first_word + "!"))

print("_____")
print("- task1 (third way) ↓")

two_words = str(input(f'Enter two words through the space:'))
index = two_words.find(" ")
word_1 = two_words[:int(index)]
word_2 = two_words[int(index)+1:]
print(f'!{word_2} ! {word_1}!')


# 4. Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n).
# Реализовать в 2-ух вариантах. Реализация с помощью цикла "for":

print("__________")
print("- task4 (for loops) ↓")

n = int(input(f'Enter a positive integer number: '))
amount = 0

for number in range(n+1):
    amount += number**3
print(f'Amount of cubes: {amount}')


# Реализация с помощью цикла "while":

print("_____")
print("- task4 (while loops) ↓")

n = int(input(f'Enter a positive integer number: '))
number = 1
amount = 0

while number <= n:
    amount += number**3
    number += 1
print(f'Amount of cubes: {amount}')


# 5. Сделать программу в которой надо будет угадывать число.

print("__________")
print("- task5 ↓")

import random

hidden_number = random.randint(1, 100)
print("Guess a number from 1 to 100!")
tries = int(input(f'Enter how many tries I have to give you: '))
attempt_number = 1

while attempt_number <= tries:
    number = int(input(f'Enter a number: '))
    if number > hidden_number:
        if attempt_number < tries:
            print(f'My number is less!')
    elif number < hidden_number:
        if attempt_number < tries:
            print(f'My number is greater!')
    else:
        print(f"You got it! I riddled: {hidden_number}")
        quit()

    attempt_number += 1

print(f"You loose, I riddled: {hidden_number}")


# 2, 3. Написать программу, которая получит имя и возраст пользователя, проверит возраст и выдаст приветственное
# сообщение в зависимости от возраста. Завернуть это в вечный цикл.

print("__________")
print("- task2, task3 ↓")

while True:
    name = str(input(f'Enter a name: '))
    age = int(input(f'Enter the age: '))
    if int(age) <= 0:
        print("Error, enter again")
    elif 0 < int(age) < 10:
        print(f"Hi, kid {name}!")
    elif 10 <= int(age) <= 18:
        print(f"What's up, {name}?")
    elif 18 < int(age) < 100:
        print(f"What would you like, {name}?")
    else:
        print(f"{name}, you're lying - they don't live that long nowadays!")
