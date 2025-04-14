"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        """Загружает груз на самолет, если нет перегруза."""
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload("Превышение максимальной грузоподъемности.")

    def remove_all_cargo(self):
        """Удаляет весь груз и возвращает его количество."""
        cargo_to_return = self.cargo
        self.cargo = 0
        return cargo_to_return
