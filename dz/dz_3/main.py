
''' Разработать программу, которая выводит на экран линию из символов.
            Пользователь указывает: число символов, тип символа и
                    ориентацию линии - вертикальную или горизонтальную '''


count = input('Количество символов: ')

while type(count) is str:
    try:
        count = int(count)

    except ValueError:
        count = input('Ошибка ввода! Введите количество символов (целое число): ')

symbol = input('Тип символа: ')
line = input('0 - горизонтальная\n1 - вертикальная\nОриентация линии: ')

while line != '0' and line != '1':
    print('Ошибка ввода! Попробуйте ещё раз!')
    print()
    line = input('0 - горизонтальная\n1 - вертикальная\nОриентация линии: ')

if line == '0':
    while count > 0:
        print(symbol, end=' ')
        count -= 1
    print()

else:
    while count > 0:
        print(symbol)
        count -= 1





''' Необходимо вывести на экран прямоугольник из чередующихся символов '''


i = 0
j = 0

while i < 5:

    if i % 2:
        while j > 0:
            print('-', end='')
            j -= 1

    else:
        while j < 16:
            print('+', end='')
            j += 1

    print()
    i += 1







''' Написать программу нахождения максимального значения из трех чисел введенных пользователем 
                с использованием тернарного выражения '''


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

max_ = 'Введенные числа равны' if number_1 == number_2 == number_3 else 'Максимальное значение: ' + str(number_1) if number_1 > number_2 and number_1 > number_3 else 'Максимальное значение: ' + str(number_2) if number_2 >= number_1 and number_2 > number_3 else 'Максимальное значение: ' + str(number_3)
print(max_)






''' Написать программу "калькулятор" '''



text = '''\n1 - "r" - применяет унарный минус к операнду\n2 - "+" - сложение\n3 - "-" - вычитание\n4 - "/" - деление\n5 - "*" - умножение\n6 - "%" - деление по модулю (остаток от деления)\n7 - "<" - минимальное из двух чисел\n8 - ">" - максимальное из двух чисел\nexit - выйти из калькулятора'''
print(text)
op = None

while op != 'exit':
    op = input('\nВыберите операцию (цифрой): ')

    while op != '1' and op != '2' and op != '3' and op != '4' and op != '5' and op != '6' and op != '7' and op != '8' and op != 'exit':
        op = input('Ошибка ввода! Выберите операцию из предложенного списка (цифрой): ')

    if op == '1':
        number = input('Введите число: ')

        while type(number) is str:
            try:
                number = float(number)

            except ValueError:
                number = input('Ошибка ввода! Введите число: ')

        result = number * (-1)
        result = result if result * 10 % 10 else int(result)

    elif op == 'exit':
        break

    else:
        number_1 = input('Введите первое число: ')

        while type(number_1) is str:
            try:
                number_1 = float(number_1)

            except ValueError:
                number_1 = input('Ошибка ввода! Введите первое число: ')

        number_2 = input('Введите второе число: ')

        while type(number_2) is str:
            try:
                number_2 = float(number_2)

            except ValueError:
                number_2 = input('Ошибка ввода! Введите второе число: ')

        if op == '2':
            result = number_1 + number_2
            result = result if result * 10 % 10 else int(result)

        elif op == '3':
            result = number_1 - number_2
            result = result if result * 10 % 10 else int(result)

        elif op == '4':

            if number_2:
                result = round(number_1 / number_2, 3)
                result = result if result * 10 % 10 else int(result)

            else:
                result = 'На 0 делить нельзя!'

        elif op == '5':
            result = round(number_1 * number_2, 3)
            result = result if result * 10 % 10 else int(result)

        elif op == '6':
            result = number_1 % number_2
            result = result if result * 10 % 10 else int(result)

        elif op == '7':
            number_1 = number_1 if number_1 * 10 % 10 else int(number_1)
            number_2 = number_2 if number_2 * 10 % 10 else int(number_2)
            result = number_1 if number_1 < number_2 else number_2 if number_2 < number_1 else 'Числа равны'

        elif op == '8':
            number_1 = number_1 if number_1 * 10 % 10 else int(number_1)
            number_2 = number_2 if number_2 * 10 % 10 else int(number_2)
            result = number_1 if number_1 > number_2 else number_2 if number_2 > number_1 else 'Числа равны'

    print('Результат:', result)




