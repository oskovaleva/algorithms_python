# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def total(a):
    if a < 10:
        return a
    return a % 10 + total(a // 10)


max_sum = 0
num_out = 0
while True:
    num_in = int(input("Введите натуральное число (чтобы выйти, введите 0): "))
    if num_in == 0:
        break
    sum_in = total(num_in)
    if sum_in > max_sum:
        max_sum = sum_in
        num_out = num_in

print(f"Число с наибольшей суммой цифр: {num_out}. Сумма его цифр: {max_sum}.")
