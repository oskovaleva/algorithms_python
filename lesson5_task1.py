# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

companies = defaultdict(int)
n = int(input('Введите количество предприятий >>> '))

for i in range(n):
    name = input(f'Введите название предприятия {i + 1} >>> ')
    for j in range(4):
        profit = float(input(f'Введите прибыль за {j + 1}-й квартал >>> '))
        companies[name] += profit

avg_profit = sum(companies.values()) / len(companies)
print(f'Средняя прибыль: {avg_profit:.2f}')

print('Компании с прибылью выше среднего:')
for key, value in companies.items():
    if value > avg_profit:
        print(key)

print('Компании с прибылью ниже среднего:')
for key, value in companies.items():
    if value < avg_profit:
        print(key)
