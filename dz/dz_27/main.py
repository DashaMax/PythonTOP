''' Напишите класс Point3D для хранения координат в трехмерном пространстве (x, y, z).
 Реализуйте перегрузку операторов сложения, вычитания, умножения и деления для этого класса.
 Также сделайте возможность сравнения координат между собой и запись/считывание значений через ключи: "x", "y", "z".
'''


class Point3D:
    def __init__(self, x: (int, float), y: (int, float), z: (int, float)):
        self.__check_value(x)
        self.__check_value(y)
        self.__check_value(z)
        self.__x = x
        self.__y = y
        self.__z = z

    def __getitem__(self, item):
        if item == 'x':
            return self.__x
        elif item == 'y':
            return self.__y
        elif item == 'z':
            return self.__z
        raise KeyError('ошибка ключа')

    def __setitem__(self, key, value):
        self.__check_value(value)
        print(f'Запись значения в координату {key}: {value}')

        if key == 'x':
            self.__x = value
        elif key == 'y':
            self.__y = value
        elif key == 'z':
            self.__z = value
        else:
            raise KeyError('ошибка ключа')

    def __add__(self, other):
        self.__check_class(other)
        add = Point3D(self.__x + other['x'], self.__y + other['y'], self.__z + other['z'])
        return add['x'], add['y'], add['z']

    def __sub__(self, other):
        self.__check_class(other)
        sub = Point3D(self.__x - other['x'], self.__y - other['y'], self.__z - other['z'])
        return sub['x'], sub['y'], sub['z']

    def __mul__(self, other):
        self.__check_class(other)
        mul = Point3D(self.__x * other['x'], self.__y * other['y'], self.__z * other['z'])
        return mul['x'], mul['y'], mul['z']

    def __truediv__(self, other):
        self.__check_class(other)
        if other['x'] == 0 or other['y'] == 0 or other['z'] == 0:
            raise ZeroDivisionError('деление на ноль невозможно')

        div = Point3D(round(self.__x / other['x'], 3), round(self.__y / other['y'], 3), round(self.__z / other['z'], 3))
        return div['x'], div['y'], div['z']

    def __eq__(self, other):
        self.__check_class(other)
        return self.__x == other['x'] and self.__y == other['y'] and self.__z == other['z']

    def __le__(self, other):
        self.__check_class(other)
        return self.__x <= other['x'] and self.__y <= other['y'] and self.__z <= other['z']

    def __ge__(self, other):
        self.__check_class(other)
        return self.__x >= other['x'] and self.__y >= other['y'] and self.__z >= other['z']

    @staticmethod
    def __check_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError('координата должна быть числом')

    @staticmethod
    def __check_class(value):
        if not isinstance(value, Point3D):
            raise TypeError('правый операнд должен быть типом Point3D')


point1 = Point3D(12, 15, 18)
point2 = Point3D(6, 3, 9)
print(f"Координаты первой точки: {point1['x']}, {point1['y']}, {point1['z']}")
print(f"Координаты второй точки: {point2['x']}, {point2['y']}, {point2['z']}")
print(f"Сложение координат: {point1 + point2}")
print(f"Вычитание координат: {point1 - point2}")
print(f"Умножение координат: {point1 * point2}")
print(f"Деление координат: {point1 / point2}")
print(f"Равенство координат: {point1 == point2}")

point1['x'] = 20

print(point1 >= point2)
print(point2 <= point1)


