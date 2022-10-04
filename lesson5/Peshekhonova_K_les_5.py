# Katherine Peshekhonova, lesson 4
# Task 1

analyzer = (lambda number: print("This number is even") if number % 2 == 0 else print("This number is odd"))

input_number = int(input("Enter the number: "))
analyzer(input_number)


# Task 2

num_list = [5, 83, 24, 9, 17]


# First version
num_str1 = list(map((lambda number: str(number)), num_list))
print(num_str1)


# Second version
num_str2 = list(map(str, num_list))
print(num_str2)


# Third version
def my_str(x):
    return str(x)


num_str3 = list(map(my_str, num_list))
print(num_str3)


#Task 3

my_words = ("radar", "daddy", "level", "apple", "peep", "beauty")

palindromes = list(filter(lambda word: word == word[::-1], my_words))
print("Words palindromes:", list(palindromes))

