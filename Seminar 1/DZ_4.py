# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
X = int(input("Укажите номер четверти: "))
def quarter (num):
    if num > 4 or num <= 0:
        print('Такой четверти нет')
    elif num == 4:
        print('Диапазон возможных координат от n до -n')
    elif num == 3:
        print('Диапазон возможных координат от -n до -n')
    elif num == 2:
        print('Диапазон возможных координат от -n до n')
    else:
        print('Диапазон возможных координат от n до n')

quarter(X)