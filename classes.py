class Car():
    color = ""
    model = ""
    speed = ""
    brand = ""
    fuel_tank = 0
    number_of_wheels = 0
    engine_size = 0
    mileage = 0
    year = 0

    def current_speed(self):
        print(f"Current speed is {self.speed}")
    def navigation(self, direction): 
        print(f"Turn {direction}")   

#constructors
    def _init_(self, brand, model):
        self.brand = brand 
        self.model = model
        




car_one = Car()    #car_one is an instance/object of the class car
car_one.brand = 'Tesla'
car_one.model = 'Model S'
car_one.engine_size = 396
car_one.number_of_wheels = 4
car_one.mileage = 0
car_one.speed = 280
car_one.colour = 'wine red' 

print(f"Mary's car model: {car_one.model}")
car_one.current_speed()
car_one.navigation("left")
