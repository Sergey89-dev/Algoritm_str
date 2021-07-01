"""5. В массиве найти максимальный отрицательный элемент. Вывести на
экран его значение и позицию в массиве."""
import sys
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


def show(obj):
    print(f'{type(obj)}, {sys.getsizeof(obj)}, {obj}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'itens'):
            for key, val in obj.itens():
                show(key)
                show(val)
        else:
            for item in obj:
                show(item)
print(show(a))

#Вес массива 912, каждый элемент 28, все элементы = 2800
#<class 'list'>, 912, [-64, 78, -43, -66, 41, -97, 78, 5, -60, -22, -61, 31, -55, 24, -22, -10, -7, 59, -75, -70, -42, -92, -20, 72, -98, 54, 48, 79, 14, 94, -56, -11, -75, -57, -12,
# -46, -22, -62, -24, -72, -50, 92, -67, -36, -92, 94, -73, -27, 80, 89, 61, -92, -98, 88, -35, -6, -31, 73, -21, 60, 54, 1, -75, 56, 6, 88, 68, -76, 1, 22, -57, -15, 99, 56, -71, 62,
# -1, -45, 85, 72, 17, -39, -48, 43, -83, -80, 85, -35, -93, -37, 45, -57, 25, 74, 68, 91, -79, -27, -57, -71]
# <class 'int'>, 28, -64
# <class 'int'>, 28, 78
# <class 'int'>, 28, -43
# <class 'int'>, 28, -66
# <class 'int'>, 28, 41
# <class 'int'>, 28, -97
# <class 'int'>, 28, 78
# <class 'int'>, 28, 5
# <class 'int'>, 28, -60
# <class 'int'>, 28, -22
# <class 'int'>, 28, -61
# <class 'int'>, 28, 31
# <class 'int'>, 28, -55
# <class 'int'>, 28, 24
# <class 'int'>, 28, -22
# <class 'int'>, 28, -10
# <class 'int'>, 28, -7
# <class 'int'>, 28, 59
# <class 'int'>, 28, -75
# <class 'int'>, 28, -70
# <class 'int'>, 28, -42
# <class 'int'>, 28, -92
# <class 'int'>, 28, -20
# <class 'int'>, 28, 72
# <class 'int'>, 28, -98
# <class 'int'>, 28, 54
# <class 'int'>, 28, 48
# <class 'int'>, 28, 79
# <class 'int'>, 28, 14
# <class 'int'>, 28, 94
# <class 'int'>, 28, -56
# <class 'int'>, 28, -11
# <class 'int'>, 28, -75
# <class 'int'>, 28, -57
# <class 'int'>, 28, -12
# <class 'int'>, 28, -46
# <class 'int'>, 28, -22
# <class 'int'>, 28, -62
# <class 'int'>, 28, -24
# <class 'int'>, 28, -72
# <class 'int'>, 28, -50
# <class 'int'>, 28, 92
# <class 'int'>, 28, -67
# <class 'int'>, 28, -36
# <class 'int'>, 28, -92
# <class 'int'>, 28, 94
# <class 'int'>, 28, -73
# <class 'int'>, 28, -27
# <class 'int'>, 28, 80
# <class 'int'>, 28, 89
# <class 'int'>, 28, 61
# <class 'int'>, 28, -92
# <class 'int'>, 28, -98
# <class 'int'>, 28, 88
# <class 'int'>, 28, -35
# <class 'int'>, 28, -6
# <class 'int'>, 28, -31
# <class 'int'>, 28, 73
# <class 'int'>, 28, -21
# <class 'int'>, 28, 60
# <class 'int'>, 28, 54
# <class 'int'>, 28, 1
# <class 'int'>, 28, -75
# <class 'int'>, 28, 56
# <class 'int'>, 28, 6
# <class 'int'>, 28, 88
# <class 'int'>, 28, 68
# <class 'int'>, 28, -76
# <class 'int'>, 28, 1
# <class 'int'>, 28, 22
# <class 'int'>, 28, -57
# <class 'int'>, 28, -15
# <class 'int'>, 28, 99
# <class 'int'>, 28, 56
# <class 'int'>, 28, -71
# <class 'int'>, 28, 62
# <class 'int'>, 28, -1
# <class 'int'>, 28, -45
# <class 'int'>, 28, 85
# <class 'int'>, 28, 72
# <class 'int'>, 28, 17
# <class 'int'>, 28, -39
# <class 'int'>, 28, -48
# <class 'int'>, 28, 43
# <class 'int'>, 28, -83
# <class 'int'>, 28, -80
# <class 'int'>, 28, 85
# <class 'int'>, 28, -35
# <class 'int'>, 28, -93
# <class 'int'>, 28, -37
# <class 'int'>, 28, 45
# <class 'int'>, 28, -57
# <class 'int'>, 28, 25
# <class 'int'>, 28, 74
# <class 'int'>, 28, 68
# <class 'int'>, 28, 91
# <class 'int'>, 28, -79
# <class 'int'>, 28, -27
# <class 'int'>, 28, -57
# <class 'int'>, 28, -71

# изменим решение , заменив список кортежем

minim = 0
a =[random.randint(-99, 99) for _ in range(100)]

a = tuple(a)

for i in a:
    if a[minim] > i:
        min_index = a.index(i)

if a[minim] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {a[minim]}.',
            f'Находится в массиве на позиции {minim}')

