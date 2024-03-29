# Задание на семинаре
# Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

# a = complex(2, 3)
# b = complex(4, 5)
# c = complex(6, 7)

a = 1
b = -2
c = 5

d = b ** 2 - 4 * a * c
print(f'Дискриминант = {d}')

x_1 = (-1) * b + pow(d, 0.5) / 2 * a
x_2 = (-1) * b - pow(d, 0.5) / 2 * a
print(f'Корни квадратного уравнекния {x_1}, {x_2}')