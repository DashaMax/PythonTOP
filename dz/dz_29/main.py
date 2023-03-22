''' Создать класс "Треугольник", свойства - длины трех сторон.
    Правильность задания свойств должны проверяться через дескриптор на ввод положительных целых числовых значений.
    Предусмотреть в классе методы проверки существования треугольника. '''


class PositiveInteger:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.__check_value(value)
        instance.__dict__[self.name] = value

    @staticmethod
    def __check_value(value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Сторона треугольника должна быть натуральным числом')


class Triangle:
    a = PositiveInteger()
    b = PositiveInteger()
    c = PositiveInteger()

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def is_exists(self) -> bool:
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        return False


triangles = (
    Triangle(2, 5, 6),
    Triangle(5, 2, 8),
    Triangle(7, 3, 6)
)

for triangle in triangles:
    if triangle.is_exists():
        print(f'Треугольник со сторонами ({triangle.a}, {triangle.b}, {triangle.c}) существует.')
    else:
        print(f'Треугольник со сторонами ({triangle.a}, {triangle.b}, {triangle.c}) не существует.')

triangles[1].b = 4
print(triangles[1].is_exists())