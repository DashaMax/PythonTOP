'''Обмен значениями'''

a, b = 1, 2
print(f'Начальные значения:\na: {a}\nb: {b}\n')

a, b = b, a
print(f'Обмен №1:\na: {a}\nb: {b}\n')

a, b = 1, 2
c = a
a = b
b = c
print(f'Обмен №2:\na: {a}\nb: {b}\n')

a, b = 1, 2
a += b
b = a - b
a -= b
print(f'Обмен №3:\na: {a}\nb: {b}\n')

a, b = 1, 2
a *= b
b = a // b
a //= b
print(f'Обмен №4:\na: {a}\nb: {b}\n')
