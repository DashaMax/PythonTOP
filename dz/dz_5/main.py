import random


''' Задание с занятия - вывести матрицу в отформатированном виде '''

# matrix = [[i * j for i in range(1, 11)] for j in range(1, 11)]
# [[print(matrix[row][col], end='\n' if col == 9 else '\t') for col in range(len(matrix[row]))] for row in range(len(matrix))]






''' Написать программу, которая проверяет, находится ли введенное с клавиатуру число в списке. Список должен вводиться во время работы программы '''


list_ = [input('-> ') for _ in range(int(input('Введите элементы списка:\nn = ')))]
num = input('Введите число:\nch = ')
result = 'Число присутствует в элементах списка' if num in list_ else 'Число в элементах списка не найдено'
print(result)






''' Заполнить список из 20 элементов случайными числами. Найти сумму элементов этого списка. '''


# list_ = [random.randint(0, 100) for _ in range(20)]
# print(list_)
# sum_ = sum(list_)
# print('Summa:', sum_)







''' Заполнить список из 10 элементов случайными числами. Переместить все положительные элементы, начиная с максимального, в начало списка. '''


# list_ = [random.randint(-100, 100) for _ in range(10)]
# print(list_)
# list_.sort(reverse=True)
# print(list_)






''' Написать программу, которая случайным образом заполняет двумерный список размером 3х4 цифрами от 0 до 4. Найти произведение ненулевых элементов списка. '''


# matrix = [[random.randint(0, 4) for _ in range(3)] for _ in range(4)]
# [[print(matrix[i][j], end='\n' if j == 2 else '\t\t') for j in range(3)] for i in range(4)]
# multy = 1
#
# for row in matrix:
#     for num in row:
#         multy *= num if num else 1
#
# print('Произведение ненулевых элементов:', multy)







''' Напишите программу нахождения минимального элемента главной диагонали массива K(n, n), заполненного случайными числами. Из него требуется сформировать новый массив только из положительных элементов. Найти из них наибольший элемент. Распечатать новый массив и наибольший элемент. '''


# n = int(input('Размерность массива: '))
# matrix = [[random.randint(-100, 100) for _ in range(n)] for _ in range(n)]
# print('Массив из случайных чисел от -100 до 100:')
# [[print(matrix[i][j], end='\n' if j == n - 1 else '\t\t') for j in range(n)] for i in range(n)]
#
#
# ''' Нахождение минимального элемента главной диагонали. '''
#
# main_diag = [matrix[i][i] for i in range(n)]
# min_ = min(main_diag)
# print('Минимальный элемент главной диагонали:', min_)
#
#
#
# ''' Формирование нового массива только из положительных элементов и нахождение наибольшего. '''
#
# matrix_is_positive = [num for row in matrix for num in row if num > 0]
# print('\nМассив из положительных элементов:')
# print(matrix_is_positive)
# max_ = max(matrix_is_positive)
# print('Наибольший элемент:', max_)







''' Написать программу, которая случайным образом заполняет двумерный список размерностью 3х4 числами от -20 до 10. Необходимо найти количество отрицательных элементов. '''


# matrix = [[random.randint(-20, 10) for _ in range(3)] for _ in range(4)]
# [[print(matrix[i][j], end='\n' if j == 2 else '\t\t') for j in range(3)] for i in range(4)]
# is_negative = 0
#
# for row in matrix:
#     for num in row:
#         is_negative += 1 if num < 0 else 0
#
# print('Количество отрицательных элементов:', is_negative)







''' Написать программу, которая случайным образом заполняет двумерный список размером 6х6 числами от 0 до 10 и одномерный список из 6-ти чисел. Нужно нечетные строки двумерного списка заменить на одномерный список. '''


# matrix = [[random.randint(0, 10) for _ in range(6)] for _ in range(6)]
# [[print(matrix[i][j], end='\n' if j == 5 else '\t\t') for j in range(6)] for i in range(6)]
#
# list_ = [random.randint(0, 10) for _ in range(6)]
# print(list_, end='\n\n')
#
# for row in range(0,6,2):
#     matrix[row] = list_
#
# [[print(matrix[i][j], end='\n' if j == 5 else '\t\t') for j in range(6)] for i in range(6)]







''' Написать программу, которая случайым образом заполняет двумерный список 6х6 числами от 0 до 10. Поменять местами 1-ю и 2-ю строки, 3-ю и 4-ю строки, 5-ю и 6-ю строки двумерного списка. '''


# matrix = [[random.randint(0, 10) for _ in range(6)] for _ in range(6)]
# [[print(matrix[i][j], end='\n' if j == 5 else '\t\t') for j in range(6)] for i in range(6)]
#
# matrix[0], matrix[1] = matrix[1], matrix[0]
# matrix[2], matrix[3] = matrix[3], matrix[2]
# matrix[4], matrix[5] = matrix[5], matrix[4]
#
# print()
# [[print(matrix[i][j], end='\n' if j == 5 else '\t\t') for j in range(6)] for i in range(6)]



