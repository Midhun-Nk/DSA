
def second(num):
    for i in range(0,len(num)):
        next_no = 0
        j=i
        while (num[i] <= num[i+1]):
            next_no = j
            j+=1
        if next_no != 0:
            num[i],num[next_no] = num[next_no],num[i] 
    print(num)

second([1,1,1,2,3,4,4,4,5,6,7 ])