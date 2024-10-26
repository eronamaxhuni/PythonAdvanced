class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"make: {self.make}, model: {self.model}, year: {self.year}")

class Car(Vehicle):
    def __init__(self,make, model,year,body_style):
        super().__init__(make,model,year,body_style)
        self.body_style=body_style

class ElectricCar(Car):
    def __init__(self,make, model,year,body_style,battery_capacity):
        self.battery_capacity = battery_capacity
    def Charge(self):
        print(f"Charging the electric car")

tesla =ElectricCar("tesla","cybertruck",2023,"triangular",112.4)
print(tesla.ElectricCar)