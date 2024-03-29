# 10.11 Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
# to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent
# integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an
# array of integers, sort the array into an alternating sequence of peaks and valleys.


def peaks_and_valleys(arr):
    N = len(arr)
    for i in range(0, N, 2):
        print(arr)
        i_max, v_max = i, arr[i]
        for i in range(i+1, min(N, i+3)):
            if arr[i] > v_max:
                i_max, v_max = i, arr[i]
            if i+1 < N:
                arr[i+1], arr[i_max] = arr[i_max], arr[i+1]



arr = [i for i in range(20)]
peaks_and_valleys(arr)
print(arr)