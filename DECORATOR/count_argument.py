
def debug(func):
    def wrapper(*args, **kwargs):
        
        return func(*args,**kwargs)
        

    return wrapper


def greet(name="suresh",greeting="Hello"):
    return f"{greeting}{name}"

print(greet("priya","kem cho "))
