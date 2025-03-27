number = int(input("Enter number : "))

def hello():
    if number % 5 == 0:
        return "hello"
    else:
        return "bye"

def electricity():
    if number <= 100 :
        print("charge is 0")
    elif number <= 200:
        print(number)

