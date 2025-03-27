def even(number):
    for i in range(2,number+1):
        if i % 2 == 0:
            yield i
    
for i in even(10):
    print(i)