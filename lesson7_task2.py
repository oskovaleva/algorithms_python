# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    arr1 = merge_sort(arr[:(len(arr) // 2)])
    arr2 = merge_sort(arr[(len(arr) // 2):])
    index1, index2 = 0, 0
    while index1 < len(arr1) or index2 < len(arr2):
        if index2 == len(arr2) or index1 < len(arr1) and arr1[index1] <= arr2[index2]:
            arr[index1 + index2] = arr1[index1]
            index1 += 1
        else:
            arr[index1 + index2] = arr2[index2]
            index2 += 1

    return arr


array = [random.random() * 50 for _ in range(10)]
print([round(i, 2) for i in array])

array = merge_sort(array)
print([round(i, 2) for i in array])
