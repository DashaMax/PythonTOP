# name = 'Dasha'
# print('Hello,', name + '!')
# print(type(name))
# PI = 3.14
# print(PI)
#
# a, b = 1, 2
# print(a, b)
# a, b = b, a
# print(a, b)

# Перенос
# text = 'dskls' \
#        'fdg'
# print(text)


# print('Document \'file.py\' \t\rfound path \nD:\\Python\\file.py')


# a = 5
# b = 7
# c = 3
# summa = a + b + c
# multy = a * b * c
# mean = summa / 3
# print('Написать программу нахождения суммы, произведения и среднего арифметического трёх чисел: 5, 7, 3')
# print('Сумма:', summa)
# print('Произведение:', multy)
# print('Среднее арифметическое:', mean)


# a = 4321
# a_new = a % 10 * 1000 + a // 10 % 10 * 100 + a // 100 % 10 * 10 + a // 1000 % 10
# print(a_new)


# print('Введите четыре числа:')
# n1 = int(input('1: '))
# n2 = int(input('2: '))
# n3 = int(input('3: '))
# n4 = int(input('4: '))
# summa_1 = n1 + n2
# summa_2 = n3 + n4
# div = summa_1 / summa_2
# print(round(div, 2))


# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))
#
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or b == c or a == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')


# day = int(input('Day (digit): '))
# if 1 <= day <= 5:
#     print('Working day')
# elif day >= 6 and day <= 7:
#     print('Holiday')
# else:
#     print('Error! Again')


# month = int(input('Number month (digit): '))
# if 3 <= month <= 5:
#     print('Spring')
# elif 6 <= month <= 8:
#     print('Summer')
# elif 9 <= month <= 11:
#     print('Autumn')
# elif 1 <= month <= 2 or month == 12:
#     print('Winter')
# else:
#     print('Error!')


#
# n = int(input('Count: '))
# if n == 1:
#     print(f'На ветке {n} ворона')
# elif 2<=n<=4:
#     print(f'На ветке {n} вороны')
# elif 5<=n<=9 or n == 0:
#     print(f'На ветке {n} ворон')
# else:
#     print('Много ворон!')


# a, b = 40, 20
# # min_ = 'a = b' if a == b else 'a < b' if a < b else 'b < a'
# # print(min_)
#
#
# del_ = a/b if b else 'Error: b = 0!'
# print(del_)


# try:
#     n = int(input())
#     m = int(input())
#     print(n * 2)
#     print(n/m)
# except (ValueError, ZeroDivisionError):
#     print('Error!')
# else:
#     print('OK!')
# finally:
#     print('Working!')


# n = input('First number: ')
# m = input('Second number: ')
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# i = 1
# while i < 21:
#     print(i+1)
#     i += 2


# n = int(input())
# print('*'*n)


# start = int(input('Start: '))
# end = int(input('End: '))
# sum_ = 0
#
# while start <= end:
#     if start % 2:
#         sum_ += start
#     start += 1
# print('Summa:', sum_)


# n = input('Input: ')
#
# while type(n) is str:
#     try:
#         n = int(n)
#         if n % 2:
#             print('Odd number')
#         else:
#             print('Even number')
#     except ValueError:
#         n = input('Input integer number: ')


# n = int(input('Input number: '))
# multi = 1
#
# while n:
#     multi *= n
#     n = int(input('Input number: '))
# else:
#     print('End n:', n)
# print('Result:', multi)


# while n >= 0:
#     print(n)
#     n = int(input())





# n = int(input('Input count numbers: '))
# i = 0
# sum_ = 0
# min_ = None
# max_ = None
#
# while i < n:
#     d = float(input('Input number: '))
#
#     if min_ is None:
#         min_ = int(d)
#
#     elif d < min_:
#         min_ = int(d)
#
#     if max_ is None:
#         max_ = int(d)
#
#     elif d > max_:
#         max_ = int(d)
#
#     sum_ += d
#     i += 1
#
# print('Count:', n)
# print('Max:', max_)
# print('Min:', min_)
# print('Mean:', round(sum_ / n, 2))




# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#
#         if j == 9:
#             print(f'{i} * {j} = {i * j}')
#         else:
#             print(f'{i} * {j} = {i * j}', end='\t\t')
#         j += 1
#     i += 1





# for i in range(10, 30):
#     if not i % 11:
#         break
#     print(i, end=' ')
# else:
#     print('END')






# len_ = int(input('Len: '))
# wight = int(input('Wight: '))
#
# for w in range(wight):
#     for l in range(len_):
#         print('*', end='')
#     print()




# wight = int(input('Wight: '))
# height = int(input('Height: '))
#
# for h in range(height):
#     for w in range(wight):
#
#         if h == 0 or h == height - 1 or w == 0 or w == wight - 1:
#             print('* ' , end='')
#
#         else:
#             print('  ', end='')
#
#     print()





# n = int(input('Count: '))
# list_ = [int(input('-> ')) for i in range(n)]
# sum_ = 0
#
# for i in list_:
#     sum_ += i if i < 0 else 0
#
# print('Summa:', sum_)



# list_ = list(range(21, 41))
# count = 0
# sum_ = 0
#
# for i in list_:
#     count += 1 if not i % 2 else 0
#     sum_ += i if i % 2 else 0
#
# print(list_)
# print('Count:', count)
# print('Summa:', sum_)





# list_ = [int(input('-> ')) for i in range(int(input('Count: ')))]
# count = 0
# sum_ = 0
#
# for i in list_:
#     count += 1 if i else 0
#     sum_ += i
#
# mean = sum_ / count
# print('Mean:', mean)



# list_ = [int(input('-> ')) for i in range(int(input('n: ')))]
#
# for i in range(1, len(list_)):
#     if list_[i] > list_[i-1]:
#         print(list_[i], end=' ')





# l = list(range(1, 8))
# print(l)
# print(l[::-1])
# print(l[::2])
# print(l[1::2])
# print(l[:1])
# print(l[-1:])
# print(l[3:4])
# print(l[-3::])
# print(l[4:1:-1])
# print(l[2:5])





# n = int(input('Кол-во элементов списка: '))
# lst = []
#
# for i in range(n):
#     d = int(input('Введите число кратное 3: '))
#     lst.append(d) if not d % 3 else print(d, 'не делится на 3 без остатка')
#
# print(lst)






# a = list(range(10, 20))
# b = list(range(15, 25))
# c = [i for i in a for j in b if i == j]
# print(c)





