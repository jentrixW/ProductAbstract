class Car: 
    brand = ""
    model = ""
    year = ""
    speed = ""
    mileage = 0

class ElectricCar(Car):
    battery_capacity = 0

class CEngineCar(Car):
    engine_capacity = 0

car = (Car)
car.year = 2020

electric_car = ElectricCar()
electric_car.battery_capacity = 2000

c_engine_car = CEngineCar()
c_engine_car.brand = "toyota"


print(f"CEngine car brand: {c_engine_car.brand}")



