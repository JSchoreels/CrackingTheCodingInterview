from typing import List


def display(matrix,n,m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end='')
        print()

def pond_size(lands : List[List[int]]):

    n = len(lands)
    m = len(lands[0])
    visited_lands = init_matrix_with_same_dim(n,m)

    for i in range(n):
        for j in range(m):
            if lands[i][j] > 0:
                visited_lands[i][j] = 'x'

    def scan_and_mark_pond(i, j, id):
        visited_lands[i][j] = id
        size = 1
        for i_radius in range(-1,2):
            for j_radius in range(-1,2):
                if not (i_radius == 0 and j_radius == 0) and i+i_radius < n and j+j_radius < m and i+i_radius>=0 and j+j_radius>=0 :
                    if visited_lands[i+i_radius][j+j_radius] == 0:
                        size += scan_and_mark_pond(i + i_radius, j + j_radius, id)
        return size

    id = 1
    all_size = []
    for i in range(len(lands)):
        for j  in range(len(lands)):
            if visited_lands[i][j] == 0:
                size = scan_and_mark_pond(i,j, id)
                all_size.append(size)
                id += 1
    display(visited_lands, n, m)
    return all_size


def init_matrix_with_same_dim(n,m):
    return [ [0 for i in range(n)] for j in range(m) ]

print(pond_size([
    [0, 2, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1]
]))