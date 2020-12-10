# ============ 1 ============
class MyDate:
    date_list = []

    def __init__(self, date_list):
        self.date_list = date_list

    @staticmethod
    def date_val(date_list):
        """Метод для валидации даты"""
        month_list = [1, 3, 5, 7, 8, 10, 12]

        # проверка количества знаков в году
        if len(str(date_list[2])) > 4:
            return "Ошибка! В году допускается не более 4 знаков!"

        # проверяем все числа на неверный ввод (меньше 1)
        for i in range(len(date_list)):
            if date_list[i] < 1:
                return "Неверный ввод даты!"

        # проверяем количество месяцев
        if date_list[1] > 12:
            return "Месяц не должен быть больше 12!"

        # проверяем количество дней в феврале
        if date_list[1] == 2 and date_list[0] > 28:
            return f"Неверно введен день месяца февраль {date_list[0]}"

        # проверяем остальные месяцы
        for i in month_list:
            if date_list[1] == i:
                if date_list[0] > 31:
                    return f"Неверно введен день месяца {date_list[0]}"
            else:
                if date_list[0] > 30:
                    return f"Неверно введен день месяца {date_list[0]}"

        return f"Дата {date_list[0]}-{date_list[1]}-{date_list[2]} введена верно"

    @classmethod
    def str_to_date(cls, my_str):
        """Метод для приведение строки к списку с числовыми элементами"""
        return list(map(int, my_str.split("-")))


my_date = input("Введите дату в формате ДД-ММ-ГГГГ: ")
date_list = MyDate(my_date)
# print(date_list.str_to_date(my_date))
print(date_list.date_val(MyDate.str_to_date(my_date)))


# =============== 2 ===================
class ZeroError(Exception):
    """Класс проверки деления на ноль"""

    def __init__(self):
        print("Деление на ноль!")
        exit()


# функция для проверки ввода строка или число
def my_err_func(my_str):
    try:
        my_str = int(my_str)
    except ValueError:
        print("Это не число!")
        exit()


# получаем аргументы и сразу проверяем на правильность ввода
my_arg1 = input("Введите arg1:")
my_err_func(my_arg1)
my_arg2 = input("Введите arg2:")
my_err_func(my_arg2)

# обработка ошибки и расчет результата
try:
    int(my_arg1) / int(my_arg2)
except ZeroDivisionError:
    raise ZeroError
else:
    print(f"Результат: {int(my_arg1) / int(my_arg2)}")


# ============== 3 ===================
class CheckData(Exception):
    """Класс для обработки ошибки"""

    def __init__(self, txt):
        self.txt = txt


my_arg = ""
my_list = []
# создаем бесконечный цикл
while True:
    my_arg = input("Введите значение (число) списка или stop для остановки: ")
    # проверяем на слово stop, которое останавливает запрос значений и выводит результат
    if my_arg != "stop":
        # обработчик ошибки
        try:
            int(my_arg)
        except ValueError:
            print(CheckData("Вы ввели не число!"))
        else:
            # заполняем лист значений
            my_list.append(my_arg)
    else:
        # выводим результат и останавливаем работу
        print(my_list)
        break


# =================== 4, 5, 6 ======================
class MyStorage:
    """Класс Склад."""
    dict_storage = {}

    # добавляем устройство на склад
    def add_item(self, name, color, prop, eq_type):
        if name not in self.dict_storage:
            self.dict_storage[name] = [eq_type, color, prop]
            print(f"Устройство {name} успешно добавлено.")
        else:
            print(f"Устройство с именем {name} уже есть на складе!")

    # перемещаем устройство со склада
    def remove_item(self, name):
        try:
            self.dict_storage.pop(name)
            print(f"Устройство {name} успешно удалено со склада.")
        except KeyError:
            print(f"Нет устройства с именем {name}!")

    # выводим список устройств на складе
    def print_items(self):
        print("На данный момент на складе в наличии следующие устройства:\n ======================\n")
        for i in self.dict_storage:
            print(f"{i} - {self.dict_storage[i]} \n")


class OfficeEquip:
    """Родительский класс для устройств"""

    def __init__(self, name, eq_type, color):
        self.name = name
        self.color = color
        self.eq_type = eq_type


