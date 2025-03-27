# polymorphism mean 1 person can do multiple work

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return {self.__brand}

    def full_name(self):
        return f"'{self.__brand}' '{self.model}'"
    
    def fuel_type(self):
        return "PETROL & DESIEL"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "ELECTRIC CHARGE"




print("---------------------------------------------------------------")

creta = Car("hyundai","creta")
# # print(creta.__brand)
# print(creta.model)
# print(f"Full name method : {creta.full_name()}\nGetter method : {creta.get_brand()}")

print(f"I am {creta.get_brand()} {creta.model} i need {creta.fuel_type()}")

print("---------------------------------------------------------------")

tesla = ElectricCar("tesla","model s","100kWh")
# # print(tesla.__brand)
# print(tesla.model , tesla.battery_size)
# print(tesla.full_name())
# print(f"Getter method : {tesla.get_brand()}")
print(f"I am {tesla.get_brand()} {tesla.model} i need {tesla.fuel_type()}")

print("---------------------------------------------------------------")
