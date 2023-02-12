''' Есть список из 10 элементов, заполненный случайными числами.
Необходимо найти число, введенное пользователем.
Используйте алгоритм линейного поиска. '''


from random import randint


def search_number(a: list, number: int) -> bool:
    for num in a:
        if num == number:
            return True
    return False


list_numbers = [randint(-100, 100) for _ in range(10)]
print(list_numbers)
user_number = int(input('Введите число: '))

if search_number(list_numbers, user_number):
    print(f'Число {user_number} в списке присутствует')
else:
    print(f'Число {user_number} в списке отсутствует')





''' Удаление строки из файла по её индексу. '''


# fail = open('text.txt', 'w+', encoding='utf-8')
# text = '''Замена строки в текстовом файле;
# изменить строку в списке;
# записать список в файл;'''
# fail.write(text)
#
# pos = int(input('Удалить строку №'))
# fail.seek(0)
# fail_lines = fail.readlines()
# fail.close()
#
# fail = open('text.txt', 'w', encoding='utf-8')
#
# if pos < len(fail_lines):
#     fail_lines.pop(pos)
#     fail.write(''.join(fail_lines))
# else:
#     fail.write(text)
#     raise IndexError('Строка не найдена')
#
# fail.close()





''' Есть четыре списка целых чисел. Необходимо их объединить в пятом списке. Полученный результат в зависимости от выбора пользователя отсортировать по убыванию или по возрастанию. Найти значение, введенное пользователем, с использованием линейного поиска. '''


# from random import randint
#
#
# # Bubble Sorting in descending order
# def bubble_sort_desc(l: list) -> list:
#     for i in range(len(l) - 1):
#         for j in range(len(l) - i - 1):
#             if l[j] < l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#     return l
#
#
# # Bubble Sorting in ascending order
# def bubble_sort_asc(l: list) -> list:
#     for i in range(len(l) - 1):
#         for j in range(len(l) - i - 1):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#     return l
#
#
# # Merge Sorting in descending order
# def merge_sort_desc(l: list) -> list:
#     if len(l) == 1:
#         return l
#
#     left = merge_sort_desc(l[:len(l) // 2])
#     right = merge_sort_desc(l[len(l) // 2:])
#
#     new_list = []
#
#     while len(left) and len(right):
#         if left[0] > right[0]:
#             new_list.append(left[0])
#             left.pop(0)
#
#         else:
#             new_list.append(right[0])
#             right.pop(0)
#
#     if len(left):
#         new_list += left
#
#     else:
#         new_list += right
#
#     return new_list
#
#
# # Merge Sorting in ascending order
# def merge_sort_asc(l: list) -> list:
#     if len(l) == 1:
#         return l
#
#     left = merge_sort_asc(l[:len(l) // 2])
#     right = merge_sort_asc(l[len(l) // 2:])
#
#     new_list = []
#
#     while len(left) and len(right):
#         if left[0] < right[0]:
#             new_list.append(left[0])
#             left.pop(0)
#
#         else:
#             new_list.append(right[0])
#             right.pop(0)
#
#     if len(left):
#         new_list += left
#
#     else:
#         new_list += right
#
#     return new_list
#
#
# # Shell Sorting in descending order
# def shell_sort_desc(l: list) -> list:
#     pos = (len(l) - 1) // 2
#
#     while pos:
#         for i in range(len(l)):
#             while i >= pos and l[i] > l[i - pos]:
#                 l[i], l[i - pos] = l[i - pos], l[i]
#                 i -= 1
#
#         pos //= 2
#
#     return l
#
#
# # Shell Sorting in ascending order
# def shell_sort_asc(l: list) -> list:
#     pos = (len(l) - 1) // 2
#
#     while pos:
#         for i in range(len(l)):
#             while i >= pos and l[i] < l[i - pos]:
#                 l[i], l[i - pos] = l[i - pos], l[i]
#                 i -= 1
#
#         pos //= 2
#
#     return l
#
#
# # Quick Sorting in descending order
# def quick_sort_desc(l: list) -> list:
#     if len(l) > 1:
#         element = l[(len(l) - 1) // 2]
#         lt = [x for x in l if x < element]
#         eq = [x for x in l if x == element]
#         gt = [x for x in l if x > element]
#         l = quick_sort_desc(gt) + eq + quick_sort_desc(lt)
#     return l
#
#
# # Quick Sorting in ascending order
# def quick_sort_asc(l: list) -> list:
#     if len(l) > 1:
#         element = l[(len(l) - 1) // 2]
#         lt = [x for x in l if x < element]
#         eq = [x for x in l if x == element]
#         gt = [x for x in l if x > element]
#         l = quick_sort_asc(lt) + eq + quick_sort_asc(gt)
#     return l
#
#
# list_1 = [randint(-100, 100) for _ in range(4)]
# list_2 = [randint(-100, 100) for _ in range(3)]
# list_3 = [randint(-100, 100) for _ in range(2)]
# list_4 = [randint(-100, 100) for _ in range(3)]
# list_ = list_1 + list_2 + list_3 + list_4
# print(list_)
#
# user_choice = int(input('1 - сортировка по убыванию\n2 - сортировка по возрастанию\n-> '))
#
# if user_choice == 1:
#     print('Сортировка пузырьком:', bubble_sort_desc(list_))
#     print('Сортировка слиянием:', merge_sort_desc(list_))
#     print('Сортировка Шелла:', shell_sort_desc(list_))
#     print('Быстрая сортировка:', quick_sort_desc(list_))
# elif user_choice == 2:
#     print('Сортировка пузырьком:', bubble_sort_asc(list_))
#     print('Сортировка слиянием:', merge_sort_asc(list_))
#     print('Сортировка Шелла:', shell_sort_asc(list_))
#     print('Быстрая сортировка:', quick_sort_asc(list_))
# else:
#     raise 'Ошибка! Ввести можно только число 1 или 2'
#
#
# # Линейный поиск (задача №1)
# def search_number(l: list, number: int) -> bool:
#     for num in l:
#         if num == number:
#             return True
#     return False
#
#
# user_number = int(input('\nВведите число: '))
#
# if search_number(list_, user_number):
#     print(f'Число {user_number} найдено')
# else:
#     print(f'Число {user_number} не найдено')