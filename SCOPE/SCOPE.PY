# name = "suryabhai"

# def home():
#     name = "suresh"
#     print(name)

# print(name)
# home()

# a = 100

# def glob(b):
#     c =a +b
#     return c

# print(glob(1))

# def glob2():
#     global a
#     a = 88
#     return a

# print(a)
# print(glob2())

a = 10

def func1():
    a = 20
    
    def func2():
        print(a)
    
    return func2

name1 = func1()
name1()

def suryacoder(mynumber):
    def rute(power):
        val = mynumber ** power
        return val
    return rute

z = suryacoder(9)
y = z(2)
print(y)