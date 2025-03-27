

# number = 6
# sum1 = 0
# for i in range(1,number+1):
#     sum1 = sum1+i

# print(sum1)

# for i in range(1,number+1):
#     if i % 2 == 1:
#         print(i)
#         sum1 += i

# print(sum1)

# str1 = "malaalam"
# reverse_str = ""

# for i in str1:
#     reverse_str = i + reverse_str
# if reverse_str == str1:
#     print(str1,"is palidram")
# else:
#     print(str1,"is not palidram")
    

# print armstrong number



for i in range(1,4679307774+1):
    len1 = len(str(i))
    sum = 0
    for j in str(i):
        j = int(j)
        sum = sum + j**len1
        if i == sum:
            print(f"{sum}")






    




