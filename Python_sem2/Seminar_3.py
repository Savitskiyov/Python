# Задание на семинаре
# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
import math
import decimal

while True:
    diam = int(input('Введите диаметр окружности: '))
    if diam <= 1000: break

decimal.getcontext().prec = 42
square = decimal.Decimal(math.pi * diam * diam / 4)
lenght = decimal.Decimal(math.pi * diam)
print(f'Площадь круга = {square}')
print(f'Длина окружности ={lenght}')

