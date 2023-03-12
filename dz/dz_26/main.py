''' Перегрузите операторы '-', '*', '//', '%', '-=', '*=', '//=', '%=' '''


class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int) or sec < 0:
            raise ValueError("Секунды должны быть целым положительным числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        h = (self.sec // 3600) % 24
        m = (self.sec // 60) % 60
        s = self.sec % 60
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    @staticmethod
    def __check_value(value):
        if not isinstance(value, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")

    @staticmethod
    def __check_zero(value):
        if not value:
            raise ZeroDivisionError('Правый операнд не должен быть равен нулю')

    def __add__(self, other):
        self.__check_value(other)
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        self.__check_value(other)
        if self.sec < other.sec:
            raise ArithmeticError('Правый операнд не должен быть больше левого')
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        self.__check_value(other)
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        self.__check_value(other)
        self.__check_zero(other.sec)
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        self.__check_value(other)
        self.__check_zero(other.sec)
        return Clock(self.sec % other.sec)


c1 = Clock(600)
c2 = Clock(200)
print('c1:', c1.get_format_time())
print('c2:', c2.get_format_time())

print('c1 + c2:', (c1 + c2).get_format_time())
print('c1 - c2:', (c1 - c2).get_format_time())
print('c1 * c2:', (c1 * c2).get_format_time())
print('c1 // c2:', (c1 // c2).get_format_time())
print('c1 % c2:', (c1 % c2).get_format_time())

# c1 += c2
# print('c1 += c2:', c1.get_format_time())
c1 -= c2
print('c1 -= c2:', c1.get_format_time())
# c1 *= c2
# print('c1 *= c2:', c1.get_format_time())
# c1 //= c2
# print('c1 //= c2:', c1.get_format_time())
# c1 %= c2
# print('c1 %= c2:', c1.get_format_time())
