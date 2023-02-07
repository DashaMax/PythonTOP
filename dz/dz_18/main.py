''' Есть список из 10 элементов, заполненный случайными числами.
    Необходимо найти число, введенное пользователем.
    Используйте алгоритм бинарного поиска.
'''


from random import randint
from time import time


def binary_search(l: list, n: int) -> str:
    while l:
        i = (len(l) - 1) // 2

        if l[i] == n:
            return f'Число {n} в списке присутствует'

        elif l[i] > n:
            l = l[:i]

        else:
            l = l[i + 1:]

    return f'Число {n} в списке отсутствует'


numbers_list = [randint(-100, 100) for _ in range(10)]
numbers_list.sort()
print(numbers_list)
user_num = int(input('Введите число: '))
time_start = time()
print(binary_search(numbers_list, user_num))
time_finish = time()
print('Время работы алгоритма:', round(time_finish - time_start, 4))