# Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume that the array was
# originally sorted in increasing order.

# input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
# Output: 8 (the index of 5 in the array)

def search_in_rotated(arr, item):
    offset = 0
    N = len(arr)
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            offset = i
            break
    def search(start, end):
        mid = (start + ((end - start) % N) // 2) % N
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return search(start, (mid-1)%N)
        else:
            return search((mid+1)%N, end)
    return search(offset, (offset-1)%N)


result1 = search_in_rotated([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5)
result2 = search_in_rotated([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 15)
result3 = search_in_rotated([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 14)

print(result1)
assert result1 == 8
print(result2)
assert result2 == 0
print(result3)
assert result3 == 11
