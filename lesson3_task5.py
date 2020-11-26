# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание
# к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)

max_neg = None
for i in [j for j in array if j < 0]:
    if max_neg is None or i > max_neg:
        max_neg = i
print(f"Максимальный отрицательный элемент: {max_neg}")
