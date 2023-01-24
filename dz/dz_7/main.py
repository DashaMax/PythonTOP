from random import randint, choices
import string


''' Введите статистику частотности символов в кортеже. '''

### Для тестов randint ###
# # tuple_ = tuple([str(randint(0, 9)) for _ in range(randint(8, 15))])




tuple_ = tuple(input('Введите по порядку, без пробелов, элементы кортежа: '))
print(tuple_)
lst = []

for element in tuple_:
    if element not in lst:
        lst.append(element)

for element in lst:
    print(f'Количество {element} = {tuple_.count(element)}')







''' На вход функции поступает список целых чисел. В результате выполнения этой функции будет получен кортеж уникальных элементов списка в обратном порядке. '''

# ### Для тестов randint ###
# # lst = [randint(-10, 10) for _ in range(5, 15)]
# # print(lst)
# # print(tuple_func(lst))




# def tuple_func(lst):
#     list_new = []
#
#     for el in lst[::-1]:
#         if el not in list_new:
#             list_new.append(el)
#
#     return tuple(list_new)
#
#
# # Тесты:
#
# list_1 = [1, 2, 3, 3, 2]
# list_2 = [2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]
# print(tuple_func(list_1))
# print(tuple_func(list_2))







''' Поиск заданного элементы в кортеже. '''

# ### Для тестов randint, choices, string ###
# # str_ = string.ascii_lowercase
# # tuple_ = tuple([''.join(choices(str_, k=randint(2, 3))) for _ in range(randint(5, 10))])
# # print('tuple =', tuple_)
# # s = ''.join(choices(str_, k=randint(2, 3)))
# # print('s =', s)




# tuple_ = ('ab', 'abcd', 'cde', 'abc', 'def')
# s = input('s = ')
# text = 'Yes' if s in tuple_ else 'No'
# print(text)



