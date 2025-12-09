from math import sqrt
number = 36

def factors(number):
    factorList = []
    for num in range(1,number+1):
        if number % num == 0:
            factorList.append(num)
    
    return factorList;

print(factors(number))


def optimalFact(number):
    factorList = []
    square = int(sqrt(number))

    for num in range(1,square+1):
        if number % num == 0:
            diviser = number // num
            factorList.append(num)
            if diviser != num:
                factorList.append(diviser)
                factorList.sort()

    return factorList

print(optimalFact(number))

    

            