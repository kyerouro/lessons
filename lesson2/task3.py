list1 = [45, "fox", None, 45, 6.8, "fox", 1, 2, 3, 4, 5]
list2 = list(set(list1))
if len(list1) == len(list2):
    print("No duplicates")
else:
    print("Duplicates are found")