# l1 = [1, 2, 3, 56, 78, 0, 9]
# l2 = [11, 22, 33, 4, 5]
# l_new = []
#
# if len(l1) > len(l2):
#     l2, l1 = l1, l2
#
# for i in range(len(l1)):
#     l_new.append(l1[i])
#     l_new.append(l2[i])
#
#     if i == len(l1) - 1:
#         l_new.extend(l2[i+1:])
#
# print(l_new)





# list_ = [int(input('-> ')) for _ in range(int(input('Elements:\nn = ')))]
# k = int(input('Index:\nk = '))
# list_.pop(k)
# print(list_)



# list_ = [2, 9, 7, 9, 0, 9, 9, 21, 67, 7, 2, 0, 2]
# list_.sort()     # сортирует по возрастанию
# print(list_)
#
# list_.sort(reverse=True)    # сортирует по убыванию
# print(list_)
#
# l = ['a', 'bb', 'cccc', 'ddd']
# l.sort(key=len)
# print(l)
#
# b = sorted(list_)   # встроенная функция python
# print(b)






import random

# print(random.random())
# print(random.randint(0, 20))
# print(random.randrange(10))
# print(random.uniform(-2, 2))
# print(random.choice(['a', 'gfd', 'bbbb']))
# print(random.choices(['a', 'gfd', 'bbbb'], k=2))

# l = [round(random.uniform(-10, 10), 3) for _ in range(10)]
# print(l)






# list_ = [random.randint(0, 100) for _ in range(10)]
# print(list_)
# max_ = max(list_)
# print('Max:', max_)
# list_.remove(max_)
# list_.insert(0, max_)
# print(list_)





# list_ = [random.randint(-20, 20) for _ in range(10)]
# print(list_)
# list_.sort(reverse=True)
# print(list_)






# list_ = [random.randint(0, 100) for _ in range(10)]
# print(list_)
# min_ = min(list_)
# print('Min:', min_)
# index_min = list_.index(min_)
# print('Index min:', index_min)
# del list_[:index_min]
# print(list_)






# list_1 = [random.randint(0, 10) for _ in range(int(input('n1 = ')))]
# list_2 = [random.randint(0, 10) for _ in range(int(input('n2 = ')))]
# print('List 1:', list_1)
# print('List 2:', list_2)
# list_3 = list_1 + list_2
# print('List 3:', list_3)
# list_3 = []
#
# for element in list_1:
#     if element not in list_3:
#         list_3.append(element)
#
# for element in list_2:
#     if element not in list_3:
#         list_3.append(element)
#
# print('List 3:', list_3)
#
# list_3 = []
#
# for element in list_1:
#     if element in list_2 and element not in list_3:
#         list_3.append(element)
#
# print('List 3:', list_3)
# list_3 = [min(list_1), min(list_2), max(list_1), max(list_2)]
# print('List 3:', list_3)






# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# for row in matrix:
#     for elem in row:
#         print(elem, end='\t\t')
#     print()
#
# print()
#
# for row in matrix:
#     for elem in row:
#         print(elem ** 2, end='\t\t')
#     print()







# matrix = [[i * j for i in range(1, 11)] for j in range(1, 11)]
# [[print(matrix[row][col], end = '\n' if col == 9 else '\t') for col in range(len(matrix[row]))] for row in range(len(matrix))]
# for row in matrix:
#     for elem in row:
#         print(elem, end='\t')
#     print()









# from math import pi
#
#
# R = int(input('R = '))
# C = round(2 * pi * R, 2)
# print('C =', C)









# import time
# import locale     # Локальные настройки
#
#
# locale.setlocale(locale.LC_ALL, 'ru')
#
# print(time.strftime('Today is %d.%m.%Y\nTime is %H:%M:%S'))
# print(time.strftime('%B'))
#
# start = time.monotonic()
# time.sleep(5)
# end = time.monotonic()
# print(end - start)







# def func(n, a, b):
#     [print(b, end='') if i % 2 else print(a, end='') for i in range(n)]
#     print()
#
#
# func(9, '+', '-')
# func(7, 'X', '0')









# def diff(n1, n2):
#     return True if n1 > n2 else False
#
#
# a, b = int(input('a = ')), int(input('b = '))
#
# if diff(a, b):
#     print('Result: a - b =', a - b)
# else:
#     print('Result: a + b =', a + b)






# def func_cube(x):
#     return x ** 3
#
#
# for i in range(1, 11):
#     print(i, 'in cube =', func_cube(i))




# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     lst.insert(0, lst.pop(-1))
#     lst.append(lst.pop(1))
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105, 0, 12, -78]))
# print(change(['s', 'l', 'o', 'n']))







# def check_password(password):
#     has_upper = False
#     has_digit = False
#     has_lower = False
#
#     for i in password:
#
#         if i.isupper():
#             has_upper = True
#
#         if i.isdigit():
#             has_digit = True
#
#         if i.islower():
#             has_lower = True
#
#
#
#     if len(password) >= 8 and has_upper and has_digit and has_lower:
#         return True
#
#     return False
#
#
# password_ = input('Password: ')
#
# if check_password(password_):
#     print('Password is good :)')
#
# else:
#     print('Password is bad :(')










# def func(n=20, sym='-'):
#     print(sym * n)
#
#
# func(10, '+')
# func(5, '*')
# func(15, '#')
# func(7, '-')
# func()






# def func(n, even=True):
#
#     if even:
#         sum_ = sum([int(x) for x in str(n) if not int(x) % 2])
#
#     else:
#         sum_ = sum([int(x) for x in str(n) if int(x) % 2])
#
#     return sum_
#
#
# print(func(9874023))






# lst = [1, 2, 3]
# tpl = 1, 2, 3
# print(lst, lst.__sizeof__())  # __sizeof__() - размер в памяти
# print(tpl, tpl.__sizeof__())






# tuple_ = tuple(2 ** i for i in range(1, 13));
# print(tuple_)





# from random import randint
#
#
# def slicer(tpl, n):
#
#     if tpl.count(n) > 1:
#         return tpl[tpl.index(n):tpl.index(n, tpl.index(n) + 1) + 1]
#
#     elif tpl.count(n) == 1:
#         return tpl[tpl.index(n):]
#
#     else:
#         return ()
#
#
# tup = tuple(randint(1, 10) for _ in range(randint(3, 10)))
# num = randint(1, 10)
# print(tup, num)
# print(slicer(tup, num))





# from random import randint
#
#
# def tuple_func(start, end):
#     return tuple(randint(start, end) for _ in range(10))
#
#
# tuple_1 = tuple_func(0, 5)
# tuple_2 = tuple_func(-5, 0)
# tuple_3 = tuple_1 + tuple_2
# count_0 = tuple_3.count(0)
#
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print('Count 0:', count_0)







