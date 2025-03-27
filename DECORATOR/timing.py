import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"{func.__name__} run in {int(end_time-start_time)} second ")
        return result
    return wrapper

@timer
def run_program(n=1):
    return time.sleep(n)
    
run_program(5)