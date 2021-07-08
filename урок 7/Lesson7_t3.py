
""" Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, 
делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы."""

import random
m = random.randint(2, 12)
lenght = 2 * m + 1

array  = [random.randint(0, 30) for _ in range(lenght)]
#алгоритм для сортировки
def tree(nums, tree_l, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < tree_l and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < tree_l and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        tree(nums, tree_l, largest)


def tree_sort(data):
    n = len(data)

    for i in range(n, -1, -1):
        tree(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        tree(data, i, 0)
print(array)
tree_sort(array)
print(array)
# алгоритм для нахождения медианы

def median(lists):
    n = len(lists)
    index = n // 2
    if n % 2:
        return lists[index]
    return sum(lists[index - 1:index + 1]) / 2
    
print('Медиана массива:', array,'число ', median(array))