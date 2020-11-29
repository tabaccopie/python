# ======== 1 ========
from time import sleep


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self, cycle, color=__color):
        print(f"Режимы работы светофора ({cycle} циклов)\n")

        def timer(num):
            sleep(num)

        def out_red(text):
            print(f"\033[7m\033[31m {text}")

        def out_yellow(text):
            print(f"\033[7m\033[33m {text}")

        def out_green(text):
            print(f"\033[7m\033[32m {text}")

        i = 0
        while i < cycle:
            for my_color in color:
                if my_color == "Red":
                    out_red("Красный свет 7 секунд")
                    timer(7)
                if my_color == "Yellow":
                    out_yellow("Желтый свет 2 секунды")
                    timer(2)
                if my_color == "Yellow":
                    out_green("Зеленый свет 7 секунд")
                    timer(7)

            # out_yellow("Желтый свет 2 секунды")
            # timer(2)
            i += 1


my_traffic_light = TrafficLight()
my_traffic_light.running(3)


# ========= 2 ==========
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        mass = 25
        thickness = 5
        print(f"Результат расчета: {self._width}м * {self._length}м * "
              f"{mass}кг * {thickness}см = {(float(self._width) * float(self._length) * mass * thickness) / 1000}т")


my_road = Road(5000, 20)
my_road.calc()


# ======== 3 =========
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(f"Оклад плюс бонус составляет: {self._income.get('wage') + self._income.get('bonus')}")


my_worker1 = Position("John", "Doe", "Engineer", 10000, 5000)
my_worker2 = Position("Bill", "Buffalo", "Shooter", 20000, 10000)
my_worker3 = Position("Коля", "Сидоров", "Тракторист", 7000, 1000)
my_worker1.get_full_name()
my_worker1.get_total_income()
my_worker2.get_full_name()
my_worker2.get_total_income()
my_worker3.get_full_name()
my_worker3.get_total_income()


# ======== 4 =========
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        if direction == "right":
            print(f"{self.name} повернул направо")
        elif direction == "left":
            print(f"{self.name} повернул налево")
        else:
            print("Неверное направление - доступно только left или right")

    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self.speed}")


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        print(f"Это {self.name}, цвет {self.color}, скорость {self.speed}")

    def show_speed(self):
        if self.speed > 60:
            print(f"В данный момент {self.name} превышает ограничение 60 - двигается со скоростью {self.speed}")
        else:
            print(f"Текущая скорость {self.name}: {self.speed}. Превышение скорости не зафиксировано")


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        print(f"Это {self.name}, цвет {self.color}, скорость {self.speed}")


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        print(f"Это {self.name}, цвет {self.color}, скорость {self.speed}")

    def show_speed(self):
        if self.speed > 40:
            print(f"В данный момент {self.name} превышает ограничение 40 - двигается со скоростью {self.speed}")
        else:
            print(f"Текущая скорость {self.name}: {self.speed}. Превышение скорости не зафиксировано")


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        print(f"Это {self.name}, цвет {self.color}, скорость {self.speed}")
        if self.is_police:
            print(f"{self.name} полицейская машина")
        else:
            print(f"{self.name} не полицейская машина")


town_car = TownCar(70, "Yellow", "Taxi", False)
sport_car = SportCar(150, "Black", "McLaren", False)
work_car = WorkCar(30, "Green", "Pickup", False)
police_car = PoliceCar(70, "Dark-blue", "Plymouth", True)
print("=" * 20)
town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()


# ========== 5 ==========
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка {self.title}")


my_stationery = Stationery("канцелярия")
my_pen = Pen("ручка")
my_pencil = Pencil("карандаш")
my_handle = Handle("маркер")
my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
