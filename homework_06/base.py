from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel, CargoOverload

class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        """
        Инициализатор класса Vehicle.

        :param weight: Вес транспортного средства
        :param fuel: Количество топлива
        :param fuel_consumption: Расход топлива (на единицу расстояния)
        """
        self.weight = weight
        self.started = False 
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """
        Метод для запуска двигателя. Если транспорт не запущен, проверяется наличие топлива.
        Если топлива нет, выбрасывается исключение LowFuelError.
        """
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Недостаточно топлива для запуска двигателя.")

    def move(self, distance):
        """
        Метод для перемещения транспортного средства на указанное расстояние.
        Проверяет, достаточно ли топлива для преодоления дистанции.
        Если топлива недостаточно, выбрасывается исключение NotEnoughFuel.

        :param distance: Расстояние, которое необходимо преодолеть
        """
        required_fuel = distance * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel("Недостаточно топлива для преодоления указанной дистанции.")
