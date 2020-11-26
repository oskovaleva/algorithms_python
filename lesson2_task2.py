# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input("Введите натуральное число: "))

even_num_count = 0
uneven_num_count = 0

while n > 0:
    if n % 2 == 0:
        even_num_count += 1
    else:
        uneven_num_count += 1
    n //= 10

print(f"Ваше число содержит {even_num_count} четные цифры и {uneven_num_count} нечетные.")
