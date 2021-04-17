import math


print("Введите коэффициенты квадратного уравнения: ")


print("ax^2 + bx + c = 0:")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

discr = (b ** 2) - (4 * a * c)
print("Дискриминант этого уравнения равен", discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2*a)
    x2 = (-b - math.sqrt(discr)) / (2*a)
    print("Первый корень равен - ", x1)
    print("Второй корень равен - ", x2)
elif discr < 0:
    print("Корней нет!")

elif discr == 0:
    x1 = (-b / 2) * a

input("Работа закончена, нажмите любую кнопку, чтобы выйти из программы")