import time

tries = 0
wait_time = 1
max_attempts = 5

while tries < max_attempts:
    print(f"Your attempte : {tries+1} and wait time : {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2
    tries += 1