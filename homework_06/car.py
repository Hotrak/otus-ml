from base import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine):
        """Устанавливает двигатель для автомобиля."""
        self.engine = engine
