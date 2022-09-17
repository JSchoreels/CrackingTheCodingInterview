# 10.9 Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element.

def sorted_matrix_search(matrix, elt):
    N = len(matrix)
    M = len(matrix[0])
    def search(i_left_top, j_left_top, i_right_bottom, j_right_bottom):
        # print(f"Searching for {elt} in box : {i_left_top},{j_left_top} ({matrix[i_left_top][j_left_top]}) - {i_right_bottom},{j_right_bottom} ({matrix[i_right_bottom][j_right_bottom]})")
        if i_left_top < 0 or j_left_top < 0 or i_right_bottom < 0 or j_right_bottom < 0 or i_left_top > i_right_bottom or j_left_top > j_right_bottom:
            # raise ValueError('Check the box corners')
            return
        i_mid = i_left_top + (i_right_bottom - i_left_top) // 2
        j_mid = j_left_top + (j_right_bottom - j_left_top) // 2
        selected_value = matrix[i_mid][j_mid]
        # print(f"Selected Value : {selected_value}")
        if selected_value == elt:
            return i_mid,j_mid
        elif i_left_top == i_right_bottom and j_left_top == j_right_bottom:
            return None
        elif selected_value > elt:
            if i_mid > i_left_top and j_mid > j_left_top and (top_left_rec := search(i_left_top, j_left_top, i_mid-1, j_mid-1)):
                return top_left_rec
            elif i_mid > i_left_top and (top_right_rec := search(i_left_top, j_mid, i_mid-1, j_right_bottom)):
                return top_right_rec
            elif j_mid > j_left_top and (bottom_left_rec := search(i_mid, j_left_top, i_right_bottom, j_mid-1)):
                return bottom_left_rec
        else:
            if j_mid < j_right_bottom and (top_right_rec := search(i_left_top, j_mid+1, i_mid, j_right_bottom)):
                return top_right_rec
            elif i_mid < i_right_bottom and (bottom_left_rec := search(i_mid+1, j_left_top, i_right_bottom, j_mid)):
                return bottom_left_rec
            elif i_mid < i_right_bottom and j_mid < j_right_bottom and (bottom_right_rec := search(i_mid+1, j_mid+1, i_right_bottom, j_right_bottom)):
                return bottom_right_rec
    return search(0,0, N-1, M-1)


matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

for i in range(26):
    result = sorted_matrix_search(matrix, i + 1)
    print(f"found {i+1} at {result}")
    if i+1 < 26:
        assert matrix[result[0]][result[1]] == i+1
    else:
        assert result == None
