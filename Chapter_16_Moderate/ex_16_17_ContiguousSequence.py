# 16.17 Contiguous Sequence: You are given an array of integers (both positive and negative). Find the
# contiguous sequence with the largest sum. Return the sum


def contiguous_sequence(arr):
    current_seg_sum = 0
    max_seg_sum = 0
    for i in range(len(arr)):
        current = arr[i]
        current_seg_sum += current
        if current_seg_sum > max_seg_sum:
            max_seg_sum = current_seg_sum
        if current_seg_sum < 0:
            current_seg_sum = 0
    return max_seg_sum

print(contiguous_sequence([2, 3, -8, -1, 2, 4, -2, 3]))