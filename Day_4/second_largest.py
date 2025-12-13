
num = [1,5,2,8,3,4,9]


def commonMethod(num):
    sorted_num = sorted(num)
    second_largest =  sorted_num[-2]
    return second_largest

print(commonMethod(num))


def withoutSorting(num):
    largest = float("-inf")
    second_largest = float("-inf")

    for i in range(len(num)):
        if num[i] > largest:
            largest = num[i]

    for j in range(len(num)):
        if num[j] > second_largest and num[j]<largest:
            second_largest = num[j]

    return second_largest

print(withoutSorting(num))


def Optimal(num):
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(len(num)):

        if num[i]> largest:
            second_largest=largest
            largest = num[i]
    return second_largest

print(Optimal(num))
        
