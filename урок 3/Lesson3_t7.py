"""7. В одномерном массиве целых чисел определить два наименьших
элемента. Они могут быть как равны между собой (оба являться
минимальными), так и различаться."""

import random

a = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {a}')

min_index_1 = 0
min_index_2 = 1

for i in a:
    if a[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = a.index(i)
    elif a[min_index_2] > i:
        min_index_2 = a.index(i)

print(f'Два наименьших элемента: {a[min_index_1]} и {a[min_index_2]}')