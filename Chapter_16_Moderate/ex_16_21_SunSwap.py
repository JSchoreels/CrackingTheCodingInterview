from typing import List


def sum_swap(arr1 : List[int], arr2 : List[int]):
    arr1.sort()
    arr2.sort()
    sum_arr1 = sum(arr1)
    sum_arr2 = sum(arr2)
    diff_sum_arr12 = sum_arr1 - sum_arr2
    if diff_sum_arr12 % 2 != 0:
        raise ValueError(f"Both arr1 and arr2 must have an even diff sum. Actual diff : {diff_sum_arr12}")
    seeked_delta = diff_sum_arr12 // 2
    i1 = 0
    i2 = 0
    while i1 < len(arr1) and i2 < len(arr2):
        current_diff = arr1[i1] - arr2[i2]
        if current_diff == seeked_delta:
            return arr1[i1], arr2[i2]
        elif i2 < len(arr2) and current_diff > seeked_delta:
            i2 += 1
        elif i1 < len(arr1):
            i1 += 1
        else:
            return None


print(sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))
