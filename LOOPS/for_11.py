import random

a = ["apple","banana","orange","kavy","dragon fruite","water melon"]
b = random.sample(a,len(a))

res = {i : j for i,j in zip(a,b) }
print(res)
    