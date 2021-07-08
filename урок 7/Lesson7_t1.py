from array import array
""" Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100).
 Выведите на экран исходный и отсортированный массивы. """
import random 
array = [random.randint(-100, 100) for _ in range(100)]

def bubble(data):
    process = True
    for i in range(len(data) -1, 0, -1):
        if not process:
            break
        process = False
        for j in range(i):
            if data[j] < data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
                process = True
    return data

print(array)
print('-'* 100)
print(bubble(array))