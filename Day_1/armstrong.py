input = 34534

def Armstrong(number):
    num = abs(number)
    
    sum = 0
    power = len(str(number))
    while(num>0):
    
        reminder = num %10 
        num = num//10
        sum = sum + reminder**power

    if sum < 0:
        sum = -sum

    if sum == number:
        return True
    else:
        return False

    

print(Armstrong(input))