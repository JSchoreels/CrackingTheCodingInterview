def tictac_win(grid):
    if res := check_rows(grid) : return res
    if res := check_columns(grid) : return res
    if res := check_diag(grid): return res
    if res := check_diag_rev(grid): return res
    return 0


def check_rows(grid):
    N = len(grid)
    for i in range(N):
        current_player = grid[i][0]
        j = 1
        while j < N and 0 < current_player == grid[i][j]:
            j += 1
        if j == N:
            return current_player
    return 0

def check_columns(grid):
    N = len(grid)
    for j in range(N):
        current_player = grid[0][j]
        i = 1
        while i < N and 0 < current_player == grid[i][j]:
            i += 1
        if i == N:
            return current_player


def check_diag(grid):
    N = len(grid)
    current_player = grid[0][0]
    i = 1
    while i < N and grid[i][i] == current_player:
        i += 1
    if i == N:
        return current_player


def check_diag_rev(grid):
    N = len(grid)
    current_player = grid[0][-1]
    i = 1
    while i < N and grid[i][-1-i] == current_player:
        i += 1
    if i == N:
        return current_player


assert tictac_win([
    [0,0,0],
    [0,0,0],
    [0,0,0]
]) == 0

assert tictac_win([
    [0,0,0],
    [1,1,1],
    [0,0,0]
]) == 1

assert tictac_win([
    [0,1,0],
    [0,1,0],
    [0,1,0]
]) == 1

assert tictac_win([
    [1,0,0],
    [0,1,0],
    [0,0,1]
]) == 1

assert tictac_win([
    [0,0,1],
    [0,1,0],
    [1,0,0]
]) == 1


assert tictac_win([
    [0,0,2],
    [0,2,0],
    [2,0,0]
]) == 2

assert tictac_win([
    [2,0,2],
    [0,2,0],
    [0,2,0]
]) == 0