# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

ROWS_NUM = 5
COLUMNS_NUM = 4
array = []

for i in range(ROWS_NUM):
    row = []
    for j in range(1, COLUMNS_NUM):
        row.append(int(input(f"Введите элемент {j} строки {i + 1}: ")))
    array.append(row)

for row in array:
    sum_row = 0
    for el in row:
        sum_row += el
        print(f"{el:>5}", end='')
    row.append(sum_row)
    print(f"{sum_row:>5}")
