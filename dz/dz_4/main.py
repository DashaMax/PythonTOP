
''' Напишите программу заполнения списка положительными и отрицательными элементами.
        Из него требуется сформировать новый массив только из положительных элементов.
            Найти из них наибольший элемент. Распечатать новый массив и наибольший элемент. '''


list_nums = []
list_positive = []

for i in range(int(input('Введите длину списка: '))):
    num = int(input('Введите элемент списка: '))
    list_nums.append(num)
    if num > 0:
        list_positive.append(num)

print('Список:', list_nums)
print('Новый список, состоящий из положительных элементов:', list_positive)

max_ = list_positive[0]

for element in list_positive:
    max_ = element if element > max_ else max_

print('Наибольший элемент списка:', max_)








''' Дан список целых чисел, число k и значение C. 
        Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, 
                имевшие индекс не менее k, вправо. '''


# list_nums = []
#
# for i in range(int(input('Введите элементы списка:\nn = '))):
#     list_nums.append(int(input('-> ')))
#
# k = int(input('Введите индекс:\nk = '))
# C = int(input('Введите значение:\nC = '))
# list_nums.insert(k, C)
# print(list_nums)









''' Сформировать список квадратов чисел от 1 до 10 (с помощью метода append()) '''


# list_square = []
#
# for num in range(1, 11):
#     list_square.append(num ** 2)
#
# print('Список квадратов =', list_square)




