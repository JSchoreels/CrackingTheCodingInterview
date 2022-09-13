def sorted_merge(arr1, n_arr1, arr2):
    if len(arr1) < len(arr2) + n_arr1:
        raise ValueError("Arr1 not big enough to store all items")
    i = n_arr1 + len(arr2) - 1
    arr1_i = n_arr1-1
    arr2_i = len(arr2)-1
    while arr2_i >= 0:
        if arr1[arr1_i] > arr2[arr2_i]:
            arr1[i] = arr1[arr1_i]
            arr1_i -= 1
        else:
            arr1[i] = arr2[arr2_i]
            arr2_i -= 1
        i -= 1
    return arr1


arr1 = [1,3,5,0,0,0,0,0]
arr2 = [2,4,6]
n_arr1 = 3
result1 = sorted_merge(arr1, n_arr1, arr2)
print(result1)
result2 = sorted_merge([4, 5, 6, 0, 0, 0, 0, 0], 3, [1, 2, 3])
print(result2)
result3 = sorted_merge([1, 2, 3, 0, 0, 0, 0, 0], 3, [4, 5, 6])
print(result3)
assert result1 == result2 == result3 == [1, 2, 3, 4, 5, 6, 0, 0]