# recursive mean you call function inside function

def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number-1)
    
print(fact(5))