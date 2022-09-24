def smallest_diff(arr1 : list, arr2 : list):
    sorted_arr1 = arr1.copy()
    sorted_arr2 = arr2.copy()
    sorted_arr1.sort()
    sorted_arr2.sort()
    N1 = len(sorted_arr1)
    N2 = len(sorted_arr2)
    i1 = 0
    i2 = 0
    min = -1
    min_pair = None
    while i1 < N1 and i2 < N2:
        print(f"Considering pair : {sorted_arr1[i1]}, {sorted_arr2[i2]}")
        if (new_min := abs(sorted_arr1[i1] - sorted_arr2[i2])) < min or min < 0:
            min = new_min
            min_pair = sorted_arr1[i1], sorted_arr2[i2]
        if sorted_arr1[i1] < sorted_arr2[i2]:
            i1 += 1
        else:
            i2 += 1
    return min, min_pair

print(smallest_diff([1,3,15,11,2],[23,127,235,19,8]))
print(smallest_diff([1,2,11,15],[4,12,19,23,127,235,500]))