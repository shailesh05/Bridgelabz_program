def binary(data, target):
    low = 0
    upper = len(data) - 1
    while low <= upper:
        mid = (low + upper) // 2
        if target == data[mid]:
            return mid+1
        elif target < data[mid]:
                upper = mid - 1
        else:
            low = mid + 1
    return False


data =sorted([12,78,98,65])
target = 12
print(binary(data, target))
