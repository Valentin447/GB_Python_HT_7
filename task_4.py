'''
4) Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и
также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print("Автомобиль движется вперед")

    @staticmethod
    def stop():
        print("Автомобиль остановился")

    @staticmethod
    def turn(direction):
        print(f"Автомобиль повернул на{direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена")
        print(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена")
        print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


wc = WorkCar(30, "oranj", "Камаз", False)
pc = PoliceCar(100, "white", "Ford", True)

print(f"Скорость: {wc.speed}; цвет: {wc.color}; марка: {wc.name}; "
      f"является полицейской: {wc.is_police}")
print(f"Скорость: {pc.speed}; цвет: {pc.color}; марка: {pc.name}; "
      f"является полицейской: {pc.is_police}")
wc.show_speed()
wc.speed = 70
wc.show_speed()
pc.show_speed()
pc.speed = 170
pc.show_speed()

wc.go()
wc.stop()
wc.turn("лево")