# def to_set(s):
#     return set(s), len(set(s))
#
#
# s_ = 'я обычная строка'
# lst = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
# print(to_set(s_))
# print(to_set(lst))








# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s_ = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s_ = s1.union(s2, s3, s4, s5, s6, s7)
# print(s_, len(s_), max(s_), min(s_))




# s1 = 'Hello'
# s2 = 'How are you'
# s = set(s1) & set(s2)
# print(' '.join(list(s)))






# s1 = input()
# s2 = input()
# s = set(s1) - set(s2)
# print(' '.join(list(s)))






#
# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# multy = 1
#
# for key in d:
#     multy *= d[key]
#
# print(multy)






# d = {i + 1: input('-> ') for i in range(4)}
# print(d)
# del_ = int(input('How element del?\n'))
# del d[del_]
# print(d)







# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
#
# for key in goods:
#     print(f'{key}) {goods[key][0]} - {goods[key][1]} шт. по {goods[key][2]}руб')
#
# key = input('№: ')
#
# while key != '0':
#     count = int(input('Количество: '))
#     goods[key][1] = count
#     key = input('№: ')
#
# for key in goods:
#     print(f'{key}) {goods[key][0]} - {goods[key][1]} шт. по {goods[key][2]}руб')









# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)






# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
# print(d)
# print(new_d)




# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)







# d = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
#
# for key in d:
#     print(key)
#     for k, v in d[key].items():
#         print(f'\t{k}: {v}')






# d = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
# name = input('Name: ')
# region = input('Region: ')
# print(d[name][region])
# new = int(input('New: '))
# d[name][region] = new
# print(d[name])










# s = 'Hello'
# d = {key + 1: s[key] for key in range(len(s))}
# print(d)







# list_ = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = {}
# key = None
#
# for x in list_:
#     if isinstance(x, str):
#         d[x] = []
#         key = x
#     else:
#         d[key].append(x)
#
# print(d)
#
# list_ = [['one', [1, 2, 3]], ['two', [10, 20]], ['three', [15, 36, 60]], ['four', [-20]]]
# d = dict(list_)
# print(d)




# d = tuple(zip([1, 2, 3], [4, 5, 6]))
# print(d)






# def to_dict(*lst):
#     return {i: i for i in lst}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))






# def is_mean(*args):
#     mean = sum(args) / len(args)
#     print(mean)
#     return [x for x in args if x < mean]
#
# print(is_mean(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(is_mean(3, 6, 1, 9, 5))






# def outer(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# Moscow = outer('Moscow')
# Moscow()
# Moscow()








# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())







# print((lambda x, y: x ** 2 + y ** 2)(2, 5))


# def func(n):
#     return lambda x: x + n


# func = lambda n: lambda x: lambda y: n + x + y
# print(func(2)(4)(6))





# list = [{'name': 'Anton', 'last name': 'Birukov', 'raiting': 9}, {'name': 'Aleksey', 'last name': 'Bodny', 'raiting': 10}, {'name': 'Feodor', 'last name': 'Sidorov', 'raiting': 4}, {'name': 'Mikhail', 'last name': 'Semenov', 'raiting': 6}]
#
# print(sorted(list, key=lambda x: x['last name']))
# print(sorted(list, key=lambda x: x['raiting']))
# print(sorted(list, key=lambda x: x['raiting'], reverse=True))




# print((lambda a, b, c: min((a, b, c)))(10, -1, 2))



# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))



# import random
#
#
# lst = [random.randint(1, 30) for _ in range(10)]
# lst_new = list(filter(lambda x: 9 < x < 21, lst))
# print(lst)
# print('[10; 20] =', lst_new)






####################
#    ДЕКОРАТОРЫ    #
####################


# def decorator(func):
#     def wrapper():
#         print('Before')
#         func()
#         print('After')
#
#     return wrapper
#
#
# # def test():
# #     print('TEST')
# #
# #
# # var = decorator(test)
# # var()
#
#
# @decorator
# def test():
#     print('TEST')
#
#
# test()








# def bold(func):
#     def wrapper():
#         return '<b>' + func() + '</b>'
#     return wrapper
#
#
# def italic(func):
#     def wrapper():
#         return '<i>' + func() + '</i>'
#     return wrapper
#
#
# @bold
# @italic
# def text():
#     return 'TEXT'
#
#
# print(text())






# def decorator(func):
#     i = 0
#
#     def wrapper():
#         nonlocal i
#         i += 1
#         func()
#         print('Вызов функции:', i)
#
#     return wrapper
#
#
# @decorator
# def func_hello():
#     print('Hello')
#
#
# func_hello()
# func_hello()






# def decorator(func):
#     def wrapper(first, last):
#         func(first, last)
#
#     return wrapper
#
#
# @decorator
# def func_name(first, last):
#     print('Name:', first, last)
#
#
# func_name('Anna', 'NN')






# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# @decorator
# def func_name(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study)
#
#
# func_name('Anna', 'Irina', 'Ivan', study='JS')
# func_name('Anna', 'Irina', 'Ivan')





# def decorator(text):
#     def add_func(func):
#         def wrapper(x, y):
#             print(text, x, 'и', y, '=', func(x, y))
#         return wrapper
#     return add_func
#
#
# @decorator('Сумма')
# def summa(x, y):
#     return x + y
#
#
# @decorator('Разность')
# def sub(x, y):
#     return x - y
#
#
# summa(12, 9)
# sub(12, 9)





# def multiply(n):
#     def decorator(func):
#         def wrapper(a):
#             return func(a) * n
#         return wrapper
#     return decorator
#
#
# @multiply(3)
# def mul_func(a):
#     return a
#
#
# print('Result:', mul_func(5))






# def typed(*args, **kwargs):
#     def decorator(func):
#         def wrapper(*f_args, **f_kwargs):
#             if f_kwargs and all(isinstance(f_kwargs[i], kwargs[i]) for i in kwargs) and all(isinstance(f_args[i], args[i]) for i in range(len(args))) or not f_kwargs and all(isinstance(f_args[i], args[i]) for i in range(len(args))):
#                 return func(*f_args, **f_kwargs)
#             raise 'Некорректный тип данных'
#         return wrapper
#     return decorator
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z=2):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 'Dog'))
# print(typed_fn2('a', 'bb', 'Dog'))
# print(typed_fn2('a', 0.9, 'Dog'))
# print(typed_fn3('a', 'bb', z='3'))
# print(typed_fn3('a', 'Dog'))






