''' Разработать класс Sphere для представления сферы в трёхмерном пространстве.
 Создать в классе набор методов:
 get_volume(), get_square(), get_radius(), get_center()
 set_radius(r), set_center(x, y, z), is_point_inside(x, y, z). '''


from math import pi


class Sphere:

    # Для представления сферы в трехмерном пространстве необходимы
    #       координаты центра сферы (x0, y0, z0) и радиус сферы (R)
    def __init__(self, x, y, z, r):
        if self.__checked_value(x) and self.__checked_value(y) \
                and self.__checked_value(z) and self.__checked_value(r):
            self.__x0 = x
            self.__y0 = y
            self.__z0 = z
            self.__R = r
        else:
            self.__x0 = self.__y0 = self.__z0 = self.__R = 0
            print('Ошибка типа данных!')

    def get_radius(self):
        return self.__R

    def set_radius(self, r):
        if self.__checked_value(r):
            self.__R = r
        else:
            print('Ошибка типа данных!')

    def get_center(self):
        return self.__x0, self.__y0, self.__z0

    def set_center(self, x, y, z):
        if self.__checked_value(x) and self.__checked_value(y) \
                and self.__checked_value(z):
            self.__x0 = x
            self.__y0 = y
            self.__z0 = z
        else:
            print('Ошибка типа данных!')

    def get_valume(self):
        return 4 * pi * self.get_radius() ** 3 / 3

    def get_square(self):
        return 4 * pi * self.get_radius() ** 2

    # Для проверки попадания точки с координатами (x, y, z) внутрь сферы воспользуемся неравенством
    #       (x - x0)^2 + (y - y0)^2 + (z - z0)^2 < R^2, где (x0, y0, z0) - координаты центра сферы, R - радиус
    def is_point_inside(self, x, y, z):
        d = (x - self.__x0) ** 2 + (y - self.__y0) ** 2 + (z - self.__z0) ** 2
        return True if d < self.get_radius() ** 2 else False

    @staticmethod
    def __checked_value(value):
        return True if isinstance(value, (int, float)) else False


sphere = Sphere(0, 0, 0, 0.6)
print(f'Радиус сферы:', sphere.get_radius())
print(f'Объем сферы:', sphere.get_valume())
print(f'Площадь поверхности:', sphere.get_square())
print(f'Координаты центра:', sphere.get_center())
print(f'Точка с координатами (0, -1.5, 0):', sphere.is_point_inside(0, -1.5, 0))

sphere.set_radius(1.6)
print(f'\nРадиус сферы:', sphere.get_radius())
print(f'Точка с координатами (0, -1.5, 0):', sphere.is_point_inside(0, -1.5, 0))