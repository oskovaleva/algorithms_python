# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import math
import timeit
import cProfile


# 1. Решето Эратосфена.
def sieve(n):
    if n == 1:
        return 2

    # Для целей оптимизации вместо натуральных чисел буду генерировать решето с единицами, причем не для всех чисел, а
    # только для нечетных, начиная с 3 (все четные можно сразу отбросить, вдвое сократив затраты по выделяемой памяти).
    # sieve_len = n * 9  # этого варианта достаточно для поиска примерно 10 млн простых чисел
    sieve_len = int(math.log10(n * 1.3) * (n * 1.3))  # наиболее близкий вариант, который получилось найти эмпирически
    sieve_lst = [1] * sieve_len
    for i in range(sieve_len):
        if sieve_lst[i] == 1:
            j = i + i * 2 + 3  # i * 2 + 3 - здесь и ниже корректировка индекса из-за выбора нечетных чисел, начиная с 3
            while j < sieve_len:
                sieve_lst[j] = 0
                j += i * 2 + 3

    sum_ = 1  # чтобы получить итоговый ответ, считаю индекс, в котором сумма единиц станет равна n
    for i in range(sieve_len):
        sum_ += sieve_lst[i]
        if sum_ >= n:
            return i * 2 + 3


print(timeit.timeit("sieve(10)", number=100, globals=globals()))     # 0.00046028700000000367
print(timeit.timeit("sieve(100)", number=100, globals=globals()))    # 0.008434233999999999
print(timeit.timeit("sieve(1000)", number=100, globals=globals()))   # 0.133309704
print(timeit.timeit("sieve(10000)", number=100, globals=globals()))  # 2.103173601

cProfile.run('sieve(100)')
#       5 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 lesson4_task2.py:15(sieve)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method math.log10}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(1000)')
#       5 function calls in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1    0.002    0.002    0.002    0.002 lesson4_task2.py:15(sieve)
#      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method math.log10}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(10000)')
#       5 function calls in 0.024 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#      1    0.024    0.024    0.024    0.024 lesson4_task2.py:15(sieve)
#      1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method math.log10}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 2. Классический способ проверки числа на простоту.
def prime(n):
    ind, num = 1, 2
    while ind < n:
        num += 1
        for i in range(2, math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            ind += 1
    else:
        return num


print(timeit.timeit("prime(10)", number=100, globals=globals()))     # 0.0018462009999999987
print(timeit.timeit("prime(100)", number=100, globals=globals()))    # 0.036267072
print(timeit.timeit("prime(1000)", number=100, globals=globals()))   # 0.724702127
print(timeit.timeit("prime(10000)", number=100, globals=globals()))  # 18.742257802

cProfile.run('prime(100)')
#       1082 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.001    0.001    0.001    0.001 test3.py:7(prime)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#    539    0.000    0.000    0.000    0.000 {built-in method math.floor}
#    539    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(1000)')
#       15838 function calls in 0.012 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#      1    0.010    0.010    0.012    0.012 test3.py:7(prime)
#      1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#   7917    0.001    0.000    0.001    0.000 {built-in method math.floor}
#   7917    0.001    0.000    0.001    0.000 {built-in method math.sqrt}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(10000)')
#       209458 function calls in 0.261 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.261    0.261 <string>:1(<module>)
#      1    0.233    0.233    0.261    0.261 test3.py:7(prime)
#      1    0.000    0.000    0.261    0.261 {built-in method builtins.exec}
# 104727    0.015    0.000    0.015    0.000 {built-in method math.floor}
# 104727    0.013    0.000    0.013    0.000 {built-in method math.sqrt}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
