#Завдання 1
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
def intersection(set1, set2):
    return set1.intersection(set2)
print(set1.intersection(set2))

#Завдання 2
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {3, 4, 5, 7, 8, 9}
def unique_elements(set1, set2):
    unique = set1 ^ set2
    return list(unique)
unique = unique_elements(set1, set2)
print(unique)

#Завдання 4
def is_number(x):
    return isinstance(x, (int, float, complex))
def filter_numbers(arr):
    return list(filter(is_number, arr))
arr = [1, "a", 2, 5, "b", 3, "c"]
numbers = filter_numbers(arr)
print(numbers)
