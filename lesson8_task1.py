# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa") -> 6
# func("sova") -> 9

import hashlib


def func(string):
    len_string = len(string)
    if len_string <= 1:
        return 0

    subs_set = set()
    for len_sub in range(1, len_string):
        for ind in range(len_string - len_sub + 1):
            subs_set.add(hashlib.sha256(string[ind:ind + len_sub].encode('utf-8')).hexdigest())

    return len(subs_set)


print(func('papa'))
print(func('sova'))
