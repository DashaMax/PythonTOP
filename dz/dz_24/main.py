''' Создать класс Pair (пара чисел) со свойствами:
    числа A и B и методами:
    изменение чисел, вычисление их произведения и суммы.

    Определить производный класс Right Triangle (прямоугольный треугольник) со свойствами:
    катеты A и B и методами:
    вычисление гипотенузы, площади треугольника, вывод информации о фигуре на экран.
'''


class Pair:
    def __init__(self, a: (int, float), b: (int, float)):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__check_value(value)
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__check_value(value)
        self.__b = value

    @staticmethod
    def __check_value(value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise TypeError('Вводимое значение должно быть положительным числом')

    def get_multy(self):
        return f'Произведение: {self.__a * self.__b}'

    def get_summa(self):
        return f'Сумма: {self.__a + self.__b}'


class RightTriangle(Pair):
    def __init__(self, a: (int, float), b: (int, float)):
        super(RightTriangle, self).__init__(a, b)

    def get_hypotenuse(self):
        return round((self.a ** 2 + self.b ** 2) ** 0.5, 2)

    def get_square(self):
        return round(self.a * self.b / 2, 2)

    def __str__(self):
        text = f'Прямоугольный треугольник △ABC ({self.a}, {self.b}, {self.get_hypotenuse()})'
        return text

    # ИЛИ
    # def get_info(self):
    #     text = f'Прямоугольный треугольник △ABC ({self.a}, {self.b}, {self.get_hypotenuse()})'
    #     return text


triangle = RightTriangle(5, 8)
print(f'Гипотенуза △ABC: {triangle.get_hypotenuse()}')
print(triangle)
print(f'Площадь △ABC: {triangle.get_square()}')

print(triangle.get_summa())
print(triangle.get_multy())

triangle.a = 10
print(f'Гипотенуза △ABC: {triangle.get_hypotenuse()}')

triangle.b = 20
print(f'Гипотенуза △ABC: {triangle.get_hypotenuse()}')

print(triangle.get_summa())
print(triangle.get_multy())
print(f'Площадь △ABC: {triangle.get_square()}')
