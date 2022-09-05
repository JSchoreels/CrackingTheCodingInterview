# 8.12 Eight Queens:Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
# so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
# diagonals, not just the two that bisect the board.


def eight_queens():
    def eight_queens_with_initial(queens_position, i):
        if i >= GRID_SIZE:
            valid_positions.append(queens_position.copy())
            valid_positions.append(list(map(lambda  j : GRID_SIZE-1-j, queens_position)))
        else:
            at_least_one_position_possible = False
            for j in range(GRID_SIZE):
                position_is_possible = check_no_colision(i, j, queens_position)
                if position_is_possible:
                    queens_position[i] = j
                    eight_queens_with_initial(queens_position, i + 1)
                    at_least_one_position_possible = True
            if not at_least_one_position_possible:
                return

    def check_no_colision(i, j, queens_position):
        for previous_i in range(i):
            if queens_position[previous_i] == j or abs(j - queens_position[previous_i]) == abs(i - previous_i):
                return False
        return True

    GRID_SIZE = 8
    queens_position = [-1] * GRID_SIZE # Represent for Queen in Row (index) in which columns she can be assigne
    valid_positions = []
    for i in range(GRID_SIZE // 2): # Other case will be handled by symmetry
        queens_position[0] = i
        eight_queens_with_initial(queens_position, 1)
    return valid_positions

def display(queens_position):
    for i,j in enumerate(queens_position):
        print("| "*j+"|x|"+" |"*(7-j))

results = eight_queens()
for result in results:
    print("---")
    display(result)
print(len(results))