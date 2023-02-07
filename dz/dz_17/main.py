''' Валидация номера телефона. '''


import re


string_numbers = '''
+7 499 456-45-78
+74994564578
74991234567
7 (499) 456 45 78
7 (499) 456-45-78
+7 495 123 45 67
7(495)1234567
7-495-123-45-67'''
list_check = re.findall(r'\+?7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}', string_numbers)
print(list_check)





''' Вычислить количество отрицательных чисел в списке. '''


# def count_negative_digits(l: list) -> int:
#     if len(l) == 1:
#         return 1 if l[0] < 0 else 0
#     n = count_negative_digits(l[1:])
#     if l[0] < 0:
#         n += 1
#     return n
#
#
# list_numbers = [-2, 3, 8, -11, -4, 6]
# print('n =', count_negative_digits(list_numbers))
