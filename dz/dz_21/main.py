''' Создать класс Rectangle, описывающий прямоугольник.
    В классе должны быть все необходимые методы,
    а также методы вычисления площади, периметра, диагонали
    и метод, который рисует прямоугольник. '''


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_square(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_diagonal(self):
        return round((self.a ** 2 + self.b ** 2) ** 0.5, 2)

    def draw_rectangle(self):
        drawing = ('*  ' * self.a + '\n') * self.b
        print(drawing)


a_user = int(input('Длина прямоугольника: '))
b_user = int(input('Ширина прямоугольника: '))

rectangle = Rectangle(a_user, b_user)
print('Площадь прямоугольника:', rectangle.get_square())
print('Периметр прямоугольника:', rectangle.get_perimeter())
print('Диагональ прямоугольника:', rectangle.get_diagonal())
rectangle.draw_rectangle()



