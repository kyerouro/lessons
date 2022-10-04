word = input(f'Enter the word: ')
half_len = len(word) // 2
index = 0

while index < half_len:
    if word[-index - 1] != word[index]:
        print("The word is not a palindrome")
        quit()
    index += 1

print("The word is a palindrome")










