''' Написать функцию, вычисляющую площадь прямоугольного параллелепипеда с ребрами a, b и c. Данная функция должна содержать внутри себя ещё одну функцию, вычисляющую площадь прямоугольника. Решить задачу для случаев, когда общая площадь определена как глобальная и как локальная переменная. Внести изменения в функции таким образом, чтобы общая площадь могла использоваться как нелокальная переменная. '''


# Способ №1 - Общая площадь (S) определена как глобальная переменная

S = 0


def area_parallelepiped(a, b, c):
    global S

    def area_rectangle(side1, side2):
        return side1 * side2

    S = (area_rectangle(a, b) + area_rectangle(a, c) + area_rectangle(b, c)) * 2


area_parallelepiped(2, 4, 6)
print(S)



# # Способ №2 - Общая площадь (S) определена как локальная переменная
#
#
# def area_parallelepiped(a, b, c):
#     def area_rectangle(side1, side2):
#         return side1 * side2
#
#     S = (area_rectangle(a, b) + area_rectangle(a, c) + area_rectangle(b, c)) * 2
#     return S
#
#
# print(area_parallelepiped(5, 8, 2))



# # Способ №3 - Использование общей площади (S) как нелокальной переменной
#
# def area_parallelepiped(a, b, c):
#     S = 0
#
#     def area_rectangle():
#         nonlocal S
#         S = (a * b + a * c + b * c) * 2
#
#     area_rectangle()
#     return S
#
#
# print(area_parallelepiped(1, 6, 8))