class Printer(OfficeEquip):
    """Класс для устройства типа Принтер"""

    def __init__(self, name, color, prn_prop, eq_type="Printer"):
        super().__init__(name, eq_type, color)
        self.prn_prop = prn_prop


class Scanner(OfficeEquip):
    """Класс для устройства типа Сканер"""

    def __init__(self, name, color, scan_prop, eq_type="Scanner"):
        super().__init__(name, eq_type, color)
        self.scan_prop = scan_prop


class Copyist(OfficeEquip):
    """Класс для устройства типа Копир"""

    def __init__(self, name, color, copy_prop, eq_type="Copyist"):
        super().__init__(name, eq_type, color)
        self.copy_prop = copy_prop


my_storage = MyStorage()
# создаем бесконечный цикл запроса параметров
while True:
    # главное меню
    try:
        main_menu = int(input("Выберите действия: \n 1 - Добавить устройство на склад. \n 2 - Удалить устройство со "
                              "склада.\n 3 - Показать устройства на складе.\n 4 - Выход.\n"))
    except ValueError:
        print("Неверный ввод!")
    # выход из цикла
    if main_menu == 4:
        break
    # обработка вывода устройств на складе
    elif main_menu == 3:
        my_storage.print_items()
    # добавляем устройство на склад
    elif main_menu == 1:
        # цикл запроса параметров
        while True:
            # главное меню добавления устройств
            try:
                add_menu = int(input("Какое устройство добавить: \n 1 - Принтер. \n 2 - Сканер. \n 3 - Копир.\n 4 - "
                                     "Выход в главное меню.\n"))
            except ValueError:
                print("Неверный ввод!")
            # выход из цикла
            if add_menu == 4:
                break
            # добавляем принтер
            elif add_menu == 1:
                my_prn_name = input("Введите имя принтера: ")
                my_prn_color = input("Введите цвет: ")
                my_prn_prop = input("Введите дополнительное свойство: ")
                my_storage.add_item(my_prn_name, my_prn_color, my_prn_prop, eq_type="Printer")
            # добавляем сканер
            elif add_menu == 2:
                my_scan_name = input("Введите имя сканера: ")
                my_scan_color = input("Введите цвет: ")
                my_scan_prop = input("Введите дополнительное свойство: ")
                my_storage.add_item(my_scan_name, my_scan_color, my_scan_prop, eq_type="Scanner")
            # добавляем копир
            elif add_menu == 3:
                my_copy_name = input("Введите имя копира: ")
                my_copy_color = input("Введите цвет: ")
                my_copy_prop = input("Введите дополнительное свойство: ")
                my_storage.add_item(my_copy_name, my_copy_color, my_copy_prop, eq_type="Copyist")
            # отработка ввода не указаных цифр в меню
            else:
                print("Неверный ввод!")
    # перемещение устройства со склада
    elif main_menu == 2:
        del_name = input("Введите имя устройства для удаления со склада: ")
        my_storage.remove_item(del_name)

print("Работа программы завершена. Спасибо.")


# ================ 7 ==================
class MyComplNum:
    """Класс комплексное число. Перегрузка сложения и умножения."""

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        # получаем листы с числами из строки
        list1 = self.num.replace("+", " ").replace("i", "").split()
        list2 = other.num.replace("+", " ").replace("i", "").split()
        # складываем по формуле z = (a1+a2) + (b1+b2)i
        return f"{int(list1[0]) + int(list2[0])} + {int(list1[1]) + int(list2[1])}i"

    def __mul__(self, other):
        # получаем листы с числами из строки
        list1 = self.num.replace("+", " ").replace("i", "").split()
        list2 = other.num.replace("+", " ").replace("i", "").split()
        # умножаем по формуле z1z2 = (ac-bd) + (ad+cb)i
        return f"{int(list1[0]) * int(list2[0]) - int(list1[1]) * int(list2[1])} + {int(list1[0]) * int(list2[1]) + int(list1[1]) * int(list2[0])}i "


num1 = input("Введите первое неотрицательное комплексное число (шаблон: 5+3i): ")
num2 = input("Введите второе неотрицательное комплексное число (шаблон: 5+3i): ")
print(f"Результат сложения чисел: {MyComplNum(num1) + MyComplNum(num2)}")
print(f"Результат умножения чисел: {MyComplNum(num1) * MyComplNum(num2)}")
