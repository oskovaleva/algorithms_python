# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте
# метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random


def median_calc(arr):
    for i in range(len(arr)):
        lower = higher = 0
        equal = -1

        for j in range(len(arr)):
            if arr[j] > arr[i]:
                higher += 1
            elif arr[j] < arr[i]:
                lower += 1
            else:
                equal += 1

        if abs(higher - lower) <= equal:
            return arr[i]


m = 5
array = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(array)

median = median_calc(array)
print(f'{median=}')

# check
array.sort()
print(array, median == array[len(array) // 2])
