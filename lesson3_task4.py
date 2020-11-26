# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

freq_num = None
freq_count = 0
for i in set(array):
    count_ = 0
    for j in array:
        if j == i:
            count_ += 1
    if freq_count < count_:
        freq_count = count_
        freq_num = i

print(f"Число {freq_num} встречается в массиве чаще всего.")
