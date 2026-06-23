numberlist1 = [1,1,2,3,4,6,3,4,3]
numberlist2 = [1,1,2,3,4,53,3,4,3]

feq3 = {}


feq = {}
feq2 = {}

    
for i in numberlist2:
    count = 0
    for j in numberlist1:
        # print(i,j)
        if i == j:
            count +=1
    feq[i] = count

hashed_list = [0]*11

for i in numberlist1:
    hashed_list[i] +=1

for j in numberlist2:
    if j < 0 or j >10:
        feq2[j] = 0
    else:
        feq2[j] = hashed_list[j]


print(feq)
print(feq2)
print(feq3)






