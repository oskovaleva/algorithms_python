# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


# Усложнила задачу и реализовала более универсальное решение: количество чисел (n >= 2) вводит пользователь.
def sum_(elements_tpl: tuple, num1: deque, num2: deque, *args):
    elements_count = len(elements_tpl)
    nums = [num.copy() for num in [num1, num2, *args]]
    pos_count = max([len(num) for num in nums])

    for num in nums:
        while len(num) < pos_count:
            num.appendleft('0')

    div_ = 0
    total = deque()
    while pos_count > 0 or div_ > 0:
        tmp = sum([elements_tpl.index(num.pop()) for num in nums]) if pos_count > 0 else 0
        div_, mod_ = divmod(tmp + div_, elements_count)
        total.appendleft(elements_tpl[mod_])
        pos_count -= 1
    return total


def multiply(elements_tpl: tuple, num1: deque, num2: deque, *args):
    if num1 == deque() or num2 == deque():
        return deque()

    nums = deque([num.copy() for num in [num1, num2, *args]])
    c1, c2 = nums.popleft(), nums.popleft()
    elements_count = len(elements_tpl)

    nums_to_sum = []
    for el in range(len(c2)):
        c = c1.copy()
        result = deque()
        digits_count = len(c)
        digit = elements_tpl.index(c2.pop())
        div_ = 0

        while digits_count > 0:
            div_, mod_ = divmod(elements_tpl.index(c.pop()) * digit + div_, elements_count)
            result.appendleft(elements_tpl[mod_])
            digits_count -= 1
        if div_ > 0:
            result.appendleft(elements_tpl[div_])

        result.extend(['0'] * el)
        nums_to_sum.append(result)

    total = nums_to_sum[0] if len(nums_to_sum) == 1 else sum_(elements_tpl, *nums_to_sum)

    if len(nums) == 0:
        return total
    else:
        nums.appendleft(total)
        return multiply(elements_tpl, *nums)


if __name__ == '__main__':
    elements = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

    numbers = []
    numbers_count = int(input('Сколько чисел вы хотите сложить и перемножить (введите натуральный n > 1)? '))
    for i in range(numbers_count):
        numbers.append(deque(input(f'Введите {i + 1}-е число в 16-ричной системе >>> ').upper()))
    print(sum_(elements, *numbers))
    print(multiply(elements, *numbers))
