input = "Malayalam"
input = input.upper()


def Palindrom(input):
    right = len(input)-1
    for left in range(0,len(input)-1):
        
        if left>=right:
            return True


        
        if input[left] != input[right]:
            print(input[left])
            print(input[right])
            return False
        else :
            right = right -1
        
    return True

print(Palindrom(input))

right = len(input)-1
def RecuPalindrome(input,left,right):
    if left >= right:
        return True
    
    if input[left] != input[right]:
        return False
    
    return RecuPalindrome(input,left+1,right-1)

print(RecuPalindrome(input,0,right))
        