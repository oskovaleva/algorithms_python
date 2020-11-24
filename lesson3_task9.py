# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

ROWS_NUM = 3
COLUMNS_NUM = 4
MIN_ITEM = -10
MAX_ITEM = 100
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(COLUMNS_NUM)] for _ in range(ROWS_NUM)]
for row in array:
    for el in row:
        print(f"{el:>5}", end='')
    print()

max_min_per_col = None
for i in range(len(array[0])):
    min_per_col = None
    for j in range(len(array)):
        if min_per_col is None or min_per_col > array[j][i]:
            min_per_col = array[j][i]
    if max_min_per_col is None or max_min_per_col < min_per_col:
        max_min_per_col = min_per_col
print(f"Максимальный элемент среди минимальных элементов столбцов матрицы: {max_min_per_col}")
