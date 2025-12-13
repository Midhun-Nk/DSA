num = [1,5,2,8,3,4,9]
maximum = float("-inf")


print(maximum)
for i in range (len(num)):
    
    if num[i] > maximum:
        maximum = num[i]

print(maximum)


