"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы. """

import random

array = [random.uniform(0, 50) for _ in range(10)]

def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
            left = left[1:]
        else:
            res.append(right[0])
            right = right[1:]
    if len(left) > 0:
        res += left
    if len(right) > 0:
        res += right
    return res

def merged_sort(data):
    len_arr = len(data)
    if len_arr <= 1:
        return data
    else:
        mid = int(len(data) / 2)
        left = merged_sort(data[:mid])
        right = merged_sort(data[mid:])
        return merge(left, right)

print(array)

print('-' * 150)
print(merged_sort(array))