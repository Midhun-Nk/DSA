num = [1,5,2,8,3,4,9]


def BubbleSort(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)-i-1):
            if list[i]>=list[j]:
                list[i],list[j] = list[j],list[i]

    return list

print(BubbleSort(num))