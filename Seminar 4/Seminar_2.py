# 1 Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.

lst = list(map(int, input("Введите числа через запятую:").split(',')))
print(lst)

print(f'Максимальное значение: {max(lst)}, минимальное значение: {min(lst)}')