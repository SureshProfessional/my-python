number = [1,-2,1,1,5,1,6,-3,2,4,2,-2,-3]

total_positive_number = 0
total_negative_number = 0

for i in number:
    if i >= 0:
        total_positive_number += 1
    else:
        total_negative_number += 1

print("total positive number is ",total_positive_number)
print("total negative number is ",total_negative_number)


