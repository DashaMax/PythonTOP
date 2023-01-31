import re


''' Проверка соответствия пароля. Он может/должен состоять из цифр, букв английского алфавита, символов дефис, собака и подчеркивание. Длина пароля от 6 до 18 символов. '''


import random
import string


# Генерируем пароль (для проверки добавляем ещё 3 символа русского алфавита)
symbols = 'йцё' + string.ascii_letters + string.digits + '_@-'
password = ''.join(random.choice(symbols) for _ in range(random.randint(6, 18)))


# Решение №1 - пароль МОЖЕТ содержать указанные символы
def check_password(password):
    check = re.search(r'^[a-zA-Z\d@_-]{6,18}$', password)
    return bool(check)


# Решение №2 - пароль ДОЛЖЕН содержать символы английского алфавита, цифры и символы (@_-)
# def check_password(password):
#     check = all([re.search(r'^[a-zA-Z\d@_-]{6,18}$', password), re.search(r'[a-zA-Z]', password), re.search(r'\d', password), re.search(r'[_@-]', password)])
#     return check


print(f'Пароль: {password}')
print(f'Результат проверки: {check_password(password)}')






''' Найти дату в формате: dd/mm/YYYY '''


# test = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков.'
#
# # Год с 1000 до 2099
# dates = re.findall(r'((?:0[1-9]|[12]\d|3[01])/(?:0[1-9]|1[0-2])/(?:1\d|20)\d{2})', test)
# print(dates)