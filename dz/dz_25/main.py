''' Создать класс Student, который будет содержать имя и распечатывать информацию,
    а также вложенный класс, который будет содержать информацию о ноутбуке
    с техническими характеристиками: модель, процессор и память. '''


# Вариант №1
class Student:
    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    def get_info(self):
        info = f'{self.name} => {self.laptop.model}, {self.laptop.processor}, {self.laptop.memory}'
        return info

    class Laptop:
        def __init__(self):
            self.model = 'HP'
            self.processor = 'i7'
            self.memory = 16


# # Вариант №2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.laptop = self.Laptop()
#
#     def get_info(self):
#         info = f'{self.name} => {self.laptop.MODEL}, {self.laptop.PROCESSOR}, {self.laptop.MEMORY}'
#         return info
#
#     class Laptop:
#         MODEL = 'HP'
#         PROCESSOR = 'i7'
#         MEMORY = 16


user1 = Student('Roman')
user2 = Student('Vladimir')
print(user1.get_info())
print(user2.get_info())