print(show(a))

#Используя кортеж массив a начал весить 848, вес каждого элемента  2796
#<class 'tuple'>, 848, (77, -1, 18, -14, -18, 91, 55, -74, -36, -97, -17, 46, 32, 24, 48, -21, 83, 86, 81, -37, 35, 39, -7, -67, 98, -39, 17, 66, -83, 11, -25, -64, -60, -2, 64, 43, 57, -28, 95, 60, 82, 77, 42, -14, 76, 92, -61, 88, -97, -9, -91, -23, 43, 18, 12, -87, 25, -65, -6, 59, -53, -73, -87, 55, 80, -58, 44, 17, 85, 37, -14, 13, 65, 31, -41, -50, 7, -87,
# -51, 57, -22, 15, -26, -9, 38, 77, 52, -78, -14, 23, 31, 59, 67, -57, 38, 61, 49, 27, -96, 91)
# <class 'int'>, 28, 77
# <class 'int'>, 28, -1
# <class 'int'>, 28, 18
# <class 'int'>, 28, -14
# <class 'int'>, 28, -18
# <class 'int'>, 28, 91
# <class 'int'>, 28, 55
# <class 'int'>, 28, -74
# <class 'int'>, 28, -36
# <class 'int'>, 28, -97
# <class 'int'>, 28, -17
# <class 'int'>, 28, 46
# <class 'int'>, 28, 32
# <class 'int'>, 28, 24
# <class 'int'>, 28, 48
# <class 'int'>, 28, -21
# <class 'int'>, 28, 83
# <class 'int'>, 28, 86
# <class 'int'>, 28, 81
# <class 'int'>, 28, -37
# <class 'int'>, 28, 35
# <class 'int'>, 28, 39
# <class 'int'>, 28, -7
# <class 'int'>, 28, -67
# <class 'int'>, 28, 98
# <class 'int'>, 28, -39
# <class 'int'>, 28, 17
# <class 'int'>, 28, 66
# <class 'int'>, 28, -83
# <class 'int'>, 28, 11
# <class 'int'>, 28, -25
# <class 'int'>, 28, -64
# <class 'int'>, 28, -60
# <class 'int'>, 28, -2
# <class 'int'>, 28, 64
# <class 'int'>, 28, 43
# <class 'int'>, 28, 57
# <class 'int'>, 28, -28
# <class 'int'>, 28, 95
# <class 'int'>, 28, 60
# <class 'int'>, 28, 82
# <class 'int'>, 28, 77
# <class 'int'>, 28, 42
# <class 'int'>, 28, -14
# <class 'int'>, 28, 76
# <class 'int'>, 28, 92
# <class 'int'>, 28, -61
# <class 'int'>, 28, 88
# <class 'int'>, 28, -97
# <class 'int'>, 28, -9
# <class 'int'>, 28, -91
# <class 'int'>, 28, -23
# <class 'int'>, 28, 43
# <class 'int'>, 28, 18
# <class 'int'>, 28, 12
# <class 'int'>, 28, -87
# <class 'int'>, 28, 25
# <class 'int'>, 28, -65
# <class 'int'>, 28, -6
# <class 'int'>, 28, 59
# <class 'int'>, 28, -53
# <class 'int'>, 28, -73
# <class 'int'>, 28, -87
# <class 'int'>, 28, 55
# <class 'int'>, 28, 80
# <class 'int'>, 28, -58
# <class 'int'>, 28, 44
# <class 'int'>, 28, 17
# <class 'int'>, 28, 85
# <class 'int'>, 28, 37
# <class 'int'>, 28, -14
# <class 'int'>, 28, 13
# <class 'int'>, 28, 65
# <class 'int'>, 28, 31
# <class 'int'>, 28, -41
# <class 'int'>, 28, -50
# <class 'int'>, 28, 7
# <class 'int'>, 28, -87
# <class 'int'>, 28, -51
# <class 'int'>, 28, 57
# <class 'int'>, 28, -22
# <class 'int'>, 28, 15
# <class 'int'>, 28, -26
# <class 'int'>, 28, -9
# <class 'int'>, 28, 38
# <class 'int'>, 28, 77
# <class 'int'>, 28, 52
# <class 'int'>, 28, -78
# <class 'int'>, 28, -14
# <class 'int'>, 28, 23
# <class 'int'>, 28, 31
# <class 'int'>, 28, 59
# <class 'int'>, 28, 67
# <class 'int'>, 28, -57
# <class 'int'>, 28, 38
# <class 'int'>, 28, 61
# <class 'int'>, 28, 49
# <class 'int'>, 28, 27
# <class 'int'>, 28, -96
# <class 'int'>, 28, 91

