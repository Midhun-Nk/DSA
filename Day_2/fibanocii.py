
def fibanocii(num):
    if num == 0 or num == 1:
        return num
    
    return fibanocii(num-1) + fibanocii(num-2) 

print(fibanocii(5))