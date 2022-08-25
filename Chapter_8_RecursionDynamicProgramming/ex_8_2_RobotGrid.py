def robot_grid(grid):
    r = len(grid)
    c = len(grid[0])

    def robot_grid(i,j):
        print(f"at position {i},{j}")
        if i+1 == r and j+1 == c:
            return ""
        else:
            if i+1 < r and grid[i+1][j] != 1:
                possible_path = robot_grid(i+1, j)
                if possible_path is not None:
                    return 'D' + possible_path
            if j+1 < c and grid[i][j+1] != 1:
                possible_path = robot_grid(i, j+1)
                if possible_path is not None:
                    return 'R' + possible_path
            return None
    return robot_grid(0,0)


if __name__ == '__main__':
    grid = [
        [0,0,0,0,0],
        [0,1,1,1,1],
        [0,0,0,1,1],
        [0,1,0,0,0],
        [0,1,0,1,1],
        [0,1,0,0,0],
    ]
    path = robot_grid(grid)
    print(path)
    assert path == "DDRRDDDRR"
    grid[5][4]=1
    assert robot_grid(grid) == None