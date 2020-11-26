# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков. Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Выбранная задача: lesson2_task4
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...

import timeit
import cProfile


# Вариант 1. Цикл for.
def total_loop(n):
    el = 1
    total = 1
    for i in range(1, n):
        el /= -2
        total += el
    return total


print(timeit.timeit("total_loop(10)", number=100, globals=globals()))   # 0.00012486599999999431
print(timeit.timeit("total_loop(20)", number=100, globals=globals()))   # 0.00020644799999999797
print(timeit.timeit("total_loop(40)", number=100, globals=globals()))   # 0.00032715999999999995
print(timeit.timeit("total_loop(80)", number=100, globals=globals()))   # 0.000632083999999998
print(timeit.timeit("total_loop(160)", number=100, globals=globals()))  # 0.001204344000000003
print(timeit.timeit("total_loop(320)", number=100, globals=globals()))  # 0.002162775999999998
print(timeit.timeit("total_loop(640)", number=100, globals=globals()))  # 0.004629250000000001

cProfile.run("total_loop(1000)")
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 lesson4_task1.py:17(total_loop)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_loop(10000)")
#       4 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.001    0.001    0.001    0.001 lesson4_task1.py:17(total_loop)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_loop(100000)")
#       4 function calls in 0.007 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#      1    0.007    0.007    0.007    0.007 lesson4_task1.py:17(total_loop)
#      1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_loop(1000000)")
#       4 function calls in 0.061 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.061    0.061 <string>:1(<module>)
#      1    0.061    0.061    0.061    0.061 lesson4_task1.py:17(total_loop)
#      1    0.000    0.000    0.061    0.061 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 2. Рекурсия (без меморизации).
def total_recursion(n):
    if n == 1:
        return 1
    return 1 / ((-2) ** (n - 1)) + total_recursion(n - 1)


print(timeit.timeit("total_recursion(10)", number=100, globals=globals()))   # 0.0004400129999999891
print(timeit.timeit("total_recursion(20)", number=100, globals=globals()))   # 0.0009684459999999839
print(timeit.timeit("total_recursion(40)", number=100, globals=globals()))   # 0.0020199239999999785
print(timeit.timeit("total_recursion(80)", number=100, globals=globals()))   # 0.004559011000000002
print(timeit.timeit("total_recursion(160)", number=100, globals=globals()))  # 0.011305705999999999
print(timeit.timeit("total_recursion(320)", number=100, globals=globals()))  # 0.025363951999999995
print(timeit.timeit("total_recursion(640)", number=100, globals=globals()))  # 0.06107879199999999

cProfile.run("total_recursion(100)")
#       103 function calls (4 primitive calls) in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  100/1    0.000    0.000    0.000    0.000 lesson4_task1.py:77(total_recursion)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_recursion(500)")
#       503 function calls (4 primitive calls) in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#  500/1    0.001    0.000    0.001    0.001 lesson4_task1.py:77(total_recursion)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_recursion(800)")
#       803 function calls (4 primitive calls) in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#  800/1    0.001    0.000    0.001    0.001 lesson4_task1.py:77(total_recursion)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 3. Рекурсия (с меморизацией).
def total_recursion_memory(n):
    total_list = [1]

    def _total_memory(n):
        if n <= len(total_list):
            return total_list[n - 1]
        total_list.append(1 / ((-2) ** (n - 1)) + _total_memory(n - 1))
        return total_list[n - 1]

    return _total_memory(n)


print(timeit.timeit("total_recursion_memory(10)", number=100, globals=globals()))   # 0.0006343389999999838
print(timeit.timeit("total_recursion_memory(20)", number=100, globals=globals()))   # 0.0013192529999999925
print(timeit.timeit("total_recursion_memory(40)", number=100, globals=globals()))   # 0.0027101200000000103
print(timeit.timeit("total_recursion_memory(80)", number=100, globals=globals()))   # 0.006450567000000018
print(timeit.timeit("total_recursion_memory(160)", number=100, globals=globals()))  # 0.014005759000000007
print(timeit.timeit("total_recursion_memory(320)", number=100, globals=globals()))  # 0.03369376000000002
print(timeit.timeit("total_recursion_memory(640)", number=100, globals=globals()))  # 0.07624898700000005

cProfile.run("total_recursion_memory(100)")
#       303 function calls (204 primitive calls) in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 lesson4_task1.py:124(total_recursion_memory)
#  100/1    0.000    0.000    0.000    0.000 lesson4_task1.py:127(_total_memory)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    100    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_recursion_memory(500)")
#       1503 function calls (1004 primitive calls) in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.000    0.000    0.001    0.001 lesson4_task1.py:124(total_recursion_memory)
#  500/1    0.001    0.000    0.001    0.001 lesson4_task1.py:127(_total_memory)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#    500    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_recursion_memory(800)")
#       2403 function calls (1604 primitive calls) in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1    0.000    0.000    0.002    0.002 lesson4_task1.py:124(total_recursion_memory)
#  800/1    0.002    0.000    0.002    0.002 lesson4_task1.py:127(_total_memory)
#      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#    800    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    799    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 4 (не интересный для анализа, но самый оптимальный). Формула суммы геометрической прогрессии.
def total_formula(n, first, mult):
    return n * first if mult == 1 else (first * (1 - mult ** n))/(1 - mult)


print(timeit.timeit("total_formula(10, 1, -0.5)", number=100, globals=globals()))   # 3.958700000000759e-05
print(timeit.timeit("total_formula(20, 1, -0.5)", number=100, globals=globals()))   # 2.6356000000005153e-05
print(timeit.timeit("total_formula(40, 1, -0.5)", number=100, globals=globals()))   # 2.6431999999992906e-05
print(timeit.timeit("total_formula(80, 1, -0.5)", number=100, globals=globals()))   # 2.632800000001989e-05
print(timeit.timeit("total_formula(160, 1, -0.5)", number=100, globals=globals()))  # 2.6273999999992803e-05
print(timeit.timeit("total_formula(320, 1, -0.5)", number=100, globals=globals()))  # 2.637999999999252e-05
print(timeit.timeit("total_formula(640, 1, -0.5)", number=100, globals=globals()))  # 2.6149000000003086e-05

cProfile.run("total_formula(1000, 1, -0.5)")
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 lesson4_task1.py:125(total_formula)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_formula(10000, 1, -0.5)")
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 lesson4_task1.py:125(total_formula)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_formula(100000, 1, -0.5)")
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 lesson4_task1.py:125(total_formula)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run("total_formula(1000000, 1, -0.5)")
#       4 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 lesson4_task1.py:125(total_formula)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Выводы.
# Были рассмотрены 4 варианта решения задачи: с помощью цикла, рекурсии (с меморизацией и без) и формулы суммы
# геометрической прогрессии.
# Замеры с помощью инструмента timeit проводились for n in (10, 20, 40, 80, 160, 320, 640).
# Замеры с помощью инструмента cProfile проводились for n in (1000, 10000, 100000, 1000000), кроме рекурсий
# (для них замеры проводились for n in (100, 500, 800), чтобы исключить ошибку переполнению стека).
# Первые три варианта похожи на линейную зависимость (O(n)), но рекурсии работают менее эффективно: они более медленные,
# коэффициент k в них явно выше. Кроме того, у них присутствует ограничение на максимальное значение n.
# Рекурсия с меморизацией медленнее рекурсии без нее: в обоих случаях зависимость линейная, но меморизация увеличивает
# количество выполняемых действий и потребляемой памяти. Наиболее оптимальный вариант (немного читерский и не интересный
# для анализа) с формулой геометрической прогрессии выполняется за константное время (O(1)).
