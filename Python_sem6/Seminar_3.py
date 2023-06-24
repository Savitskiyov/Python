# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

def my_func(text = "Сорок одежок и все без застежок", solution = ['капуста', 'капустка'], attemt =5):
    count = 1
    print(f"Отгадайте загадку: {text}")

    while count<attemt:
        a = input("Введите отгадку: ").lower()
        if a in solution:
            print (f"Вы отгадали за {count} попытку")
            return count
        else:
            print(f"Ошибка")
            count += 1
        if count == attemt:
            print (f"Вы исчерпали количество попыток")
            return 0


if "__main__" == __name__:
    print(my_func())