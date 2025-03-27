class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"BRAND : '{self.brand}' and MODEL : '{self.model}'"
    
class ElectricCar(Car):
    
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size



creta = Car("hyundai","creta")
print(creta.brand)
print(creta.model)
print(creta.full_name())

be_6e = ElectricCar("mahindra","be_6e","100kWh")
print(be_6e.brand ,be_6e.model , be_6e.battery_size)
print(be_6e.full_name())
