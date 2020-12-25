# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
print("=== Задание 1 ===")


def f_delete(arg1, arg2):
    if arg2 == 0:
        print("Деление на ноль!")
    else:
        return arg1 / arg2


f_num = input("Введите первое число: ")
s_num = input("Введите второе число: ")

try:
    f_num = int(f_num)
    s_num = int(s_num)
    if s_num == 0:
        print("Деление на ноль!")
    else:
        print(f"Результат деления: {round(f_delete(f_num, s_num), 2)}")
except ValueError:
    print("Ошибка ввода!")


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
print("\n=== Задание 2 ===")


def my_func1(name, surname, year, city, email, phone):
    return print(f"Имя: {name}, фамилия: {surname}, год рождения: {year}, город: {city}, email: {email}, "
                 f"телефон: {phone}")


my_func1(name=input("Введите имя: "), surname=input("Введите фамилию: "), year=input("Введите год рождения: "),
         city=input("Введите город: "), email=input("Введите email: "), phone=input("Введите телефон: "),)

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
print("\n=== Задание 3 ===")


def my_func2(arg1, arg2, arg3):
    n = (arg1 + arg2 + arg3) - min(arg1, arg2, arg3)
    return n


my_list = input('Введите 3 аргумента (через пробел): ')
my_list = list(my_list.split())
try:
    print(f"Результат: {my_func2(int(my_list[0]), int(my_list[1]), int(my_list[2]))}")
except ValueError:
    print("Ошибка ввода!")

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
print("\n=== Задание 4 ===")


def my_func_pow1(x, y):
    return 1 / (x ** abs(y))


def my_func_pow2(x, y):
    result = x
    i = 1
    for i in range(1, abs(y)):
        result = result * x

    return 1 / result


x = input("Введите положительное число Х: ")
try:
    x = int(x)
    while int(x) <= 0:
        print("Ошибка ввода! Х должен быть больше 0")
        x = input("Введите положительное число Х: ")
        x = int(x)
except ValueError:
    print("Ошибка - X не является числом!")
    exit()

y = input("Введите отрицательное число Y: ")
try:
    y = int(y)
    while int(y) >= 0:
        print("Ошибка ввода! Y должен быть меньше 0")
        y = input("Введите отрицательное число Y: ")
        y = int(y)
except ValueError:
    print("Ошибка - Y не является числом!")
    exit()

print(f"Результат с использованием ** {my_func_pow1(x, y)}")
print(f"Результат без использования ** {my_func_pow2(x, y)}")


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.
print("\n=== Задание 5 ===")


def my_func3(*args):
    i = 0
    global result
    global exit_key
    for i in range(len(my_list)):
        if my_list[i] != "q":
            try:
                result = result + int(my_list[i])
            except:
                print(f"Ошибка ввода! Некорректный символ - {my_list[i]}")
                exit()
        else:
            exit_key = "q"
            break
    return result


result = 0
exit_key = ""
while exit_key != "q":
    my_list = input("Введите строку чисел через пробел или введите q для выхода: ")
    my_list = list(my_list.split())
    print(f"Общая сумма: {my_func3(my_list)}")

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
print("\n=== Задание 6 ===")


def int_func(str_key):
    my_string = "".join(str_key)
    return my_string.title()


def test_lat(my_char):
    if ord(my_char) != 32:
        if ord(my_char) < 97 or ord(my_char) > 122:
            print("Ошибка ввода! Не все символы латинские.")
            exit()


str_list = list(input("Введите слово или строку из слов латинскими буквами: "))
i = 0
for i in range(len(str_list)):
    char = str_list[i]
    test_lat(char)
    i += 1

print(f"Результат: {int_func(str_list)}")