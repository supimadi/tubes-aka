def binary_search(data: list, target):
    low = 0
    high = len(data) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return f"Ditemukan di index ke: {mid}"

    return "Tidak Ditemukan"

data_testing = [2, 3, 4, 10, 40]
target = 2
 
print(binary_search(data_testing, target))
