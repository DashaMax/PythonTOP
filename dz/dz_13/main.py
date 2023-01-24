''' Замена символа на другой символ в строке на четных позициях. '''


def change_symbol_func(s: str, start: str, end: str) -> str:
    '''
    Заменяет символ строки на новый только на чётных позициях.

    :param s: строка, в которой нужно выполнить замену
    :param start: символ, который нужно заменить
    :param end: символ, на который нужно заменить
    :return: новая строка
    '''

    s_new = ''

    for i, item in enumerate(s):
        if item == start and not i % 2:
            s_new += end
            continue
        s_new += item

    return s_new


str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
print(str1, change_symbol_func(str1, 'N', 'P'), sep='\n')





''' Удаление из слова буквы, заданной номером позиции. '''


# s = 'Python'
# print(s)
# n = int(input('Удалить символ №\n-> '))
# s_new = s[:n - 1] + s[n:]
# print(s_new)





''' Удаление всех вхождений заданного символа из строки. '''


# s = '012345263738494'
# print(s)
# n = input('Удалить символ:\n-> ')
# s_new = [x for x in s if x != n]
# print(*s_new, sep='')





''' Написать функцию перевода десятичного числа в двоичное (без использования встроенной функции). '''


# import math
#
#
# def dec_to_bin_func(n: int) -> str:
#     '''
#     Переводит из десятичной СС в двоичную.
#
#     :param n: положительное или равное нулю число
#     :return: строка, двоичное число
#     '''
#
#     n_bin = ''
#
#     if n > 0:
#         pow_ = int(math.log(n, 2))
#
#         for j in range(pow_, -1, -1):
#             if 2 ** j <= n:
#                 n_bin += '1'
#                 n -= 2 ** j
#             else:
#                 n_bin += '0'
#
#     elif n == 0:
#         n_bin = '0000'
#
#     if len(n_bin) < 4:
#         n_bin = '0' * (4 - len(n_bin)) + n_bin
#
#     return n_bin
#
#
# print(dec_to_bin_func(int(input('-> '))))










