def binary_search(data_array, high, target, low = 0):
    if high >= low:
        mid = (high + low) // 2

        if data_array[mid] == target:
            return mid
        elif data_array[mid] > target:
            return binary_search(data_array, mid - 1, target, low)
        else:
            return binary_search(data_array, high, target, mid + 1)

    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10
 
result = binary_search(arr, len(arr) - 1, x)
 
if result != -1:
    print("Data yang dicari ada di index ke: ", result)
else:
    print("Data yang dicari tidak dimukan!")
