class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"MODEL : {self.brand}\nCAR : {self.model}"    



creta = Car("hyundai","creta")
s_class = Car("mercedes","s_class")
print(creta.full_name())
print(s_class.full_name())

