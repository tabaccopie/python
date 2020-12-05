# ============= 1 =============
class Matrix:
    """Класс для обработки матриц одинаковой размерности.
        Выводим матрицы в "классическом" виде. Суммируем матрицы."""

    def __init__(self, list_x):
        self.my_list = list_x

    def __str__(self):
        for row in self.my_list:
            for el in row:
                print(el, end='\t')
            print()
        return f"=================="

    def __add__(self, other):
        tmp_list1 = []
        for x, y in zip(self.my_list, other.my_list):
            tmp_list2 = []
            for i, j in zip(x, y):
                tmp_list2.append(int(i) + int(j))
            tmp_list1.append(tmp_list2)
        for row in tmp_list1:
            for el in row:
                print(el, end='\t')
            print()
        return "=================="


# создаем объекты
matr1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
matr2 = Matrix([[8, 9, 10], [10, 11, 12], [7, 8, 9]])

# вызываем объекты (__str__)
print(matr1)
print(matr2)

# складываем объекты (__add__)
print(matr1 + matr2)

# ============== 2 =================
from abc import ABC, abstractmethod


class Clothes(ABC):
    """Класс Одежда с 3 параметрами"""

    def __init__(self, name, size, height):
        self.size = size
        self.height = height
        self.name = name

    @abstractmethod
    def get_square(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name, size, 1)
        # сразу вычисляем площадь
        self.c_square = self.size / 6.5 + 0.5

    # обязательный метод вывода площади делаем через property
    @property
    def get_square(self):
        return f"Площадь ткани на {self.name} (Property) {self.c_square}"

    def __str__(self):
        return f'Площадь ткани на {self.name} {self.c_square}'

    # реализуем сложение площадей ткани одежды
    def __add__(self, other):
        return f"Общая площадь ткани {self.name} + {other.name} {self.c_square + other.c_square}"


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name, height, 1)
        # сразу вычисляем площадь
        self.c_square = 2 * self.height + 0.3

    # обязательный метод вывода площади делаем через property
    @property
    def get_square(self):
        return f"Площадь ткани на {self.name} (Property) {self.c_square}"

    def __str__(self):
        return f'Площадь ткани на {self.name} {self.c_square}'

    # реализуем сложение площадей ткани одежды
    def __add__(self, other):
        return f"Общая площадь ткани {self.name} + {other.name} {self.c_square + other.c_square}"


# создаем объекты
my_coat = Coat("Пальтишко", 52)
my_suit = Suit("Костюмчик", 7)

# вызываем объекты (__str__)
print(my_coat)
print(my_suit)

# обращаемся к property
print(my_coat.get_square)
print(my_suit.get_square)

# складываем площади
print(my_coat + my_suit)
print(my_suit + my_coat)


# ============= 3 ==============
class Cell:
    """Класс Клетка. Вполняет арифметические операции между клетками"""

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return f"Результат сложения клеток: {self.number + other.number}"

    def __sub__(self, other):
        return f"Результат вычитания клеток: {self.number - other.number}" if other.number < self.number else "Ошибка вычитания! "

    def __mul__(self, other):
        return f"Результат умножения клеток: {self.number * other.number}"

    def __truediv__(self, other):
        return f"Результат деления клеток (с округлением): {round(self.number / other.number)}\n"

    def make_order(self, arg):
        print(f"Визуализация клетки по рядам в {arg}:")
        i = 0
        for i in range(0, self.number // arg):
            print("*" * arg)
            i += 1
        print("*" * (self.number - arg * i))
        return "================"


my_cell1 = Cell(12)
my_cell2 = Cell(7)
print(my_cell1 + my_cell2)
print(my_cell1 - my_cell2)
print(my_cell1 * my_cell2)
print(my_cell1 / my_cell2)
print(my_cell1.make_order(5))
print(my_cell2.make_order(3))
print(my_cell1.make_order(8))
