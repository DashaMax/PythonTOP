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



print('TEST')






















































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
