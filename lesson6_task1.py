# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили
# творчество, фантазию и создали универсальный код для замера памяти.

# Выбранная задача: lesson2_task4  # та же, которая анализировалась в уроке 4
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.

import sys


def memory_count(x):
    count = sys.getsizeof(x)
    if hasattr(x, '__iter__') and not isinstance(x, str):
        if hasattr(x, 'items'):
            for key, value in x.items():
                count += memory_count(key)
                count += memory_count(value)
        else:
            for item in x:
                count += sys.getsizeof(item)
    return count


n = int(input("Введите натуральное число: "))  # одинаковое для всех реализаций

print('Версия python 3.8, разрядность OS 64-bit')
memory_total = [memory_count(n) for i in range(3)]

print('Вариант 1. Цикл for.')
el = 1
total = 1

memory_tmp = (memory_count(el), memory_count(total))

for i in range(1, n):
    el /= -2
    total += el

# print(total)

for num, item in enumerate([el, total, i, range(1, n)]):
    memory_total[0] += max(memory_count(item), memory_tmp[num] if num < len(memory_tmp) else 0)
print(f'Затраты по памяти: {memory_total[0]}')  # 2932

print('Вариант 2. Рекурсия.')


def total_recursion(n):
    global memory_total
    if n == 1:
        for i in [n == 1, 1]:
            memory_total[1] += memory_count(i)
        return 1
    tmp = 1 / ((-2) ** (n - 1))
    new_n = n - 1
    for i in [n == 1, tmp, new_n]:
        memory_total[1] += memory_count(i)
    return tmp + total_recursion(new_n)


total = total_recursion(n)
# print(total)

memory_total[1] += total
print(f'Затраты по памяти: {memory_total[1]:.2f}')  # 7608.67

print('Вариант 3. Формула суммы геометрической прогрессии.')


def total_formula(n, first, mult):  # общая формула суммы геометрической прогрессии
    global memory_total
    for i in [first, mult, n * first, mult == 1, (first * (1 - mult ** n))/(1 - mult)]:
        memory_total[2] += memory_count(i)

    return n * first if mult == 1 else (first * (1 - mult ** n))/(1 - mult)


first = 1
mult = -0.5
total = total_formula(n, first, mult)
# print(total)

print(f'Затраты по памяти: {memory_total[2]}')  # 156

# Вывод.
# Были рассмотрены 3 варианта решения задачи: с помощью цикла, рекурсии и формулы суммы геометрической прогрессии.
# Наиболее оптимальный вариант - расчет по готовой формуле, поскольку для него не нужно запоминать множество
# дополнительных переменных. Наименее оптимальный вариант - рекурсия, так как нужно хранить в памяти все промежуточные
# значения (каждый уже посчитанный элемент прогрессии), в отличие от цикла, операции в теле которого изменяют уже
# существующие переменные, не увеличивая затраты по памяти.
