import math

def circle_fun(radius):
    Circumference = 2 * math.pi * radius
    area = math.pi *(radius**2)
    return Circumference,area


c,a = circle_fun(3)
print(f"Circumference : {round(c,2)}\narea : {round(a,)}")