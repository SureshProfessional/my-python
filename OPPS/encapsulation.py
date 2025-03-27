# capsulate brand attribute with private __

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return f"{self.__brand} !"

    def full_name(self):
        return f"'{self.__brand}' '{self.model}'"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


creta = Car("hyundai","creta")
# print(creta.__brand)
print(creta.model)
print(f"Full name method : {creta.full_name()}\nGetter method : {creta.get_brand()}")

print("-------------------------------------------")

tesla = ElectricCar("tesla","model s","100kWh")
# print(tesla.__brand)
print(tesla.model , tesla.battery_size)
print(tesla.full_name())
print(f"Getter method : {tesla.get_brand()}")

