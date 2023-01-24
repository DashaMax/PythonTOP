''' Создать функцию, которая будет находить сумму любого количества чисел и декоратор, который будет находить среднее арифметическое этих чисел. '''


def decorator(func):
    def wrapper(*args):
        if args and all(isinstance(x, int) or isinstance(x, float) for x in args):
            summa = func(*args)
            print(f'Сумма чисел {", ". join(str(x) for x in args)} = {summa}')
            print(f'Среднее арифметическое чисел {", ". join(str(x) for x in args)} = {round(summa / len(args), 3)}')
        else:
            raise 'Список элементов пуст или неверный тип данных'
    return wrapper


@decorator
def func_sum(*args):
    return sum(args)


func_sum(2, 3, 3, 4)
