''' Написать функцию, которая принимает один аргумент, который в дальнейшем будет умножаться на заданное число. '''


def func_compute(arg):
    def func_mult(num):
        return arg * num

    return func_mult


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))





''' Создать лямбда-выражение, которое возвращает произведение трех чисел. '''


# func = lambda a, b, c: a * b * c
# print(func(2, 5, 5))





''' Отсортировать список объектов по имени студентов и итоговым оценкам в порядке убывания. '''


# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# print(sorted(students, key=lambda x: x['name']))
# print(sorted(students, key=lambda x: x['final'], reverse=True))





''' Получить минимальную и максимальную итоговую оценку студентов. '''


# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# max_ = max(students, key=lambda x: x['final'])
# min_ = min(students, key=lambda x: x['final'])
# print(max_)
# print(min_)