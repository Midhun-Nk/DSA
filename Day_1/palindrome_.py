
number = 1213121

def check(num):
    temp = num
    sum = 0
    while temp > 0:
        sum = sum *10
        remainder = temp % 10
        temp = temp // 10
        sum += remainder

    if num == sum:
        return True
    else:
        return False




print(check(number))