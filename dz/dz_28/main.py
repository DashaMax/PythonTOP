''' Создать класс Shape и три дочерних класса: Square, Rectangle, Triangle.
    Родительский класс должен иметь абстрактные методы нахождения периметра, площади,
                                                рисования фигуры и вывода информации.
    С помощью полиморфизма реализуйте вывод информации о дочерних фигурах. '''


class Shape:
    def __init__(self, name: str, color: str):
        self.name = name
        self.__check_color(color)
        self.color = color

    def get_perimetr(self):
        raise NotImplementedError('Необходимо определить метод нахождения периметра фигуры')

    def get_area(self):
        raise NotImplementedError('Необходимо определить метод нахождения площади фигуры')

    def draw(self):
        raise NotImplementedError('Необходимо определить метод рисования фигуры')

    def get_info(self):
        raise NotImplementedError('Необходимо определить метод вывода информации')

    def check_value(self, value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError(f'Сторона фигуры {self.name} должна быть натуральным числом')

    def __check_color(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Цвет фигуры {self.name} должен быть строковым типом данных')


class Square(Shape):
    def __init__(self, side: int, color: str):
        super(Square, self).__init__('квадрат', color)
        self.check_value(side)
        self.side = side

    def get_perimetr(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2

    def draw(self):
        print(('*  ' * self.side + '\n') * self.side)

    def get_info(self):
        info = f'==={self.name.capitalize()}===\nСторона: {self.side}\nЦвет: {self.color}'
        return info


class Rectangle(Shape):
    def __init__(self, length: int, width: int, color: str):
        super(Rectangle, self).__init__('прямоугольник', color)
        self.check_value(length)
        self.check_value(width)
        self.length = length
        self.width = width

    def get_perimetr(self):
        return (self.width + self.length) * 2

    def get_area(self):
        return self.width * self.length

    def draw(self):
        print(('*  ' * self.length + '\n') * self.width)

    def get_info(self):
        info = f'==={self.name.capitalize()}===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}'
        return info


class Triangle(Shape):
    def __init__(self, a: int, b: int, c: int, color: str):
        super(Triangle, self).__init__('треугольник', color)
        self.check_value(a)
        self.check_value(b)
        self.check_value(c)
        self.__check_triangle(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def get_perimetr(self):
        return self.a + self.b + self.c

    def get_area(self):
        p = self.get_perimetr() / 2
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, 2)

    def draw(self):
        sides = [self.a, self.b, self.c]
        c = max(sides)
        sides.remove(c)
        a, b = min(sides), max(sides)
        cos_a = (c ** 2 + b ** 2 - a ** 2) / (2 * c * b)
        cos_b = (c ** 2 + a ** 2 - b ** 2) / (2 * c * a)
        c_a = int(a * cos_b) if a * cos_b - int(a * cos_b) < 0.5 else int(a * cos_b) + 1
        c_b = int(b * cos_a) if b * cos_a - int(b * cos_a) < 0.5 else int(b * cos_a) + 1
        n = round(c_b / c_a)

        for i in range(c_a):
            if i == 0:
                print('  ' * c_a + '*')
            else:
                print('  ' * (c_a - i) + '* ' * (i + 1), end='')
                print('* ' * i * n)

    def get_info(self):
        info = f'==={self.name.capitalize()}===\nСторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}\nЦвет: {self.color}'
        return info

    @staticmethod
    def __check_triangle(a, b, c):
        if not (a < b + c and c < a + b and b < a + c):
            raise TypeError('Стороны треугольника заданы неверно')


shapes = (
    Square(3, 'red'),
    Rectangle(7, 3, 'green'),
    Triangle(11, 6, 6, 'yellow')
)

for shape in shapes:
    print(shape.get_info())
    print('Площадь:', shape.get_area())
    print('Периметр:', shape.get_perimetr())
    shape.draw()