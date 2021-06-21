"""5. В массиве найти максимальный отрицательный элемент. Вывести на
экран его значение и позицию в массиве."""

import random

a = [random.randint(-99, 99) for _ in range(100)]
print(f'Массив: {a}')

min_index = 0

for i in a:
    if a[min_index] > i:
        min_index = a.index(i)

if a[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {a[min_index]}.',
            f'Находится в массиве на позиции {min_index}')