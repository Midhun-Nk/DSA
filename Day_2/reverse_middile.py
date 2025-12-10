list1 = [1,4,2,6,5,3,7,9,2]
left = 0 
right=len(list1)-1
def Reverse(list1,left,right):

    if left > right:
        return
    
    temp = list1[left]
    list1[left] = list1[right]
    list1[right] = temp

    # list1[left],list1[right] = list1[right],list1[left]

    Reverse(list1,left+1,right-1)


Reverse(list1,3,7)
print(list1)