# Представим данные массива в виде множества

a =[random.randint(-99, 99) for _ in range(100)]

minim = 0 
for i in a:
    if a[minim] > i:
        minim = a.index(i)

if a[minim] >= 0:
    print(f'В массиве нет отрицательных элементов')
    a = set(a)
else:
    print(f'В массиве минимальный отрицательный элемент: {a[minim]}.',
            f'Находится в массиве на позиции {minim}')
    a = set(a)
print(show(a))




#<class 'set'>, 8416, {1, 2, 3, 7, 14, 16, 18, 19, 20, 23, 25, -98, -96, 33, 34, -94, 40, 42, 43, 44, -84, 46, 47, 45, -80, 50, 53, 57, 58, -69, -68, -67, -66, -65, 62, 60, -61, 69, -57, -56, -53, -51, -50, 79, 80, -49, 82, -45, -48, 81, -40, 89, -38, 91, 92, 90, -34, 96, 97, -30, -31, -32, 98, -26, -25, -23, -22, -21, -20, -16, -14, -10, -9, -7, -6, -5}
# <class 'int'>, 28, 1
# <class 'int'>, 28, 2
# <class 'int'>, 28, 3
# <class 'int'>, 28, 7
# <class 'int'>, 28, 14
# <class 'int'>, 28, 16
# <class 'int'>, 28, 18
# <class 'int'>, 28, 19
# <class 'int'>, 28, 20
# <class 'int'>, 28, 23
# <class 'int'>, 28, 25
# <class 'int'>, 28, -98
# <class 'int'>, 28, -96
# <class 'int'>, 28, 33
# <class 'int'>, 28, 34
# <class 'int'>, 28, -94
# <class 'int'>, 28, 40
# <class 'int'>, 28, 42
# <class 'int'>, 28, 43
# <class 'int'>, 28, 44
# <class 'int'>, 28, -84
# <class 'int'>, 28, 46
# <class 'int'>, 28, 47
# <class 'int'>, 28, 45
# <class 'int'>, 28, -80
# <class 'int'>, 28, 50
# <class 'int'>, 28, 53
# <class 'int'>, 28, 57
# <class 'int'>, 28, 58
# <class 'int'>, 28, -69
# <class 'int'>, 28, -68
# <class 'int'>, 28, -67
# <class 'int'>, 28, -66
# <class 'int'>, 28, -65
# <class 'int'>, 28, 62
# <class 'int'>, 28, 60
# <class 'int'>, 28, -61
# <class 'int'>, 28, 69
# <class 'int'>, 28, -57
# <class 'int'>, 28, -56
# <class 'int'>, 28, -53
# <class 'int'>, 28, -51
# <class 'int'>, 28, -50
# <class 'int'>, 28, 79
# <class 'int'>, 28, 80
# <class 'int'>, 28, -49
# <class 'int'>, 28, 82
# <class 'int'>, 28, -45
# <class 'int'>, 28, -48
# <class 'int'>, 28, 81
# <class 'int'>, 28, -40
# <class 'int'>, 28, 89
# <class 'int'>, 28, -38
# <class 'int'>, 28, 91
# <class 'int'>, 28, 92
# <class 'int'>, 28, 90
# <class 'int'>, 28, -34
# <class 'int'>, 28, 96
# <class 'int'>, 28, 97
# <class 'int'>, 28, -30
# <class 'int'>, 28, -31
# <class 'int'>, 28, -32
# <class 'int'>, 28, 98
# <class 'int'>, 28, -26
# <class 'int'>, 28, -25
# <class 'int'>, 28, -23
# <class 'int'>, 28, -22
# <class 'int'>, 28, -21
# <class 'int'>, 28, -20
# <class 'int'>, 28, -16
# <class 'int'>, 28, -14
# <class 'int'>, 28, -10
# <class 'int'>, 28, -9
# <class 'int'>, 28, -7
# <class 'int'>, 28, -6
# <class 'int'>, 28, -5
#Данный массив в итоге весит 2272, а элементы 2800
# Следовательно по хранению данных самым затратным является способ хранение во множестве, тк данная структура данных способна хранить элементы различных типов в одном массиве
#Самым экономичным в плане хранения выступает кортеж, тк в нем данные не изменяются, а значит не идут дополнительные затраты памяти на хранение
# Список также требует больше памяти, тк данные в нем способны изменяться
# Сумма веса всех массивов 10176
#Сумма веса всех элементов 8396
#Версия языка Pyrhon 3.7,4 система 64-bit, windows 7
