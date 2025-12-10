string = "asdfsdfgdzxcvzx"
letter = ["a","z","f","x","z","d"]
hashed_list = {}
result= {}



for char in string:
    hashed_list[char] = hashed_list.get(char,0)+1

for char in letter:
    result[char]= hashed_list.get(char,0)

print(result)



# hashed_list = [0]*26



# for char in string:
#     ascii_value =  ord(char)
#     ascii_value = ascii_value-97
#     hashed_list[ascii_value] = hashed_list[ascii_value]+1

# for char in letter:
#     ascii_value = ord(char)
#     ascii_value = ascii_value-97
#     result[char] = hashed_list[ascii_value]

# print(result)

