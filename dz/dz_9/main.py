
''' Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами, а элементы второго - соответственно значениями нашего словаря.'''


# l1 = ['red', 'green', 'blue']
# l2 = ['#FF0000', '#008000', '#0000FF']
# d = dict(zip(l1, l2))
# print(d)





''' Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб. '''


# d = {key: key ** 3 for key in range(1, 11)}
# print(d)




''' Даны три словаря. Объединить данные словари в один. '''


# d1 = {1: 10, 2: 20}
# d2 = {3: 30, 4: 40}
# d3 = {5: 50, 6: 60}
# d = d1 | d2 | d3
# print(d)





''' Дан словарь. Измените значение зарплаты Брэда с 6500 до 8500. '''


# d = {'emp1': {
#         'name': 'Jhon',
#         'salary': 7500
#     },
#
#     'emp2': {
#         'name': 'Emma',
#         'salary': 8000
#     },
#
#     'emp3': {
#         'name': 'Brad',
#         'salary': 6500
#     }
# }
# d['emp3']['salary'] = 8500
#
# for key1 in d:
#     print(key1)
#     for key2, value in d[key1].items():
#         print(f'{key2}: {value}')





''' Пользователь вводит данные о количестве студентов, их фамилии, имена и балл для каждого. Программа должна определить средний балл и вывести фамилии и имена студентов, чей балл выше среднего. '''


# from math import ceil
#
#
# students = {}
#
# for student in range(int(input('Количество студентов: '))):
#     name = input(f'{student + 1}-й студент: ')
#     students[name] = int(input('Балл: '))
#
# mean = ceil(sum(list(students.values())) / len(list(students.values())))
# print(f'Средний балл: {mean}. Студенты с баллом выше среднего:')
#
# [print(name) for name, bal in students.items() if bal > mean]
#
# # for name, bal in students.items():
# #     if bal > mean:
# #         print(name)





''' Используя два списка данных, создайте новый словарь с использованием генератора словарей. '''


# l1 = ['color', 'fruit', 'pet']
# l2 = ['blue', 'apple', 'dog']
# d = {l1[i]: l2[i] for i in range(len(l1))}
# print(d)