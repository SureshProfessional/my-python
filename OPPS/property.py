# access by class not by object

class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return {self.__brand}
    
    def full_name(self):
        return f"'{self.__brand}' '{self.__model}'"
    
    def fuel_type(self):
        return "PETROL & DESIEL"
    
    @staticmethod   
    def general_des():
        return "This is my dream car"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "ELECTRIC CHARGE"



creta = Car("HYUNDAI","CRETA")
tesla = ElectricCar("TESLA","MODEL_S","100kWh")

# creta.model = "suresh"

print(f"I am {creta.get_brand()} {creta.model} i need {creta.fuel_type()}")
print(f"I am {tesla.get_brand()} {tesla.model} i need {tesla.fuel_type()}")
print(f"{ElectricCar.general_des()}")
