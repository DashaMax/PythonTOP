from math import pi


def rectangle_square(a, b):
    return a * b


def triangle_square(a, h):
    return 0.5 * a * h


def circle_square(R):
    return round(pi * R ** 2, 2)


text = 'Площадь какой фигуры хотите найти?\n(1 - прямоугольник, 2 - треугольник, 3 - круг)\nВведите цифру: '
n = int(input(text))

if n == 1:
    a_, b_ = int(input('Длина прямоугольника: ')), int(input('Ширина прямоугольника: '))
    result = rectangle_square(a_, b_)

elif n == 2:
    a_, h_ = int(input('Основание треугольника: ')), int(input('Высота треугольника: '))
    result = triangle_square(a_, h_)

elif n == 3:
    R_ = int(input('Радиус круга: '))
    result = circle_square(R_)

else:
    result = 'error'

print('Площадь:', result)