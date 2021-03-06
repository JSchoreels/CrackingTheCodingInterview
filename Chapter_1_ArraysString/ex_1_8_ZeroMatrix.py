# Zero Matrix
# Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0

def gen_square_matrix(n):
    return [list(map(lambda x: x+n*i, range(0, n))) for i in range(n)]

def zero_matrix(matrix):
    m = len(matrix)
    n = 0
    if m > 0:
        n = len(matrix[0])
    i_to_erase = []
    j_to_erase = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                i_to_erase.append(i)
                j_to_erase.append(j)
    for i in i_to_erase:
        for j in range(n):
            matrix[i][j] = 0
    for j in j_to_erase:
        for i in range(m):
            matrix[i][j] = 0

def zero_matrix_opti(matrix):
    m = len(matrix)
    n = 0
    if m > 0:
        n = len(matrix[0])
    first_row_to_erase = 0 in matrix[0] # we will use the first row to mark rows to delete, so we need to remember the state of it
    first_column_to_erase = 0 in [matrix[i][0] for i in range(m)] # idem for first column
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == 0: # if element = 0, we mark the first column and row for future deletion
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1,m): # we will erase first row/column after the rest of the matrix
        if matrix[i][0] == 0: # if row marked for deletion
            for j in range(1,n):
                matrix[i][j] = 0
    for j in range(1,n):
        if matrix[0][j] == 0: # we will erase first row/column after the rest of the matrix
            for i in range(1,m): # if column marked for deletion
                matrix[i][j] = 0
    if first_column_to_erase: # now we can put 0 in the first column without altering the rest
        for i in range(m):
            matrix[i][0] = 0
    if first_row_to_erase: # now we can put 0 in the first row without altering the rest
        for j in range(n):
            matrix[0][j] = 0


matrix = gen_square_matrix(5)
matrix[0][0] = 1
matrix[1][0] = 0
matrix[0][4] = 0
matrix[2][2] = 0
zero_matrix_opti(matrix)
assert matrix == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 16, 0, 18, 0], [0, 21, 0, 23, 0]]