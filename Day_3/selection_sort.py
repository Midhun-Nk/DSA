num = [1,5,2,8,3,4,9]

for i in range(len(num)):
    minIndex = i
    
    for j in range(i+1,len(num)):
        if num[j] <= num[minIndex]:
            minIndex = j
            pos = j
    num[i],num[minIndex] = num[minIndex],num[i]

print(num)
        