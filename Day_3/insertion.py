num = [1, 5, 2, 8, 3, 4, 9]

def Insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]       # element to insert
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # shift right
            j -= 1

        arr[j + 1] = key      # insert key

    return arr

print(Insertion(num))
