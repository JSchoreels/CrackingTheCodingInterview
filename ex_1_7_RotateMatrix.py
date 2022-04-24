# Rotate Matrix : Given an image represented by a N x N matrix, where each pixel in the image is represented by an
# integer, write a method to rotate the image by 90 degrees. Can you do this in place ?

def gen_square_matrix(n):
    return [list(map(lambda x: x+n*i, range(0, n))) for i in range(n)]

def rotate(matrix):
    n = len(matrix)
    for i in range(n//2+n%2): # for odd n number, we need to take the "middle row"
        for j in range(n//2): # if we take the middle column here, we will process the rotation 2 times for the same items
            tmp=matrix[i][j]
            matrix[i][j] = matrix[-1-j][i]
            matrix[-1-j][i] = matrix[-1-i][-1-j]
            matrix[-1-i][-1-j] = matrix[j][-1-i]
            matrix[j][-1 - i] = tmp
    return matrix

def matrix_equal(m1, m2):
    if len(m1) != len(m2): return False
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]): return False
        for j in range(len(m1[i])):
            if m1[i][j] != m2[i][j]:
                return False
    return True


def main():
    even_matrix_4 = gen_square_matrix(4)
    odd_matrix_5 = gen_square_matrix(5)
    rotate(odd_matrix_5)
    assert matrix_equal(odd_matrix_5, [[20, 15, 10, 5, 0], [21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4]]) # careful, the odd_matrix_5 is the rotated one now
    rotate(even_matrix_4)
    assert matrix_equal(even_matrix_4, [[12, 8, 4, 0], [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3]]) # careful, the even_matrix_4 is the rotated one now


if __name__ == "__main__":
    main()