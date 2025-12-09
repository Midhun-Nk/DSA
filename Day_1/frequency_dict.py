input  = [1,2,3,4,5,1,2,3,5,4,4,4,3]


def freqOccerence(list):
    frequence = {}
    for num in list:
        if num in frequence:
            frequence[num] +=1
        else:
            frequence[num] = 1
    return frequence

print(freqOccerence(input))

def OptimalFreq(list):
    freq = {}
    for num in list:
        freq[list[num]] = freq.get(list[num],0)+1

    
    
    return freq

print(OptimalFreq(input))