# def args_decorator(tx=None, text=''):
#     def decorator(func):
#         def wrapper(*args):
#             print(text, func(*args), end='')
#         return wrapper
#
#     if not tx:
#         print('2:', tx)
#         return decorator
#     else:
#         print('1:', tx)
#         return decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     return text
#
#
# @args_decorator(text=', ')
# def hello_world2(text):
#     return text
#
#
# hello_world('Hello')
# hello_world2('world!')





##########################
#    СИСТЕМЫ СЧИСЛЕНИЯ   #
##########################


# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 10))
# print(int('100', 16))
#
# print(bin(18))
# print(oct(18))
# print(hex(18))
#
# print(0b10010)
# print(0o22)
# print(0x10)






# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
# str2 = ''
#
# for i in range(len(str1)):
#     if str1[i] == 'N':
#         str2 += 'P'
#         continue
#     str2 += str1[i]
#
# print(str2)






#########################
#    ПРЕФИКСЫ СТРОК     #
#########################


# x = 10
# y = 5.1234
# print(f'{x = }, {y = :.2f}, {{{x}}}, {{{{{y}}}}}')





#################################
#    НАПИСАНИЕ ДОКУМЕНТАЦИИ     #
#################################


# def func(R, h):
#     '''
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param R: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     '''
#     pass
#
#
# print(func.__doc__)





# str = 'Test string for me'
# list_ASCII = [ord(x) for x in str]
# print(f'ASCII коды: {list_ASCII}')
# mean = round(sum(list_ASCII) / len(list_ASCII))
# list_ASCII.insert(0, mean)
# print(f'Среднее арифметическое: {list_ASCII}')
# input_word = input('-> ').split()[:3]
# input_ASCII = [list_ASCII.append(ord(x)) for x in input_word if ord(x) not in list_ASCII]
# print(f'ASCII коды: {list_ASCII}')
# print(f'Количество последних элементов: {list_ASCII.count(list_ASCII[-1]) - 1}')
# print(f'Отсортированный список: {sorted(list_ASCII, reverse=True)}')







# a = 97
# b = 122
# list_ = [chr(x) for x in range(min(a, b), max(a, b) + 1)]
# print(*list_)









#######################
#   Random password   #
#######################


# from random import randint
#
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def random_password() -> str:
#     random_length = randint(SHORTEST, LONGEST)
#     password = ''.join(chr(randint(MIN_ASCII, MAX_ASCII)) for _ in range(random_length))
#     return password
#
#
# print('Your random password:', random_password())


##############################################






# print('heLLo, wORld!'.swapcase())   # - меняет регистр на противоположный
#
# print('heLLo, wORld!'.find('OR'))   # - возвращает первый индекс, который соответствует заданной подстроке. Если совпадений нет -> -1
#
# print('heLLo, wORld!'.rfind('L'))   # - ищет справа налево
#
# print('heLLo, wORld!'.index('OR'))   # - возвращает первый индекс, который соответствует заданной подстроке. Если совпадений нет -> Ошибка!
#
# print('heLLo, wORld!'.rindex('L'))   # - ищет справа налево
#
# print('abc123'.isalnum())  # - строка состоит из букв и цифр
# print('abc'.isalpha())  # - строка состоит только из букв
# print('abc'.center(10, '='))









#######################
#      Swap words     #
#######################


# s = 'One Two'
# space = s.index(' ')
# s_new = s[space + 1:] + ' ' + s[:space]
# print(s_new)


##############################################







#######################
#     Find numbers    #
#######################


# s = 'ab12c59p7dq'
# digits = [int(x) for x in s if x.isdigit()]
# print(digits)


##############################################







#######################
#     Find letter     #
#######################


# s = 'Nearly all web services collect this basic information from users in their server logs. However, Python Tutor does not collect any personally identifiable information from its users.'
#
# LETTER = 'K'
# result = s.index(LETTER) if s.count(LETTER) == 1 else '' if not s.count(LETTER) else str(s.find(LETTER)) + ' ' + str(s.rfind(LETTER))
# print(result)


##############################################








#######################
#    Delete letter    #
#######################


# s = 'Nearly all web services collect this basic information from users in their server logs. However, Python Tutor does not collect any personally identifiable information from its users.'
#
# LETTER = 'h'
# h_1 = s.find(LETTER)
# h_2 = s.rfind(LETTER)
# s_new = s[:h_1] + s[h_2 + 1:]
# print(s_new)


##############################################









##############################
#     Replace the symbol     #
##############################


# s = 'В строке заменить пробелы символом "*"'
# s = '*'.join(s.split())
# print(s)


##############################################






###############
#     FIO     #
###############


# s = input('FIO: ').split()
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')


##############################################










################################
#     Регулярные выражения     #
################################


# import re
#
#
# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = r'и'
#
# print(re.findall(reg, s))  # - возвращает список, содержащий все совпадения с заданным шаблоном
#
# print(re.search(reg, s))  # - возвращает данные первого совпадения с шаблоном
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
#
# print(re.match(reg, s))  # - возвращает данные совпадения с шаблоном в начале строки
#
# print(re.split(reg, s, 1))  # - разбивает строку по шаблону
#
# print(re.sub(reg, '*', s))  # - заменяет шаблон на заданный символ


##############################################








#######################################
#     Найти время в формате 16:25     #
#######################################


# import re
#
#
# text = 'Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09.'
# reg = re.findall(r'[0-2][0-9]:[0-5][0-9]', text)
# print(reg)


##############################################








############################
#     Применить шаблон     #
############################


# import re
#
#
# text = '05-03-1987 # Дата рождения'
# reg = re.sub(r'-', '.', re.sub('#.*', ' ', text))
# print(reg)


##############################################








############################
#     Применить шаблон     #
############################


# import re
#
#
# text = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# reg = re.findall(r'\w+\s*=[^;]+', text)
# print(reg)


##############################################








################################
#     Найти номер телефона     #
################################


# import re
#
#
# text = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg = re.findall(r'\+?7\d{10}', text)
# print(reg)


##############################################









#######################
#     Найти email     #
#######################


# import re
#
#
# text = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# reg = re.findall(r'[\w.-]+@[\w.-]+\.[a-z]{2,3}', text)
# print(reg)


##############################################











#######################
#      Найти IP       #
#######################


# import re
#
#
# s1 = '192.168.255.255'
# reg = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', s1)
# print(reg)


##############################################











##################################
#       Работа с выражением      #
##################################


# import re
#
#
# text = '5 + 7*2 -4'
# reg = re.split(r'\s*([+*-])\s*', text)
# print(reg)


##############################################










#################
#      img      #
#################


# import re
#
#
# text = '<p>Изображения <img src="bg.jpg"> - фон страницы</p>'
# reg = re.findall(r'<img\s+>*src=(?P<q>["\'])(.+)(?P=q)', text)
# print(reg)


##############################################










###########################################
#      Date mm/dd/YYYY -> dd.mm.YYYY      #
###########################################


# import re
#
#
# text = 'Самолет прилетает 10/23/2023. Будем вас рады видеть после 10/24/2023'
# reg = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2.\1.\3', text)
# print(reg)


##############################################










##################
#      Link      #
##################


# import re
#
#
# text = 'yandex.com and yandex.ru'
# reg = re.sub(r'(([a-zA-Z\d-]{2,}\.)+[a-z]{2,4})', r'https://\1', text)
# print(reg)


##############################################










#############################
#     Recursion - floor     #
#############################


# def elevator(floor):
#     if floor == 0:
#         print('You in basement!')
#         return
#     print('->', floor)
#     elevator(floor - 1)
#
#
# floor_user = int(input('Your floor: '))
# elevator(floor_user)


##############################################








#############################
#     Recursion - summa     #
#############################


# def summa_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] + summa_list(lst[1:])
#
#
# list_num = [1, 3, 5, 7, 9]
# print(summa_list(list_num))


##############################################








#########################################
#     Recursion - the number system     #
#########################################


# def number_system(num, base):
#     convert = '0123456789'
#     if num < base:
#         return convert[num]
#     return number_system(num // base, base) + convert[num % base]
#
#
# print(number_system(769, 8))


##############################################








#############################
#     Recursion - lists     #
#############################


# def count_items(l: list) -> int:
#     count = 0
#     for item in l:
#         if isinstance(item, str):
#             count += 1
#         elif isinstance(item, list):
#             count += count_items(item)
#     return count
#
#
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(count_items(names))


##############################################










#############################
#     Recursion - lists     #
#############################


# def union(l: list) -> int:
#     if not l:
#         return l
#     if isinstance(l[0], list):
#         return union(l[0]) + union(l[1:])
#     return l[:1] + union(l[1:])
#
#
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(union(names))


##############################################







###################
#    LoopSort     #
###################


# from random import randint
# import time
#
# def loop_sort(l: list) -> list:
#     for i in range(len(l) - 1):
#         for j in range(len(l) - i - 1):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#     return l
#
#
# list_ = [randint(-100, 100) for _ in range(1000)]
# time1 = time.monotonic()
# print(time1)
# print('Отсортированный список:\n', loop_sort(list_))
# time2 = time.monotonic()
# delta_time = time2 - time1
# print('Время сортировки:', round(delta_time, 4))


#############################################







#######################
#    Merge Sorting    #
#######################


# from random import randint
# import time
#
# def merge_sort(l: list) -> list:
#     n = len(l)
#     if n == 1:
#         return l
#     left = merge_sort(l[:n // 2])
#     right = merge_sort(l[n // 2:n])
#     i = j = 0
#     new = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             new.append(right[j])
#             j += 1
#         elif not j < len(right):
#             new.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             new.append(left[i])
#             i += 1
#         else:
#             new.append(right[j])
#             j += 1
#
#     return new
#
#
# list_ = [randint(-100, 100) for _ in range(1000)]
# time1 = time.monotonic()
# print('Отсортированный список:\n', merge_sort(list_))
# time2 = time.monotonic()
# delta_time = time2 - time1
# print('Время сортировки:', round(delta_time, 4))


#############################################









#######################
#    Shell Sorting    #
#######################


# from random import randint
# import time
#
# def shell_sort(l: list) -> list:
#     gap = len(l)
#
#     while gap:
#         for val in range(gap, len(l)):
#             cur_val = l[val]
#             pos = val
#
#             while pos >= gap and l[pos - gap] > cur_val:
#                 l[pos] = l[pos - gap]
#                 pos -= gap
#                 l[pos] = cur_val
#
#         gap //= 2
#
#     return l
#
#
# list_ = [randint(-100, 100) for _ in range(1000)]
# time1 = time.monotonic()
# print('Отсортированный список:\n', shell_sort(list_))
# time2 = time.monotonic()
# delta_time = time2 - time1
# print('Время сортировки:', round(delta_time, 4))


#############################################










######################
#    Quick Sorting   #
######################


# from random import randint
# import time
#
# def quick_sort(l: list) -> list:
#     if len(l) > 1:
#         x = l[(len(l) - 1) // 2]
#         low = [i for i in l if i < x]
#         eq = [i for i in l if i == x]
#         hi = [i for i in l if i > x]
#         l = quick_sort(low) + eq + quick_sort(hi)
#     return l
#
#
# list_ = [randint(-100, 100) for _ in range(1000)]
# time1 = time.monotonic()
# print('Отсортированный список:\n', quick_sort(list_))
# time2 = time.monotonic()
# delta_time = time2 - time1
# print('Время сортировки:', round(delta_time, 4))


#############################################











##############
#    Files   #
##############


# fail = open('text.txt')
# count_lines = len(fail.readlines())
# print(count_lines)


#############################################









##############
#    Files   #
##############


# def get_string(l: list) -> str:
#     return '\t'.join(map(str, l))
#
#
# numbers = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
# fail_name = 'text.txt'
#
# with open(fail_name, 'r+', encoding='utf-8') as file:
#     text = get_string(numbers)
#     file.write(text)
#
#     nums = list(map(float, file.read().split()))
#     print(nums, sum(nums), len(nums))



#############################################







####################
#    Modules OS    #
####################


# import os


# print(os.getcwd())      # return path dir (absolute path)
# print(os.listdir())      # return list dirs and files
# print(os.listdir('../'))
#
# os.mkdir('folder')      # create dir
# os.makedirs('folder/folder/new')
#
# os.remove('text.txt')      # remove fail
# os.rename('folder', 'new')      # rename dir
#
# os.rmdir('folder')      # remove empty dir
#
# for root, dirs, files in os.walk('venv'):      # watch dirs and files in root
#     print(root, dirs, files)




#############################################








#########################
#    Modules OS.PATH    #
#########################


# from os import path
#
#
# print(path.split(r'C:\Users\Admin\Desktop'))      # tuple (head, tail)
# print(path.dirname(r'C:\Users\Admin\Desktop'))      # name dir
# print(path.basename(r'C:\Users\Admin\Desktop'))      # name file


#############################################







#########################
#    Modules OS.PATH    #
#########################


# import os
#
#
# dirs = [r'Work\F1', r'Work\F2\F21']
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
# files_with_text = []
#
# for d in dirs:
#     os.makedirs(d)
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         files_with_text.append(file_path)
#         open(file_path, 'w').close()
#
# for file_name in files_with_text:
#     with open(file_name, 'w') as file:
#         file.write(file_name)



#############################################











#########################
#    Modules OS.PATH    #
#########################


# import os
#
#
# path = r'C:/Users/Admin/Desktop'
# docs = os.listdir(path)
#
# for doc in docs:
#     doc = os.path.join(path, doc)
#     if os.path.isfile(doc):
#         name, size = os.path.basename(doc), os.path.getsize(doc)
#         print(f'{name} - file - {size} bytes')
#     elif os.path.isdir(doc):
#         name = os.path.basename(doc)
#         print(f'{name} - dir')


#############################################






# class Car:
#     model = None
#     year = None
#     name = None
#     power = None
#     color = None
#     price = None
#
#     def input_data(self, model, year, name, power, color, price):
#         self.model = model
#         self.year = year
#         self.name = name
#         self.power = power
#         self.color = color
#         self.price = price
#
#     def output_data(self):
#         print('Название модели:', self.model)
#         print('Год выпуска:', self.year)
#         print('Производитель:', self.name)
#         print('Мощность двигателя:', self.power, 'л. с.')
#         print('Цвет машины:', self.color)
#         print('Цена:', self.price)
#
#     def get_model(self):
#         return self.model
#
#     def set_model(self, value):
#         self.model = value
#
#
# BMW = Car()
# BMW.input_data('X7 M50i', 2021, 'BMW', 530, 'white', 10790000)
# BMW.output_data()
# BMW.set_model('Y7')
# print(BMW.get_model())










###############
#    Robot    #
###############


# class Robot:
#     COUNT = 0
#
#     def __init__(self, name):
#         self.name = name
#         Robot.COUNT += 1
#         print(f'Инициализация робота: {self.name}')
#
#     def __del__(self):
#         Robot.COUNT -= 1
#         print(f'Выключение робота: {self.name}')
#         if not Robot.COUNT:
#             print(f'Робот {self.name} был последним')
#             print(f'Численность роботов: {self.COUNT}')
#         else:
#             print(f'Работающих роботов: {self.COUNT}')
#
#     def say_hello(self):
#         print(f'Приветствую! Меня зовут: {self.name}')
#
#     def get_count_robots(self):
#         return self.COUNT
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hello()
# print(f'Численность роботов: {droid1.get_count_robots()}')
#
# droid2 = Robot('C-3PO')
# droid2.say_hello()
# print(f'Численность роботов: {droid2.get_count_robots()}')


#############################################








######################
#    Kg -> Pounds    #
######################


# class KgToPounds:
#     def __init__(self, kg):
#         self.__check_value(kg)
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, value):
#         self.__check_value(value)
#         self.__kg = value
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     @staticmethod
#     def __check_value(value):
#         if isinstance(value, (int, float)):
#             return True
#         raise 'Некорректное значение кг!'
#
#
# weight = KgToPounds(12)
# print(f'{weight.kg} кг -> {weight.to_pounds()} фунтов')


#############################################










################
#    Person    #
################


# class Person:
#     def __init__(self, name, age):
#         if isinstance(name, str) and isinstance(age, int):
#             self.__name = name
#             self.__age = age
#         else:
#             print('Некорректные данные!')
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if isinstance(value, str):
#             self.__name = value
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if isinstance(value, int):
#             self.__age = value
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# person = Person('Irina', 26)
# print(person.__dict__)


#############################################









################
#    Person    #
################


# from math import factorial
#
#
# class MathMethods:
#     @staticmethod
#     def get_maximum(*args):
#         return max(args)
#
#     @staticmethod
#     def get_minimum(*args):
#         return min(args)
#
#     @staticmethod
#     def get_avg(*args):
#         if args:
#             return sum(args) / len(args)
#         return 0
#
#     @staticmethod
#     def get_factorial():
#         return factorial(5)
#
#
# print('Максимальное число:', MathMethods.get_maximum(3, 5, 7, 9))
# print('Минимальное число:', MathMethods.get_minimum(3, 5, 7, 9))
# print('Среднее арифметическое:', MathMethods.get_avg(3, 5, 7, 9))
# print('Факториал числа 5:', MathMethods.get_factorial())


#############################################









##############
#    Area    #
##############


# class Area:
#     __COUNT = 0
#
#     @staticmethod
#     def get_count():
#         return Area.__COUNT
#
#     @staticmethod
#     def get_area_triangle_geron(a, b, c):
#         Area.__COUNT += 1
#         p = sum((a, b, c)) / 2
#         return (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
#     @staticmethod
#     def get_area_triangle(a, h):
#         Area.__COUNT += 1
#         return (a * h) / 2
#
#     @staticmethod
#     def get_area_square(a):
#         Area.__COUNT += 1
#         return a ** 2
#
#     @staticmethod
#     def get_area_rectangle(a, b):
#         Area.__COUNT += 1
#         return a * b
#
#
# print('Площадь треугольника по формуле Герона:', Area.get_area_triangle_geron(3, 4, 5))
# print('Площадь треугольника:', Area.get_area_triangle(6, 7))
# print('Площадь квадрата:', Area.get_area_square(7))
# print('Площадь прямоугольника:', Area.get_area_rectangle(2, 6))
# print('Количество подсчетов площади:', Area.get_count())


#############################################








#######################
#    class Account    #
#######################


# class Account:
#     RATE_RUB_TO_USD = 0.013
#     RATE_RUB_TO_EUR = 0.011
#     SUFFIX_RUB = 'RUB'
#     SUFFIX_USD = 'USD'
#     SUFFIX_EUR = 'EUR'
#
#     def __init__(self, surname, number, percent, balance=0):
#         self.surname = surname
#         self.number = number
#         self.percent = percent
#         self.balance = balance
#
#         print(f'Счет №{self.number}, принадлежащий {self.surname} был открыт.\n{"*" * 50}')
#
#     def __del__(self):
#         print(f'{"*" * 50}\nСчет №{self.number}, принадлежащий {self.surname} был закрыт.')
#
#     @classmethod
#     def set_usd(cls, value):
#         cls.RATE_RUB_TO_USD = value
#
#     @classmethod
#     def set_eur(cls, value):
#         cls.RATE_RUB_TO_EUR = value
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def get_usd(self):
#         value = Account.convert(self.balance, self.RATE_RUB_TO_USD)
#         return f'Состояние счёта: {value} {self.SUFFIX_USD}'
#
#     def get_eur(self):
#         value = Account.convert(self.balance, self.RATE_RUB_TO_EUR)
#         return f'Состояние счёта: {value} {self.SUFFIX_EUR}'
#
#     def set_surname(self, value):
#         self.surname = value
#
#     def add_percents(self):
#         self.balance += self.balance * self.percent
#         print(f'Проценты были успешно начислены!')
#         return self.get_balance()
#
#     def withdraw_money(self, value):
#         if value > self.balance:
#             print(f'Недостаточно средств на счете!')
#         else:
#             self.balance -= value
#             print(f'{value} {self.SUFFIX_RUB} успешно снято.')
#         return self.get_balance()
#
#     def add_money(self, value):
#         self.balance += value
#         print(f'Сумма {value} {self.SUFFIX_RUB} успешно добавлена.')
#         return self.get_balance()
#
#     def get_balance(self):
#         text = f'Текущий баланс: {self.balance} {self.SUFFIX_RUB}\n{"-" * 20}'
#         return text
#
#     def get_info(self):
#         text = f'Информация о счете:\n{"-" * 20}\n№{self.number}\nВладелец: {self.surname}\nТекущий баланс: {self.balance} {self.SUFFIX_RUB}\nПроценты: {self.percent:.0%}\n{"-" * 20}'
#         return text
#
#
# account = Account('Долгих', 12345, 0.03, 1000)
# print(account.get_info())
# print(account.get_usd())
# print(account.get_eur())
#
# Account.set_usd(2)
# print(account.get_usd())
# print(account.add_percents())
# print(account.withdraw_money(400))
# print(account.withdraw_money(4000))
# print(account.add_money(500))








#####################
#    class Table    #
#####################


# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if length is None and width:
#             self._width = self._length = width
#         elif radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def get_area(self):
#         raise NotImplementedError
#
#
# class RectangleTable(Table):
#     def __init__(self, width=None, length=None):
#         super(RectangleTable, self).__init__(width, length)
#
#     def get_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def __init__(self, radius=None):
#         super(RoundTable, self).__init__(radius=radius)
#
#     def get_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# table1 = RectangleTable(20, 10)
# table2 = RoundTable(40)
# table3 = RectangleTable(30)
# print(table1.__dict__)
# print(table2.__dict__)
# print(table3.__dict__)
# print(table1.get_area())
# print(table2.get_area())
# print(table3.get_area())









########################
#    class Currency    #
########################


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         raise NotImplementedError
#
#     @abstractmethod
#     def get_info(self):
#         raise NotImplementedError
#
#
# class Dollar(Currency):
#     RATE = 74.16
#     SUFFIX = 'USD'
#
#     def convert_to_rub(self):
#         return str(round(self.value * self.RATE, 3)) + ' RUB'
#
#     def get_info(self):
#         return str(self.value) + ' ' + self.SUFFIX
#
#
# class Euro(Currency):
#     RATE = 90.14
#     SUFFIX = 'EUR'
#
#     def convert_to_rub(self):
#         return str(round(self.value * self.RATE, 3)) + ' RUB'
#
#     def get_info(self):
#         return str(self.value) + ' ' + self.SUFFIX
#
#
# dollar = Dollar(20)
# print(dollar.get_info(), '=', dollar.convert_to_rub())
#
# euro = Euro(20)
# print(euro.get_info(), '=', euro.convert_to_rub())





#####################
#    class Clock    #
#####################


# class Clock:
#     def __init__(self, s: int):
#         self.sec = s
#
#     def __lt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть Clock')
#         return self.sec < other.sec
#
#     def __le__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть Clock')
#         return self.sec <= other.sec
#
#     def __gt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть Clock')
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть Clock')
#         return self.sec >= other.sec
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# print(c1 > c2)
# print(c2 >= c1)
# print(c1 < c2)
# print(c2 <= c1)








#################################
#    class Cat and class Dog    #
#################################


# class Dog:
#     def __init__(self, name: str, age: (int, float)):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}'
#
#     def make_sound(self):
#         return f'{self.name} гавкает.'
#
#
# class Cat:
#     def __init__(self, name: str, age: (int, float)):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}'
#
#     def make_sound(self):
#         return f'{self.name} мяукает.'
#
#
# cat = Cat('Пушок', 2.5)
# dog = Dog('Мухтар', 4)
#
# for animal in [cat, dog]:
#     print(animal.info())
#     print(animal.make_sound())







###############################################################
#  class Human, class Student, class Teacher, class Graduate  #
###############################################################


# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def info(self):
#         return f'{self.name}, {self.surname}, {self.age}'
#
#
# class Student(Human):
#     def __init__(self, name, surname, age, speciality, group, rating):
#         super(Student, self).__init__(name, surname, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         return super(Student, self).info() + f', {self.speciality}, {self.group}, {self.rating}'
#
#
# class Teacher(Human):
#     def __init__(self, name, surname, age, speciality, experience):
#         super(Teacher, self).__init__(name, surname, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         return super(Teacher, self).info() + f', {self.speciality}, {self.experience}'
#
#
# class Graduate(Student):
#     def __init__(self, name, surname, age, speciality, group, rating, topic):
#         super(Graduate, self).__init__(name, surname, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         return super(Graduate, self).info() + f', {self.topic}'
#
#
# group = [Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#          Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#          Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#          Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#          Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#          Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     print(i.info())







#################
#  class Power  #
#################


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def multy(a, b):
#     return a * b
#
#
# print(f'Результат: {multy(2, 3)}')







#################
#  Дескрипторы  #
#################


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# person = Person('Ivan', 'Petrov')
# print(person.name)







############################
#  Дескриптор class Order  #
############################


# class NoNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int) or value <= 0:
#             raise ValueError('Значение должно быть положительным')
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NoNegative()
#     quantity = NoNegative()
#
#     def __init__(self, name, price, quantity):
#         self.order = name
#         self.price = price
#         self.quantity = quantity
#
#     def get_total(self):
#         return self.price * self.quantity
#
#
# order = Order('apple', 5, 10)
# print(order.get_total())








##############################
#  Дескриптор class Point3D  #
##############################


# class Integer:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise TypeError(f'Координата {self.name} должна быть целым числом')
#         instance.__dict__[self.name] = value
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# point = Point3D(1, 2, 3)
# print(point.__dict__)









############
#  pickle  #
############


# import pickle
#
#
# class Test:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x ** 2
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x ** 2
#
#
# item1 = Test()
# print(item1.__dict__)
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)







##########
#  json  #
##########


# import json
#
#
# data = {
#     'name': 'Olga',
#     'age': 27,
#     1: None,
#     True: 12,
#     'hobbies': ('running', 'swimming'),
#     'children': [
#         {
#             1: 'Иван',
#             2: 'Андрей'
#         }
#     ]
# }
#
# json_dumps = json.dumps(data, indent=4, ensure_ascii=False)
# print(json_dumps)
# json_loads = json.loads(json_dumps)
# print(json_loads)






###############################
#  class Student class Group  #
###############################


# import json
#
#
# class Student:
#     def __init__(self, name: str, marks: list):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         return f'{self.name}: {", ".join(map(str, self.marks))}'
#
#     def add_mark(self, mark: int):
#         self.marks.append(mark)
#
#     def del_mark(self, index: int):
#         self.marks.pop(index)
#
#     def change_mark(self, index: int, value: int):
#         self.marks[index] = value
#
#     def get_avg(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @staticmethod
#     def dump_to_json(student, filename: str):
#         try:
#             students = json.load(open(filename))
#
#         except FileNotFoundError:
#             students = []
#
#         student = {
#             'name': student.name,
#             'marks': student.marks
#         }
#         students.append(student)
#
#         with open(filename, 'w') as file:
#             json.dump(students, file, indent=2)
#
#     @staticmethod
#     def load_json(filename: str):
#         with open(filename) as file:
#             print(json.load(file))
#
#
# class Group:
#     def __init__(self, name: str, students: list):
#         self.name = name
#         self.students = students
#
#     def __str__(self):
#         result = 'Группа: ' + self.name + '\n'
#
#         for student in self.students:
#             result += 'Студент ' + str(student) + '\n'
#
#         return result
#
#     def add_student(self, student: Student):
#         self.students.append(student)
#
#     def del_student(self, index: int):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index: int):
#         return group2.add_student(group1.del_student(index))
#
#     def dump_group(self, filename):
#         try:
#             students = json.load(open(filename))
#
#         except FileNotFoundError:
#             students = []
#
#         for student in self.students:
#             students.append([student.name, student.marks])
#
#         with open(filename, 'w') as file:
#             json.dump(students, file, indent=2)
#
#     @staticmethod
#     def load_group(group, filename):
#         with open(filename) as file:
#             print(json.load(file))
#
#
# students1 = [Student('Bobnya', [5, 4, 3, 4, 5, 3]), Student('Nikolaenko', [2, 3, 5, 4, 2])]
# group1 = Group('ГК Python', students1)
# print(group1)
#
# Student.dump_to_json(students1[1], 'student.txt')
# Student.load_json('student.txt')
#
# students2 = [Student('Birukov', [3, 5, 3, 2, 5, 4])]
# group2 = Group('ГК Web', students2)
# print(group2)
#
# group1.dump_group('group.json')
# Group.load_group(group1, 'group.json')







##############
#  requests  #
##############


# import requests
# import json
#
#
# url = 'https://jsonplaceholder.typicode.com/todos'
# response = requests.get(url)
# data = json.loads(response.text)
#
# todos = {}
#
# for todo in data:
#     if todo['completed'] and not todo['userId'] in todos:
#         todos[todo['userId']] = 1
#     elif todo['completed'] and todo['userId'] in todos:
#         todos[todo['userId']] += 1
#
# max_todo = max(list(todos.values()))
# max_todos = dict(filter(lambda x: x[1] == max_todo, list(todos.items())))







#########
#  csv  #
#########


# import csv
#
#
# with open('data.csv') as file:
#     file = csv.reader(file, delimiter=';')
#
#     for row in file:
#         print(row)
#
#
# with open('data.csv') as file:
#     file = csv.DictReader(file, delimiter=';')
#
#     for row in file:
#         print(row)



# with open('data.csv', 'w') as file:
#     write = csv.writer(file, delimiter=';', lineterminator='\r')
#     write.writerow(['Name', 'Age'])
#     write.writerow(['name1', 'age1'])
#     write.writerow(['name2', 'age2'])





# with open('data.csv', 'w') as file:
#     write = csv.DictWriter(file, delimiter=';', lineterminator='\r', fieldnames=['Name', 'Age'])
#     write.writerow({'Name': 'name1', 'Age': 23})
#     write.writerow({'Name': 'name2', 'Age': 33})








#############
#  Парсинг  #
#############


# from bs4 import BeautifulSoup
#
#
# with open('index.html') as file:
#     data = file.read()
#
# soup = BeautifulSoup(data, 'html.parser')
# # row = soup.find_all('div', class_='row')[0]
# # row = soup.find('div', class_='row').find('div', class_='links')
# row = soup.find('div', id='whois3').find_next_sibling()
# print(row)






############
#  socket  #
############


import socket


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen()

    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024)

        print(f'Клиент: {address} => \n{request}\n')


if __name__ == '__main__':
    run()



























# n, m = [int(x) for x in input().split()]
# matrix = [[0] * m for i in range(n)]
# var = 0
#
# directions = ['left', 'down', 'right', 'up']
# i, j = 0, 0
# current_direction = directions[0]
#
# while var < n * m - 1:
#
#     while current_direction == directions[0] and var < n * m - 1:
#
#         if j < m - 1 and matrix[i][j+1] == 0:
#             var += 1
#             matrix[i][j] = var
#             j += 1
#
#         else:
#             current_direction = directions[1]
#
#     while current_direction == directions[1] and var < n * m - 1:
#
#         if i < n - 1 and matrix[i+1][j] == 0:
#             var += 1
#             matrix[i][j] = var
#             i += 1
#
#         else:
#             current_direction = directions[2]
#
#
#     while current_direction == directions[2] and var < n * m - 1:
#
#         if j > 0 and matrix[i][j-1] == 0:
#             var += 1
#             matrix[i][j] = var
#             j -= 1
#
#         else:
#             current_direction = directions[3]
#
#     while current_direction == directions[3] and var < n * m - 1:
#
#         if i > 0 and matrix[i-1][j] == 0:
#             var += 1
#             matrix[i][j] = var
#             i -= 1
#
#         else:
#             current_direction = directions[0]
#
#     if var == n * m - 1:
#         matrix[i][j] = var + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()









# def jarriquez_encryption(text, alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
#     #your code
#     for i in range(1000, 1000000):
#         text_new = ''
#         key = str(i)
#         text_key = key*(len(text)//len(key)) + key[:len(text)%len(key)]
#         for j in range(len(text)):
#             text_new += alphabet[(alphabet.index(text[j])-int(text_key[j]))%len(alphabet)]
#         if 'ДАКОСТ' in text_new or 'АЛМАЗ' in text_new:
#             print(text_new)
#             print(key + '\n')
#
# jarriquez_encryption('ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖОИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС')
