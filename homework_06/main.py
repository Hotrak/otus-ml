from car import Car
from engine import Engine
from plane import Plane

# Создаем автомобиль
car = Car(weight=1500, fuel=50, fuel_consumption=0.1)
engine = Engine(volume=2.0, pistons=4)
car.set_engine(engine)

car.start()
print("Машина заведена:", car.started)
car.move(100)
print("Оставшееся топливо в машине:", car.fuel)

# Создаем самолет
plane = Plane(weight=10000, fuel=500, fuel_consumption=5, max_cargo=2000)
plane.load_cargo(1500)
print("Груз на самолете:", plane.cargo)
plane.load_cargo(400)  # Это вызовет исключение CargoOverload
