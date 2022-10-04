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










