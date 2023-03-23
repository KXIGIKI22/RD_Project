#Завдання 1
def go_y(x, y):
    x = 3
    y = 4
    return x ** y

#Завдання 2
def sum_all(*args):
    result = sum(*args)
    return result

#Завдання 3
#3,1
arr = [22, 34, 87, 155, 2, 333, 124, 605]
max_element = max(arr)
print(max_element)

#3.2
def find_max(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element
arr = [3, 7, 9, 2, 1]
max_element = find_max(arr)
print(max_element)

#3.3
from functools import reduce

arr = [9, 22, 66, 22, 15]
max_element = reduce(lambda a, b: a if a > b else b, arr)
print(max_element)