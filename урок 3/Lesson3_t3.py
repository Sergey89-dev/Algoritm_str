"""3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы."""

import random

a = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {a}')

max = a[0]
min = a[0]

for i in a:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = a.index(min)
max_index = a.index(max)
a[min_index], a[max_index] = a[max_index], a[min_index]
print(f'Массив осле изменения элементов {min_index} и {max_index}: {a}')
