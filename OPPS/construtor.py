class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    
creta = Car("hyundai","creta")
e6 = Car("mahindra","6e")
s_class = Car("mercedes","s class")


car_list = [creta,e6,s_class]

for i in car_list:
    print(f"This car is {i.brand} {i.model}")