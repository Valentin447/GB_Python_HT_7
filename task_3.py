'''
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
'''


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
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


ivanov = Position("Иван", "Иванов", "слесарь", 17500, 11250)
petrov = Position("Петр", "Петров", "водитель", 16845, 10700)
print(ivanov.name)
print(ivanov.surname)
print(ivanov.position)
print(ivanov.get_full_name())
print(ivanov.get_total_income())
print(petrov.get_full_name())
print(petrov.get_total_income())
