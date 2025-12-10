list1 = [4,2,4,7,3,2,6,1,3,8]
list2 = [9,8,6,7,5,3,4,2,1,0]

# Build frequency hash for list1
hashed_list = {}
for num in list1:
    hashed_list[num] = hashed_list.get(num, 0) + 1

# Build result based on order of list2
result = {}
for item in list2:
    result[item] = hashed_list.get(item, 0)

print(result)

# hash_list = [0]*11

# for num in list2:
#     if num in list1:
#         hash_list[num] +=1

# result ={}

# for num in list2:
#     if num < 0 | num>10:
#         result[num] = 0
#     else:
#         result[num] = hash_list[num]
    

# print(result)


