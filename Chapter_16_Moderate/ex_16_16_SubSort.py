# 16.16 Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted
# elements m throughn , the entire array would be sorted. Minimize n - m (that is, find the smallest
# such sequence).
# EXAMPLE
# Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
# Output: (3, 9)


def sub_sort(arr):
    N = len(arr)
    end_prefix = 0
    start_suffix = N-1
    while end_prefix + 1 < N:
        if arr[end_prefix+1] < arr[end_prefix]:
            break
        end_prefix += 1
    if end_prefix + 1 == N: ## If everything was sorted, just end here
        return None
    while start_suffix - 1 > 0:
        if arr[start_suffix-1] > arr[start_suffix]:
            break
        start_suffix -= 1
    min_mid = None
    max_mid = None
    for i in range(end_prefix+1, start_suffix+1):
        if not min_mid or min_mid > arr[i]:
            min_mid = arr[i]
        if not max_mid or max_mid < arr[i]:
            max_mid = arr[i]
    # Shrink prefix and suffix to match max/min of the mid
    while end_prefix >= 0 and arr[end_prefix-1] > min_mid:
        end_prefix -= 1
    while start_suffix < N and arr[start_suffix+1] < max_mid:
        start_suffix += 1
    return end_prefix, start_suffix

arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(sub_sort(arr))